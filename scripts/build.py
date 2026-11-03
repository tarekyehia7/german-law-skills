#!/usr/bin/env python3
"""Build portable AI skill packs from the Gesetze-fuer-KI/bundesrecht Markdown mirror.

Usage: build.py <mirror_dir> <codes.json> <out_dir>

mirror_dir is a clone of github.com/Gesetze-fuer-KI/bundesrecht (one <xx>/<slug>.md per law,
synced nightly with gesetze-im-internet.de). keywords.json next to codes.json is picked up automatically.

For every law in codes.json this produces

  laws/<skill>/SKILL.md   – skill entry point: metadata, outline, how to use
  laws/<skill>/toc.md     – every § / Art with its heading and the chunk file
  laws/<skill>/text/*.md  – the full law text split into chunks ≤ MAX_CHUNK bytes

plus a top-level SKILL.md router that tells the AI which law to open.
"""
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

SNAPSHOT = "unknown"  # set in main() from the mirror's last commit date
MAX_CHUNK = 100_000  # bytes; ~25k tokens, comfortable for any model to read whole

HEADING_RE = re.compile(r"^(#{1,6}) (.*)$")
# § 12, §§ 3 bis 6, Art 1, Artikel 1, (XXXX) § 10 (weggefallen)
PARA_RE = re.compile(r"^(?:\(XXXX\) )?(§+|Art\.?|Artikel|Anlage|Anhang|Schlussformel|Eingangsformel|Präambel)(?=\s|$)", re.I)


def slugify(s: str, n: int = 60) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("ß", "ss")
    s = s.encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s[:n].rstrip("-") or "teil"


def read_meta(lines):
    """Front matter + the definition-list header of the mirror file."""
    meta = {}
    i = 0
    starts = [k for k in range(min(12, len(lines))) if lines[k].strip() == "---"]
    if starts:
        i = starts[0] + 1
        while i < len(lines) and lines[i].strip() != "---":
            if ":" in lines[i]:
                k, v = lines[i].split(":", 1)
                meta[k.strip()] = v.strip()
            i += 1
        i += 1
    # the H1 is the reliable title: "# Long title (JURABK)"
    for line in lines[i:i + 20]:
        if line.startswith("# "):
            h1 = line[2:].strip()
            meta["Title"] = re.sub(r"\s*\([^()]*\)\s*$", "", h1) or h1
            break
    # definition list: "Key\n:   value"
    body_start = i
    key = None
    for j in range(i, min(len(lines), i + 400)):
        line = lines[j]
        if HEADING_RE.match(line) and not line.startswith("# "):
            body_start = j
            break
        if line.startswith(":   ") and key:
            meta.setdefault(key, line[4:].strip())
            key = None
        elif line.strip() and not line.startswith("#"):
            key = line.strip()
    return meta, body_start


def parse(lines, body_start):
    """Return list of nodes: dict(level, title, is_para, lines)."""
    nodes = []
    cur = None
    stack = {}  # level -> structural heading title, for breadcrumbs
    for line in lines[body_start:]:
        m = HEADING_RE.match(line)
        if m:
            level, title = len(m.group(1)), m.group(2).strip()
            is_para = bool(PARA_RE.match(title))
            if not is_para:
                stack = {k: v for k, v in stack.items() if k < level}
                stack[level] = title
            crumbs = [stack[k] for k in sorted(stack) if is_para or k < level]
            cur = {"level": level, "title": title, "is_para": is_para, "crumbs": crumbs, "lines": [line]}
            nodes.append(cur)
        elif cur is not None:
            cur["lines"].append(line)
    return nodes


def size(nodes):
    return sum(len("\n".join(n["lines"])) + 1 for n in nodes)


def group(nodes):
    """Group nodes into chunks ≤ MAX_CHUNK, splitting on structural headings.

    Strategy: find the shallowest structural (non-§) heading level L. Cut at
    every heading with level ≤ L. Any chunk still too big is recursively cut at
    the next deeper structural level; if no deeper level exists, cut by §.
    """
    struct_levels = sorted({n["level"] for n in nodes if not n["is_para"]})

    def split_at(nodes, levels_left):
        if size(nodes) <= MAX_CHUNK or not nodes:
            return [nodes]
        if not levels_left:
            # cut by paragraph count
            out, cur = [], []
            for n in nodes:
                if cur and size(cur) + size([n]) > MAX_CHUNK:
                    out.append(cur)
                    cur = []
                cur.append(n)
            if cur:
                out.append(cur)
            return out
        L = levels_left[0]
        parts, cur = [], []
        for n in nodes:
            if n["level"] <= L and not n["is_para"] and cur:
                parts.append(cur)
                cur = []
            cur.append(n)
        if cur:
            parts.append(cur)
        out = []
        for p in parts:
            out.extend(split_at(p, levels_left[1:]))
        return out

    chunks = split_at(nodes, struct_levels)
    # a chunk holding only structural headings (e.g. a bare "Buch 1") is glued to the next one
    glued, carry = [], []
    for c in chunks:
        if not any(n["is_para"] for n in c):
            carry += c
            continue
        glued.append(carry + c)
        carry = []
    if carry:
        if glued:
            glued[-1] += carry
        else:
            glued.append(carry)
    # merge tiny neighbours so we do not end up with 300 files of 2 KB
    merged = []
    for c in glued:
        if merged and size(merged[-1]) + size(c) <= MAX_CHUNK // 2:
            merged[-1] = merged[-1] + c
        else:
            merged.append(c)
    return merged


