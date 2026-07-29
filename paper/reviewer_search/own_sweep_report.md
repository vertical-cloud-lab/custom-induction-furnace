# Reviewer candidates from an independent sweep of RSI authors (2015–2026)

**Session:** PR #12, 2026-07-29 (Claude). Companion to the two Edison
Scientific queries in this directory (`edison_analysis_task_id.txt`,
`edison_literature_task_id.txt`).

## Method

1. `fetch_rsi_authors_corpus.py` pulled every *Review of Scientific
   Instruments* journal article indexed by Crossref with a publication date
   from 2015-01-01 to 2026-07-29: **11,869 articles**, with title, abstract
   (where deposited), year, DOI, and full author lists (affiliations where
   Crossref carries them — sparse before ~2019).
2. `rank_rsi_authors.py` scored every article against 23 weighted keyword
   patterns drawn from the manuscript's pillars (induction heating,
   susceptor/crucible, pyrometry/emissivity, furnace/annealing, vacuum,
   grain growth/EBSD/Kikuchi, zirconia, temperature control, open
   hardware/LabVIEW, retrofit). **351 articles** scored ≥ 8 ("relevant");
   **2,305 authors** appear on them and were ranked by aggregate score with
   a mild recency boost.
3. Manual curation: I read the top ~40 relevant articles and the per-author
   records of every high-ranking name, plus targeted sweeps of the full
   corpus for themes the keyword screen underweights (levitation/
   containerless processing: 54 hits; in-situ heating stages: 4; open-source
   instruments: 19), then applied judgment about seniority, current
   activity, and independence.

**COI screen applied:** manuscript authors are all BYU Mechanical
Engineering (S. G. Baird, R. Weber, C. Nyborg, R. Guymon, G. Erickson,
O. K. Johnson). No candidate below is at BYU or is a known coauthor of any
of them; Baird's prior affiliations (U. Utah, U. Toronto Acceleration
Consortium) were also avoided. Caveat: Crossref-only disambiguation — the
authors should confirm no direct coauthorship/collaboration before
nominating anyone, especially within the grain-boundary community, where
O. K. Johnson has many collaborative ties.

## Primary candidates (10)

