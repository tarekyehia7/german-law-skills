# German Law Skills · Deutsches Bundesrecht als AI-Skills

The full German text of **82 core federal laws (17,064 paragraphs)**, packaged as portable *skills* that any AI assistant (Claude, ChatGPT, Gemini, Cursor, local models, ...) can load on demand and quote the exact § wording from.

```
SKILL.md                      ← router: which law applies to a question
laws/
  index.json                  ← machine-readable list of all laws
  bgb-buergerliches-gesetzbuch/
    SKILL.md                  ← metadata + outline table (section → chunk file → §§)
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
```

Every file is plain Markdown, so the pack works wherever an AI can read files.

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
| Datenschutz und Digitales | BDSG, TTDSG, TMG |
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

- **Source:** official texts from [gesetze-im-internet.de](https://www.gesetze-im-internet.de/) via the Markdown mirror [bundestag/gesetze](https://github.com/bundestag/gesetze).
- **Snapshot date: 26 March 2022.** Amendments after that date (e.g. the 2023 BGB/StGB changes, Bürgergeld reform of SGB II, Fachkräfteeinwanderungsgesetz 2023 in AufenthG, Staatsangehörigkeitsreform 2024) are **not** in the text. Every `SKILL.md` carries the exact *Zuletzt geändert durch* line of its law so you can tell what is covered.
- **Statute text only.** No case law, no commentary, no translation. German language.
- **Not legal advice.** The skills instruct the AI to say so and to recommend checking the current version at the source link.

## Rebuilding / updating

```bash
git clone --depth 1 https://github.com/bundestag/gesetze.git /tmp/gesetze
python3 scripts/build.py /tmp/gesetze scripts/codes.json .
```

To add a law, append an entry to `scripts/codes.json` (`slug` = folder name in the mirror, e.g. `b/bgb` → `bgb`). To update the text to the current state, run the official XML through a Markdown conversion (or wait for the mirror to update) and rebuild. The build is deterministic, so a rebuild on the same input produces no diff.

## License

German statutes and regulations are public domain under § 5 UrhG. The mirror is released into the public domain (Unlicense). The build scripts and skill files in this repository are released under the same terms: use them for anything.