def para_label(title):
    t = re.sub(r"^\(XXXX\) ", "", title)
    return t


def chunk_title(chunk):
    for n in chunk:
        if not n["is_para"]:
            return " › ".join(n["crumbs"] + [n["title"]])
    if chunk[0]["crumbs"]:
        return " › ".join(chunk[0]["crumbs"]) + " › " + para_range(chunk)
    # pure § chunk: use first and last §
    first = para_label(chunk[0]["title"]).split(" ")
    last = para_label(chunk[-1]["title"]).split(" ")
    return f"{' '.join(first[:2])} bis {' '.join(last[:2])}"


def para_range(chunk):
    paras = [para_label(n["title"]) for n in chunk if n["is_para"]]
    if not paras:
        return ""
    short = lambda p: " ".join(p.split(" ")[:2]).rstrip(",;")
    return short(paras[0]) if len(paras) == 1 else f"{short(paras[0])} – {short(paras[-1])}"


def build_law(mirror, code, out_root, kw=None):
    kw = kw or {"de": [], "en": [], "ar": []}
    slug = code["slug"]
    src = Path(mirror) / slug[:2] / f"{slug}.md"
    if not src.exists():  # legacy bundestag/gesetze layout
        src = next(iter(Path(mirror).glob(f"*/{slug}/index.md")), None)
    if src is None:
        print(f"!! missing {code['slug']}", file=sys.stderr)
        return None
    lines = src.read_text(encoding="utf-8").splitlines()
    meta, body_start = read_meta(lines)
    # normalise the two mirror formats to one set of keys
    stand = meta.get("stand") or meta.get("Zuletzt geändert durch", "")
    meta["Zuletzt geändert durch"] = re.sub(r"^zuletzt geändert durch\s+", "", stand.strip(), flags=re.I)
    meta["Ausfertigungsdatum"] = (meta.get("ausfertigung") or meta.get("Ausfertigungsdatum", "")).strip("'\"")
    meta["quelle"] = meta.get("quelle") or f"https://www.gesetze-im-internet.de/{slug}/"
    nodes = parse(lines, body_start)
    chunks = group(nodes)

    skill_dir = Path(out_root) / "laws" / code["skill"]
    text_dir = skill_dir / "text"
    text_dir.mkdir(parents=True, exist_ok=True)
    for old in text_dir.glob("*.md"):
        old.unlink()

    jurabk = re.sub(r" \d{4}$", "", meta.get("abkuerzung") or meta.get("jurabk") or code["slug"].upper())
    title = meta.get("Title", jurabk)
    outline, toc_rows = [], []
    width = len(str(len(chunks)))
    for i, chunk in enumerate(chunks, 1):
        ct = chunk_title(chunk)
        fname = f"{str(i).zfill(width)}-{slugify(ct.split(' › ')[-1])}.md"
        rng = para_range(chunk)
        head = [f"# {title} ({jurabk})", f"## Teil {i}/{len(chunks)}: {ct}", f"*{rng}* · Quelle: {meta['quelle']} · Stand: {meta.get('Zuletzt geändert durch') or 'siehe SKILL.md'} · Abruf: {SNAPSHOT}", ""]
        (text_dir / fname).write_text("\n".join(head + ["\n".join(n["lines"]) for n in chunk]) + "\n", encoding="utf-8")
        outline.append((i, ct, rng, fname, sum(len('\n'.join(n['lines'])) for n in chunk)))
        for n in chunk:
            if n["is_para"]:
                toc_rows.append((para_label(n["title"]), fname))
            else:
                toc_rows.append((("#" * (n["level"] - 1)) + " " + n["title"], fname))

    n_paras = sum(1 for n in nodes if n["is_para"])
    total = sum(o[4] for o in outline)

    # SKILL.md
    desc = (f"Full German text of the {title} ({jurabk}) – {code['en']}. "
            f"Use when a question concerns German {code['area']} and the exact wording of a § of the {jurabk} is needed.")
    sk = [
        "---",
        f"name: {code['skill']}",
        f"description: {json.dumps(desc, ensure_ascii=False)}",
        "metadata:",
        f"  jurabk: {json.dumps(jurabk, ensure_ascii=False)}",
        f"  title: {json.dumps(title, ensure_ascii=False)}",
        f"  area: {code['area']}",
        f"  ausfertigungsdatum: {meta.get('Ausfertigungsdatum', '')}",
        f"  stand: {json.dumps(meta.get('Zuletzt geändert durch', ''), ensure_ascii=False)}",
        f"  source: {meta['quelle']}",
        f"  mirror: https://github.com/Gesetze-fuer-KI/bundesrecht/blob/main/{src.parent.name}/{src.name}",
        f"  snapshot: {SNAPSHOT}",
        f"  paragraphs: {n_paras}",
        f"  chunks: {len(chunks)}",
        f"  size_bytes: {total}",
        "---",
        "",
        f"# {title} ({jurabk})",
        "",
        f"**Area:** {code['area']}  ",
        f"**Covers:** {code['en']}  ",
        f"**Text state:** {meta.get('Zuletzt geändert durch', 'unknown')} (text retrieved {SNAPSHOT} from a mirror that syncs nightly with gesetze-im-internet.de; verify the current wording at the source link above before relying on it).",
        "",
        "## How to use this skill",
        "",
        "1. Identify the § (or Art.) you need. If you only know the topic, scan the outline below, or open `toc.md` and search the heading keywords.",
        "2. Open **only** the chunk file in `text/` that contains that §. Each chunk is self-contained and under 100 KB.",
        "3. Quote the German wording verbatim and cite it as `§ <nr> <Abs.> <jurabk>` (e.g. `§ 433 Abs. 1 BGB`). Translate or explain afterwards, keeping the quote separate from your interpretation.",
        "4. `(weggefallen)` means the § was repealed. Headings marked `(XXXX)` are placeholders for repealed ranges.",
        "5. This is statute text only – no case law, no commentary. For anything decision-relevant, name the text state above and recommend checking the current version at the source and consulting a lawyer.",
        "",
        "## Keywords / Stichwörter / كلمات مفتاحية",
        "",
        "Questions in any language that mention these topics belong to this law:",
        "",
        f"- **DE:** {', '.join(kw['de'])}",
        f"- **EN:** {', '.join(kw['en'])}",
        f"- **AR:** {'، '.join(kw['ar'])}",
        "",
        "## Outline (chunk → content)",
        "",
        "| # | File | Section | Paragraphs | Size |",
        "|---|------|---------|------------|------|",
    ]
    for i, ct, rng, fname, sz in outline:
        sk.append(f"| {i} | `text/{fname}` | {ct} | {rng} | {sz // 1000} KB |")
    sk += ["", f"Full paragraph index: `toc.md` ({n_paras} paragraphs)."]
    (skill_dir / "SKILL.md").write_text("\n".join(sk) + "\n", encoding="utf-8")

    # toc.md
    toc = [f"# {title} ({jurabk}) – Inhaltsverzeichnis", "", "Format: `heading → text/<file>`", ""]
    for label, fname in toc_rows:
        if label.startswith("#"):
            toc.append(f"\n{label}  \n`text/{fname}`\n")
        else:
            toc.append(f"- {label} → `text/{fname}`")
    (skill_dir / "toc.md").write_text("\n".join(toc) + "\n", encoding="utf-8")

    return {"skill": code["skill"], "jurabk": jurabk, "title": title, "area": code["area"], "en": code["en"],
            "paragraphs": n_paras, "chunks": len(chunks), "size": total, "stand": meta.get("Zuletzt geändert durch", ""),
            "keywords": kw}