| # | Name | Likely institution | Fit (pillars) | Supporting RSI record |
|---|------|--------------------|---------------|----------------------|
| 1 | **Christian Pfleiderer** (with Andreas Bauer) | TU München, Physics | Induction heating + UHV furnace design | Ultra-high-vacuum *induction-heated* rod casting furnace, 2016, 10.1063/1.4954926; UHV intermetallic preparation chain, 2016, 10.1063/1.4967011. The closest single match in 11 years of RSI: RF induction heating into a custom vacuum chamber for metal processing. |
| 2 | **Florian Kargl** | DLR Institute of Materials Physics in Space, Cologne | Furnace design, in-situ metal processing | Five RSI furnace papers 2015–2023: 10.1063/1.4922359, 10.1063/1.5124548, 10.1063/5.0004356, 10.1063/5.0037398, 10.1063/5.0151523 (isothermal, gradient, and gas-loading furnaces with in-situ X-radiography). Top aggregate score of the whole sweep. |
| 3 | **Stefan Zaefferer** | MPI für Eisenforschung, Düsseldorf | EBSD, microstructure | Fully automated large-scale EBSD system, 2022, 10.1063/5.0087945. A leading EBSD authority who also publishes instrumentation in RSI — ideal for the no-prep EBSD claims. *Authors should verify no collaboration link to O. K. Johnson within the EBSD/GB community.* |
| 4 | **Laurent Gallais** | Institut Fresnel / Centrale Méditerranée, Marseille | High-temperature annealing systems + optical thermometry | Four RSI papers 2018–2025 on laser-based high-temperature heating/annealing platforms with radiometric temperature control: 10.1063/1.4996611, 10.1063/1.5133741, 10.1063/5.0139508, 10.1063/5.0202933 (the 2025 one is an annealing methodology for restoration-mechanism studies — close in spirit to accelerated grain-growth workflows). |
| 5 | **Gopalan Jagadeesh** (with Sneh Deep) | IISc Bangalore, Aerospace | Ratio pyrometry in furnaces | Broadband two-color ratio pyrometry inside a tube furnace, 2019, 10.1063/1.5088149 — the single highest-scoring article in the sweep; directly about pyrometer temperature fidelity in a furnace. Senior. |
| 6 | **Ke An** | Oak Ridge National Laboratory (VULCAN) | High-temperature vacuum furnace practice | Automated rapid cooling of high-temperature vacuum furnaces, 2026, 10.1063/5.0299443; electrostatic levitation facility, 2016, 10.1063/1.4939194. Senior instrument scientist; evaluates exactly the vacuum-furnace engineering in Secs. II–III. |
| 7 | **Cheng-Chi Tai** | National Cheng Kung University, Taiwan | Induction-heating systems + closed-loop temperature control | Three RSI induction-heating papers with feedback temperature controllers, 2017–2022: 10.1063/1.4992021, 10.1063/5.0006019, 10.1063/5.0066308. Covers the PID-on-induction-power control loop. |
| 8 | **Shuangbao Shu** | Hefei University of Technology | Pyrometer calibration, emissivity | Four RSI papers 2018–2022 on CCD-based pyrometers, noise/calibration, and spectral emissivity: 10.1063/1.5034233, 10.1063/1.5129758, 10.1063/5.0046410, 10.1063/5.0101504. |
| 9 | **Tairan Fu** | Tsinghua University | Multispectral/imaging pyrometry | VIS–NIR multispectral imaging pyrometer, 2017, 10.1063/1.4985170; high-temperature measurement method, 2020, 10.1063/5.0004126. Senior radiation-thermometry figure publishing in RSI. |
| 10 | **Marco Minissale** | CNRS PIIM, Aix-Marseille | High-power heating facilities, emissivity | 10.1063/1.5133741 (2020) and 10.1063/5.0202933 (2025). Mid-career; complements Gallais (same consortium — nominate one of the two, not both). |

**Pillar coverage:** instrument/furnace design (1, 2, 6, 7), induction
heating specifically (1, 7), pyrometry/emissivity (4, 5, 8, 9, 10),
vacuum/atmosphere practice (1, 2, 6), grain growth/EBSD (3, 4-adjacent).
The RSI author pool is thin on ceramic (YSZ) grain-growth kinetics — that
pillar is better served by the Edison literature query's field-wide sweep
(e.g., the Tekeli/Matsui lineage already cited in the manuscript).

## Alternates

- **Sonja Steinbach / Christoph Dreißigacker** (DLR Cologne) — furnace
  modules for directional solidification (10.1063/1.5124822 and three
  others); overlaps Kargl's group, so use as substitutes for #2.
- **Yves Pontillon** (CEA Cadarache) — high-temperature annealing test
  facilities (10.1063/1.5133741, 10.1063/5.0139508); nuclear-fuel focus.
- **Jennifer Niedziela** (ORNL) — vacuum furnace design for neutron
  scattering, 2017, 10.1063/1.5007089; substitute for #6.
- **Dante Quirinale** (ORNL) — levitation + high-temperature vacuum
  furnaces (10.1063/1.4939194, 10.1063/5.0299443); early/mid-career.
- **Andreas Neuber's group** (Texas Tech; T. M. Watson et al.) — nanosecond
  two-color pyrometry of electron-beam-heated metal, 2025,
  10.1063/5.0215582; pyrometry substitute.
- **Santiago Jiménez** — two-color two-dimensional pyrometers >1000 °C,
  2020, 10.1063/5.0021784 (institution uncertain from Crossref — verify).

## Limitations

- Crossref author records have no ORCIDs in this select-set and sparse
  affiliations before ~2019; names were disambiguated manually.
- Keyword scoring favors titles/abstracts that use our vocabulary; the
  targeted theme sweeps partially compensate, but instrument builders who
  describe their furnaces in application-domain language may be missed.
- Current institutions are my best assessment, not verified against 2026
  rosters; the submission form should use verified emails/affiliations.
