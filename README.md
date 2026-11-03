# German Law Skills · Deutsches Bundesrecht als AI-Skills

The full German text of **82 core federal laws (17,064 paragraphs)**, packaged as portable *skills* that any AI assistant (Claude, ChatGPT, Gemini, Cursor, local models, ...) can load on demand and quote the exact § wording from.

```
SKILL.md                      ← router: which law applies to a question
laws/
  index.json                  ← machine-readable list of all laws
  keywords.md                 ← trilingual topic index (DE / EN / AR) → law
  bgb-buergerliches-gesetzbuch/
    SKILL.md                  ← metadata, DE/EN/AR keywords, outline table (section → chunk file → §§)
    toc.md                    ← every § with its heading and chunk file
    text/
      01-buch-1-allgemeiner-teil.md
      02-abschnitt-3-rechtsgeschafte.md
      ...                     ← full law text, chunks ≤ 100 KB, § never split
  stgb-strafgesetzbuch/
  aufenthg-aufenthaltsrecht/
  ... (82 laws)
scripts/
  build.py                    ← regenerates everything from the source mirror
  codes.json                  ← which laws to include + one-line descriptions
  keywords.json               ← German / English / Arabic topic keywords per law
```

Every file is plain Markdown, so the pack works wherever an AI can read files.

**Ask in any language.** Every law carries its topics in German, English and Arabic (≈4,500 keywords in total), and `laws/keywords.md` is the combined index, so a question like *"I got fired without notice"* or *"اتفصلت من الشغل من غير إنذار"* routes to KSchG and BGB § 622 just as *"fristlose Kündigung"* does. The statute text itself is German; the skills instruct the AI to quote it in German and then translate.

## Which laws are included

| Area | Laws |
|------|------|
| Verfassungsrecht | GG, BVerfGG |
| Zivilrecht | BGB, EGBGB, ProdHaftG, AGG, WEG, VVG |
| Handels- und Gesellschaftsrecht | HGB, GmbHG, AktG, UmwG, InsO |
| Wettbewerbs- und IP-Recht | UWG, GWB, UrhG, MarkenG, PatG |
| Arbeitsrecht | KSchG, BetrVG, ArbZG, BUrlG, TzBfG, MiLoG, EntgFG, MuSchG, BBiG, ArbGG, TVG, AÜG, ArbSchG |
| Strafrecht | StGB, StPO, OWiG, BtMG, WaffG |
| Prozessrecht | ZPO, FamFG, GVG, ZVG, GKG, RVG |
| Verwaltungsrecht | VwVfG, VwGO, GewO, IFG |
| Datenschutz und Digitales | BDSG, TTDSG, DDG (successor of the TMG) |
| Migrationsrecht | AufenthG, StAG, AsylG |
| Sozialrecht | SGB I–XII (I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII), WoGG, BAföG |
| Steuerrecht | AO, EStG, KStG, GewStG, UStG, ErbStG, GrEStG, FGO |
| Verkehrsrecht | StVG, StVO, FeV |
| Immobilienrecht | GBO, BeurkG |
| Familien- und Personenrecht | PStG, LPartG, VersAusglG |

The complete list with paragraph counts is in [`SKILL.md`](SKILL.md) and [`laws/index.json`](laws/index.json).

## How to use it with your AI

### Claude Code / Claude Agent SDK
Clone the repo into `.claude/skills/` of a project (or `~/.claude/skills/` for all projects):

```bash
git clone https://github.com/tarekyehia7/german-law-skills ~/.claude/skills/german-law
```

Claude discovers `SKILL.md` automatically. Ask a question like *"Was sagt § 573 BGB zur Kündigung durch den Vermieter?"* and it opens the router, then the BGB skill, then only the tenancy chunk.

### Claude.ai (Projects / Skills upload)
Upload the folder of **one law** (e.g. `laws/bgb-buergerliches-gesetzbuch/`) as a skill or as project knowledge. Each law folder is self-contained. Upload `SKILL.md` from the root as well if you want the router.

### ChatGPT (Custom GPT / Projects)
Create a GPT or Project and upload the chunk files of the laws you need from `laws/<law>/text/` plus that law's `SKILL.md`. Paste the *How to use this skill* section of the law's `SKILL.md` into the instructions.

### Gemini (Gems), Cursor, Windsurf, Copilot, local models
Point the tool at the cloned folder (Cursor: add it to the workspace; Gemini Gem: upload the files). The `SKILL.md` files are the instructions, the `text/` files are the knowledge.

### Any other agent
Give the agent file-read access to the repo and tell it: *"Read `SKILL.md` first; for a law, read `laws/<law>/SKILL.md` and then only the one chunk under `text/` that contains the §."*

## Important: text state and limits

- **Source:** official texts from [gesetze-im-internet.de](https://www.gesetze-im-internet.de/) via the Markdown mirror [Gesetze-fuer-KI/bundesrecht](https://github.com/Gesetze-fuer-KI/bundesrecht), which syncs with the official site every night.
- **Text state:** each `SKILL.md` carries its law's official *Zuletzt geändert durch* line and the `snapshot` date the text was retrieved (see the root `SKILL.md` for the pack-wide date). Laws change; rebuild to refresh.
- **Statute text only.** No case law, no commentary, no translation. German language.
- **Not legal advice.** The skills instruct the AI to say so and to recommend checking the current version at the source link.

## Rebuilding / updating

```bash
git clone --depth 1 https://github.com/Gesetze-fuer-KI/bundesrecht.git /tmp/bundesrecht
python3 scripts/build.py /tmp/bundesrecht scripts/codes.json .
```

The mirror is updated nightly, so rerunning these two commands refreshes every law to the current official text. To add a law, append an entry to `scripts/codes.json` (`slug` = file name in the mirror, e.g. `bg/bgb.md` → `bgb`) and its keywords to `scripts/keywords.json`. The build is deterministic, so a rebuild on the same input produces no diff.

## License

German statutes and regulations are public domain under § 5 UrhG. The mirror's maintainers publish the texts under the same public-domain terms. The build scripts and skill files in this repository are released under the same terms: use them for anything.