def build_router(results, out_root):
    areas = {}
    for r in results:
        areas.setdefault(r["area"], []).append(r)
    lines = [
        "---",
        "name: german-law",
        "description: \"Router for German federal law (deutsches Bundesrecht). Use for any question about German statutes – civil, criminal, commercial, labour, social, tax, immigration, administrative, traffic law – to find which law (BGB, StGB, HGB, SGB, AufenthG, ...) applies, then open that law's skill under laws/ to read the exact § wording in German.\"",
        "metadata:",
        f"  laws: {len(results)}",
        f"  paragraphs: {sum(r['paragraphs'] for r in results)}",
        "  language: de",
        f"  text_state: gesetze-im-internet.de via github.com/Gesetze-fuer-KI/bundesrecht, retrieved {SNAPSHOT}",
        "---",
        "",
        "# German Law (Bundesrecht) – Skill Router",
        "",
        f"{len(results)} federal laws, {sum(r['paragraphs'] for r in results):,} paragraphs of original German statute text, split so an AI can load exactly the part it needs.",
        "",
        "## Workflow",
        "",
        "1. **Classify the question** into one of the areas below and pick the law(s). When unsure between two, open both.",
        "2. **Open `laws/<skill>/SKILL.md`** – it has a short outline table that maps topics to chunk files.",
        "3. **Open the single chunk** `laws/<skill>/text/<file>.md` with the § you need (or search `toc.md` by keyword first). Never load all chunks at once.",
        "4. **Answer with the exact German wording**, cited as `§ 433 Abs. 1 BGB`, then explain/translate. Mark your own interpretation clearly.",
        f"5. **Always add**: the text was retrieved {SNAPSHOT} (each law's SKILL.md names its last amendment) and is not legal advice; check the source for changes since.",
        "",
        "## Any language works / أي لغة تعمل",
        "",
        "Questions may be asked in **German, English, Arabic or any other language**. Each law's `SKILL.md` lists its topics in DE / EN / AR under *Keywords*, and `laws/keywords.md` is the combined trilingual index: search it for a word from the question (e.g. `فصل من العمل`, `fired`, `Kündigung`) to find the law, then open that law's skill. The statute text itself is German; quote it in German and translate afterwards.",
        "",
        "## Quick routing hints",
        "",
        "- Contract, purchase, rent, damages, divorce, inheritance, custody → **BGB**; which country's law applies → **EGBGB**",
        "- Company (GmbH, AG, OHG/KG), accounting, commercial register → **GmbHG / AktG / HGB**; bankruptcy → **InsO**",
        "- Fired, notice period, overtime, holidays, works council → **KSchG, BGB §§ 611a-630, ArbZG, BUrlG, BetrVG**",
        "- Crime and punishment → **StGB**; police, arrest, trial → **StPO**; fines like parking/speeding → **OWiG, StVO, StVG**",
        "- Visa, residence permit, Blue Card, citizenship, asylum → **AufenthG, StAG, AsylG**",
        "- Health insurance, pension, unemployment money, Bürgergeld, care → **SGB V, VI, III, II, XI**",
        "- Income tax, VAT, tax procedure → **EStG, UStG, AO**",
        "- Suing someone, enforcement, court costs → **ZPO, GVG, GKG, RVG**; suing an authority → **VwGO, VwVfG**",
        "- Data protection, cookies, Impressum → **BDSG, TTDSG, DDG**",
        "- Constitutional rights → **GG**",
        "",
        "## Laws by area",
        "",
    ]
    for area, rs in areas.items():
        lines += [f"### {area}", "", "| Law | Skill folder | Covers | §§ |", "|-----|-------------|--------|----|"]
        for r in rs:
            lines.append(f"| **{r['jurabk']}** – {r['title']} | `laws/{r['skill']}/` | {r['en']} | {r['paragraphs']} |")
        lines.append("")
    (Path(out_root) / "SKILL.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (Path(out_root) / "laws" / "index.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    kwl = ["# Trilingual keyword index · Stichwortindex · فهرس الكلمات المفتاحية", "",
           "Search this file for a word from the question in German, English or Arabic. Each hit names the law and its skill folder.", ""]
    for r in results:
        kwl += [f"## {r['jurabk']} – {r['title']}  →  `laws/{r['skill']}/`", "",
                f"- **DE:** {', '.join(r['keywords']['de'])}",
                f"- **EN:** {', '.join(r['keywords']['en'])}",
                f"- **AR:** {'، '.join(r['keywords']['ar'])}", ""]
    (Path(out_root) / "laws" / "keywords.md").write_text("\n".join(kwl) + "\n", encoding="utf-8")


def main():
    global SNAPSHOT
    mirror, codes_path, out_root = sys.argv[1:4]
    try:
        import subprocess
        SNAPSHOT = subprocess.run(["git", "-C", mirror, "log", "-1", "--format=%cs"], capture_output=True, text=True, check=True).stdout.strip() or SNAPSHOT
    except Exception:
        pass
    codes = json.loads(Path(codes_path).read_text(encoding="utf-8"))
    kw_path = Path(codes_path).with_name("keywords.json")
    keywords = json.loads(kw_path.read_text(encoding="utf-8")) if kw_path.exists() else {}
    results = []
    for code in codes:
        r = build_law(mirror, code, out_root, keywords.get(code["slug"]))
        if r:
            results.append(r)
            print(f"{r['jurabk']:<12} {r['paragraphs']:>5} §§  {r['chunks']:>3} chunks  {r['size'] // 1000:>5} KB")
    build_router(results, out_root)
    print(f"\n{len(results)} laws, {sum(r['paragraphs'] for r in results)} paragraphs, {sum(r['size'] for r in results) // 1_000_000} MB")


if __name__ == "__main__":
    main()
