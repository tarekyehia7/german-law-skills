---
name: german-law
description: "Router for German federal law (deutsches Bundesrecht). Use for any question about German statutes – civil, criminal, commercial, labour, social, tax, immigration, administrative, traffic law – to find which law (BGB, StGB, HGB, SGB, AufenthG, ...) applies, then open that law's skill under laws/ to read the exact § wording in German."
metadata:
  laws: 82
  paragraphs: 17064
  language: de
  text_state: gesetze-im-internet.de snapshot via github.com/bundestag/gesetze (2022-03-26)
---

# German Law (Bundesrecht) – Skill Router

82 federal laws, 17,064 paragraphs of original German statute text, split so an AI can load exactly the part it needs.

## Workflow

1. **Classify the question** into one of the areas below and pick the law(s). When unsure between two, open both.
2. **Open `laws/<skill>/SKILL.md`** – it has a short outline table that maps topics to chunk files.
3. **Open the single chunk** `laws/<skill>/text/<file>.md` with the § you need (or search `toc.md` by keyword first). Never load all chunks at once.
4. **Answer with the exact German wording**, cited as `§ 433 Abs. 1 BGB`, then explain/translate. Mark your own interpretation clearly.
5. **Always add**: the text is the 2022 state of the law and not legal advice; newer amendments may apply.

## Quick routing hints

- Contract, purchase, rent, damages, divorce, inheritance, custody → **BGB**; which country's law applies → **EGBGB**
- Company (GmbH, AG, OHG/KG), accounting, commercial register → **GmbHG / AktG / HGB**; bankruptcy → **InsO**
- Fired, notice period, overtime, holidays, works council → **KSchG, BGB §§ 611a-630, ArbZG, BUrlG, BetrVG**
- Crime and punishment → **StGB**; police, arrest, trial → **StPO**; fines like parking/speeding → **OWiG, StVO, StVG**
- Visa, residence permit, Blue Card, citizenship, asylum → **AufenthG, StAG, AsylG**
- Health insurance, pension, unemployment money, Bürgergeld, care → **SGB V, VI, III, II, XI**
- Income tax, VAT, tax procedure → **EStG, UStG, AO**
- Suing someone, enforcement, court costs → **ZPO, GVG, GKG, RVG**; suing an authority → **VwGO, VwVfG**
- Data protection, cookies, Impressum → **BDSG, TTDSG, TMG**
- Constitutional rights → **GG**

## Laws by area

### Verfassungsrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **GG** – Grundgesetz für die Bundesrepublik Deutschland | `laws/gg-grundgesetz/` | Basic Law (constitution): fundamental rights, federal structure, state organs, legislation, judiciary | 204 |
| **BVerfGG** – Gesetz über das Bundesverfassungsgericht | `laws/bverfgg-verfassungsgericht/` | Federal Constitutional Court Act: constitutional complaints, procedure before the BVerfG | 134 |

### Zivilrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **BGB** – Bürgerliches Gesetzbuch | `laws/bgb-buergerliches-gesetzbuch/` | Civil Code: contracts, obligations, torts, property, family law, inheritance, tenancy, sales, consumer protection | 2527 |
| **BGBEG** – Einführungsgesetz zum Bürgerlichen Gesetzbuche | `laws/egbgb-einfuehrungsgesetz-bgb/` | Introductory Act to the Civil Code: private international law (which country's law applies), transitional rules, consumer information duties | 461 |
| **ProdHaftG** – Gesetz über die Haftung für fehlerhafte Produkte | `laws/prodhaftg-produkthaftung/` | Product Liability Act: strict liability of manufacturers for defective products | 19 |
| **AGG** – Allgemeines Gleichbehandlungsgesetz | `laws/agg-gleichbehandlung/` | General Equal Treatment Act: anti-discrimination in employment and civil contracts | 33 |
| **WoEigG** – Gesetz über das Wohnungseigentum und das Dauerwohnrecht | `laws/weg-wohnungseigentum/` | Condominium Act: ownership of apartments, owners' associations, management | 52 |
| **VVG** – Gesetz über den Versicherungsvertrag | `laws/vvg-versicherungsvertrag/` | Insurance Contract Act: rights and duties of insurers and policyholders | 223 |

### Handels- und Gesellschaftsrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **HGB** – Handelsgesetzbuch | `laws/hgb-handelsgesetzbuch/` | Commercial Code: merchants, commercial register, commercial partnerships (OHG, KG), accounting, commercial transactions | 680 |
| **GmbHG** – Gesetz betreffend die Gesellschaften mit beschränkter Haftung | `laws/gmbhg-gmbh/` | Limited Liability Companies Act: founding, managing directors, shareholders, liability of a GmbH | 125 |
| **AktG** – Aktiengesetz | `laws/aktg-aktiengesetz/` | Stock Corporation Act: AG founding, management board, supervisory board, shareholders' meeting, corporate groups | 388 |
| **UmwG** – Umwandlungsgesetz | `laws/umwg-umwandlung/` | Transformation Act: mergers, splits, change of legal form of companies | 341 |
| **InsO** – Insolvenzordnung | `laws/inso-insolvenzordnung/` | Insolvency Code: insolvency proceedings, creditors, administrator, consumer insolvency, discharge of residual debt | 411 |

### Wettbewerbs- und IP-Recht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **UWG** – Gesetz gegen den unlauteren Wettbewerb | `laws/uwg-unlauterer-wettbewerb/` | Unfair Competition Act: misleading advertising, aggressive practices, cease-and-desist claims | 28 |
| **GWB** – Gesetz gegen Wettbewerbsbeschränkungen | `laws/gwb-kartellrecht/` | Act against Restraints of Competition: antitrust, cartels, abuse of dominance, merger control, public procurement | 235 |
| **UrhG** – Gesetz über Urheberrecht und verwandte Schutzrechte | `laws/urhg-urheberrecht/` | Copyright Act: protected works, author rights, licences, limitations, enforcement | 254 |
| **MarkenG** – Gesetz über den Schutz von Marken und sonstigen Kennzeichen | `laws/markeng-markenrecht/` | Trade Mark Act: registration, protection and infringement of trade marks | 193 |
| **PatG** – Patentgesetz | `laws/patg-patentrecht/` | Patent Act: patentability, application, patent infringement | 173 |

### Arbeitsrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **KSchG** – Kündigungsschutzgesetz | `laws/kschg-kuendigungsschutz/` | Protection Against Dismissal Act: when a dismissal is socially unjustified, lawsuits against dismissal | 28 |
| **BetrVG** – Betriebsverfassungsgesetz | `laws/betrvg-betriebsverfassung/` | Works Constitution Act: works councils, co-determination in the workplace | 148 |
| **ArbZG** – Arbeitszeitgesetz | `laws/arbzg-arbeitszeit/` | Working Hours Act: maximum working hours, breaks, rest periods, Sunday work | 27 |
| **BUrlG** – Mindesturlaubsgesetz für Arbeitnehmer | `laws/burlg-urlaub/` | Federal Leave Act: minimum paid vacation for employees | 18 |
| **TzBfG** – Gesetz über Teilzeitarbeit und befristete Arbeitsverträge | `laws/tzbfg-teilzeit-befristung/` | Part-Time and Fixed-Term Employment Act: part-time rights, limits on fixed-term contracts | 24 |
| **MiLoG** – Gesetz zur Regelung eines allgemeinen Mindestlohns | `laws/milog-mindestlohn/` | Minimum Wage Act: statutory minimum wage | 24 |
| **EntgFG** – Gesetz über die Zahlung des Arbeitsentgelts an Feiertagen und im Krankheitsfall | `laws/entgfg-entgeltfortzahlung/` | Continued Remuneration Act: pay during sickness and public holidays | 15 |
| **MuSchG** – Gesetz zum Schutz von Müttern bei der Arbeit, in der Ausbildung und im Studium | `laws/muschg-mutterschutz/` | Maternity Protection Act: protection of pregnant and breastfeeding employees | 34 |
| **BBiG** – Berufsbildungsgesetz | `laws/bbig-berufsbildung/` | Vocational Training Act: apprenticeships (Ausbildung), training contracts, exams | 114 |
| **ArbGG** – Arbeitsgerichtsgesetz | `laws/arbgg-arbeitsgerichte/` | Labour Court Act: procedure before the labour courts | 145 |
| **TVG** – Tarifvertragsgesetz | `laws/tvg-tarifvertrag/` | Collective Agreements Act: binding effect of collective bargaining agreements | 16 |
| **AÜG** – Gesetz zur Regelung der Arbeitnehmerüberlassung | `laws/aueg-arbeitnehmerueberlassung/` | Temporary Employment Act: agency work, equal pay for temp workers | 31 |
| **ArbSchG** – Gesetz über die Durchführung von Maßnahmen des Arbeitsschutzes zur Verbesserung der Sicherheit und des Gesundheitsschutzes der Beschäftigten bei der Arbeit | `laws/arbschg-arbeitsschutz/` | Occupational Safety and Health Act: employer duties for safety at work | 29 |

### Strafrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **StGB** – Strafgesetzbuch | `laws/stgb-strafgesetzbuch/` | Criminal Code: general principles of criminal liability, sentencing, and all offences (theft, fraud, assault, homicide, etc.) | 559 |
| **StPO** – Strafprozeßordnung | `laws/stpo-strafprozessordnung/` | Code of Criminal Procedure: investigation, arrest, pre-trial detention, trial, appeals, rights of the accused | 684 |
| **OWiG** – Gesetz über Ordnungswidrigkeiten | `laws/owig-ordnungswidrigkeiten/` | Regulatory Offences Act: fines (Bußgeld) for administrative offences, procedure | 148 |
| **BtMG** – Gesetz über den Verkehr mit Betäubungsmitteln | `laws/btmg-betaeubungsmittel/` | Narcotics Act: controlled substances and drug offences | 51 |
| **WaffG** – Waffengesetz | `laws/waffg-waffenrecht/` | Weapons Act: possession, licences and prohibitions for weapons | 84 |

### Prozessrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **ZPO** – Zivilprozessordnung | `laws/zpo-zivilprozessordnung/` | Code of Civil Procedure: civil lawsuits, evidence, judgments, appeals, enforcement (Zwangsvollstreckung), default proceedings (Mahnverfahren) | 1079 |
| **FamFG** – Gesetz über das Verfahren in Familiensachen und in den Angelegenheiten der freiwilligen Gerichtsbarkeit | `laws/famfg-familienverfahren/` | Act on Proceedings in Family Matters: divorce, custody, maintenance proceedings, guardianship, probate, registers | 518 |
| **GVG** – Gerichtsverfassungsgesetz | `laws/gvg-gerichtsverfassung/` | Courts Constitution Act: court system, jurisdiction of Amtsgericht, Landgericht, OLG, BGH | 216 |
| **ZVG** – Gesetz über die Zwangsversteigerung und die Zwangsverwaltung | `laws/zvg-zwangsversteigerung/` | Forced Sale Act: foreclosure auctions and receivership of real property | 230 |
| **GKG** – Gerichtskostengesetz | `laws/gkg-gerichtskosten/` | Court Fees Act: court costs and fee tables | 87 |
| **RVG** – Gesetz über die Vergütung der Rechtsanwältinnen und Rechtsanwälte | `laws/rvg-anwaltsverguetung/` | Lawyers' Remuneration Act: statutory lawyer fees | 81 |

### Verwaltungsrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **VwVfG** – Verwaltungsverfahrensgesetz | `laws/vwvfg-verwaltungsverfahren/` | Administrative Procedure Act: administrative acts, hearings, revocation, public-law contracts | 118 |
| **VwGO** – Verwaltungsgerichtsordnung | `laws/vwgo-verwaltungsgerichtsordnung/` | Code of Administrative Court Procedure: lawsuits against authorities, interim relief | 214 |
| **GewO** – Gewerbeordnung | `laws/gewo-gewerbeordnung/` | Trade Regulation Act: starting a business (Gewerbeanmeldung), licences, prohibitions | 167 |
| **IFG** – Gesetz zur Regelung des Zugangs zu Informationen des Bundes | `laws/ifg-informationsfreiheit/` | Freedom of Information Act: access to federal government information | 15 |

### Datenschutz und Digitales

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **BDSG** – Bundesdatenschutzgesetz | `laws/bdsg-datenschutz/` | Federal Data Protection Act: national supplement to the GDPR, employee data, data protection officers | 86 |
| **TTDSG** – Gesetz über den Datenschutz und den Schutz der Privatsphäre in der Telekommunikation und bei Telemedien | `laws/ttdsg-telekommunikation-telemedien-datenschutz/` | Telecommunications-Telemedia Data Protection Act: cookies, confidentiality of communications | 30 |
| **TMG** – Telemediengesetz | `laws/tmg-telemedien/` | Telemedia Act: provider information (Impressum), liability of hosting providers | 17 |

### Migrationsrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **AufenthG** – und die Integration von Ausländern im Bundesgebiet | `laws/aufenthg-aufenthaltsrecht/` | Residence Act: visas, residence permits, Blue Card, settlement permit, family reunification, deportation | 180 |
| **RuStAG** – Staatsangehörigkeitsgesetz | `laws/stag-staatsangehoerigkeit/` | Nationality Act: acquiring and losing German citizenship, naturalisation requirements | 48 |
| **AsylVfG** – Asylgesetz | `laws/asylg-asyl/` | Asylum Act: asylum procedure, refugee status, subsidiary protection | 127 |

### Sozialrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **SGB 1** – Sozialgesetzbuch (SGB) Erstes Buch (I) - Allgemeiner Teil - (Artikel I des Gesetzes vom 11. Dezember 1975, BGBl. I S. 3015) | `laws/sgb-1-allgemeiner-teil/` | Social Code I: general principles of social benefits, rights and duties of claimants | 81 |
| **SGB 2** – Sozialgesetzbuch (SGB) Zweites Buch (II) - Grundsicherung für Arbeitsuchende - (Artikel 1 des Gesetzes vom 24. Dezember 2003, BGBl. I S. 2954) | `laws/sgb-2-grundsicherung/` | Social Code II: basic income support for jobseekers (Bürgergeld / formerly Hartz IV) | 144 |
| **SGB 3** – Sozialgesetzbuch (SGB) Drittes Buch (III) - Arbeitsförderung - (Artikel 1 des Gesetzes vom 24. März 1997, BGBl. I S. 594) | `laws/sgb-3-arbeitsfoerderung/` | Social Code III: unemployment insurance, unemployment benefit (Arbeitslosengeld I), job promotion | 385 |
| **SGB 4** – Sozialgesetzbuch (SGB) Viertes Buch (IV) - Gemeinsame Vorschriften für die Sozialversicherung - (Artikel I des Gesetzes vom 23. Dezember 1976, BGBl. I S. 3845) | `laws/sgb-4-sozialversicherung-gemeinsam/` | Social Code IV: common rules of social insurance, contributions, employment status | 196 |
| **SGB 5** – Sozialgesetzbuch (SGB) Fünftes Buch (V) - Gesetzliche Krankenversicherung - (Artikel 1 des Gesetzes v. 20. Dezember 1988, BGBl. I S. 2477) | `laws/sgb-5-krankenversicherung/` | Social Code V: statutory health insurance, insured persons, benefits, contributions | 666 |
| **SGB 6** – Sozialgesetzbuch (SGB) Sechstes Buch (VI) - Gesetzliche Rentenversicherung - (Artikel 1 des Gesetzes v. 18. Dezember 1989, BGBl. I S. 2261, 1990 I S. 1337) | `laws/sgb-6-rentenversicherung/` | Social Code VI: statutory pension insurance, retirement age, pension calculation | 509 |
| **SGB 7** – Siebtes Buch Sozialgesetzbuch - Gesetzliche Unfallversicherung - (Artikel 1 des Gesetzes vom 7. August 1996, BGBl. I S. 1254) | `laws/sgb-7-unfallversicherung/` | Social Code VII: statutory accident insurance, work accidents, occupational diseases | 252 |
| **SGB 8** – Sozialgesetzbuch (SGB) - Achtes Buch (VIII) - Kinder- und Jugendhilfe - (Artikel 1 des Gesetzes v. 26. Juni 1990, BGBl. I S. 1163) | `laws/sgb-8-kinder-jugendhilfe/` | Social Code VIII: child and youth welfare, daycare, Jugendamt | 163 |
| **SGB 9** – Sozialgesetzbuch Neuntes Buch – Rehabilitation und Teilhabe von Menschen mit Behinderungen – (Artikel 1 des Gesetzes v. 23. Dezember 2016, BGBl. I S. 3234) | `laws/sgb-9-rehabilitation-behinderung/` | Social Code IX: rehabilitation and participation of people with disabilities | 247 |
| **SGB 10** – Zehntes Buch Sozialgesetzbuch - Sozialverwaltungsverfahren und Sozialdatenschutz - | `laws/sgb-10-verwaltungsverfahren-sozialdaten/` | Social Code X: administrative procedure of social agencies, social data protection | 134 |
| **SGB 11** – Sozialgesetzbuch (SGB) - Elftes Buch (XI) - Soziale Pflegeversicherung (Artikel 1 des Gesetzes vom 26. Mai 1994, BGBl. I S. 1014) | `laws/sgb-11-pflegeversicherung/` | Social Code XI: long-term care insurance, care levels (Pflegegrade) | 217 |
| **SGB 12** – Sozialgesetzbuch (SGB) Zwölftes Buch (XII) - Sozialhilfe - (Artikel 1 des Gesetzes vom 27. Dezember 2003, BGBl. I S. 3022) | `laws/sgb-12-sozialhilfe/` | Social Code XII: social assistance, basic income in old age and reduced earning capacity | 195 |
| **WoGG** – Wohngeldgesetz | `laws/wogg-wohngeld/` | Housing Benefit Act: rent subsidies (Wohngeld) | 51 |
| **BAföG** – Bundesgesetz über individuelle Förderung der Ausbildung | `laws/bafoeg-ausbildungsfoerderung/` | Federal Training Assistance Act: student financial aid (BAföG) | 79 |

### Steuerrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **AO** – Abgabenordnung | `laws/ao-abgabenordnung/` | Fiscal Code: general tax procedure, tax assessment, deadlines, objections, tax evasion | 496 |
| **EStG** – Einkommensteuergesetz | `laws/estg-einkommensteuer/` | Income Tax Act: taxable income, deductions, tax classes, wage tax, capital gains | 235 |
| **KStG** – Körperschaftsteuergesetz | `laws/kstg-koerperschaftsteuer/` | Corporate Income Tax Act: taxation of corporations | 48 |
| **GewStG** – Gewerbesteuergesetz | `laws/gewstg-gewerbesteuer/` | Trade Tax Act: municipal trade tax on businesses | 41 |
| **UStG** – Umsatzsteuergesetz | `laws/ustg-umsatzsteuer/` | Value Added Tax Act: VAT rates, exemptions, invoices, small business rule | 88 |
| **ErbStG** – Erbschaftsteuer- und Schenkungsteuergesetz | `laws/erbstg-erbschaftsteuer/` | Inheritance and Gift Tax Act: tax on inheritances and gifts, allowances | 46 |
| **GrEStG** – Grunderwerbsteuergesetz | `laws/grestg-grunderwerbsteuer/` | Real Estate Transfer Tax Act: tax on buying real property | 27 |
| **FGO** – Finanzgerichtsordnung | `laws/fgo-finanzgerichtsordnung/` | Code of Procedure for Fiscal Courts: lawsuits against tax authorities | 172 |

### Verkehrsrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **StVG** – Straßenverkehrsgesetz | `laws/stvg-strassenverkehrsgesetz/` | Road Traffic Act: driving licences, liability of vehicle owners, points system, driving bans | 124 |
| **StVO** – Straßenverkehrs-Ordnung | `laws/stvo-strassenverkehrsordnung/` | Road Traffic Regulations: rules of the road, speed limits, signs, parking | 63 |
| **FeV** – Verordnung über die Zulassung von Personen zum Straßenverkehr | `laws/fev-fahrerlaubnis/` | Driving Licence Regulation: licence classes, probation, medical-psychological assessment (MPU) | 123 |

### Immobilienrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **GBO** – Grundbuchordnung | `laws/gbo-grundbuch/` | Land Register Code: land register entries, priority, procedure | 163 |
| **BeurkG** – Beurkundungsgesetz | `laws/beurkg-beurkundung/` | Notarisation Act: notarial deeds and procedure | 84 |

### Familien- und Personenrecht

| Law | Skill folder | Covers | §§ |
|-----|-------------|--------|----|
| **PStG** – Personenstandsgesetz | `laws/pstg-personenstand/` | Civil Status Act: birth, marriage and death registration | 83 |
| **LPartG** – Gesetz über die Eingetragene Lebenspartnerschaft | `laws/lpartg-lebenspartnerschaft/` | Civil Partnership Act: registered same-sex partnerships (pre-2017) | 24 |
| **VersAusglG** – Gesetz über den Versorgungsausgleich | `laws/versausglg-versorgungsausgleich/` | Pension Rights Adjustment Act: splitting pension rights on divorce | 55 |

