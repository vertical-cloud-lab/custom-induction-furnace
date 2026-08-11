# Consolidated reviewer candidates with verified contacts

**Compiled 2026-08-11** (PR #12, Claude) from three independent sweeps:

- `edison_analysis_reviewers_report.md` — Edison analysis task `947fc0d9`, full parse of all 11,869 RSI articles 2015–2026 (`rsi_all_articles_compact.tsv`).
- `edison_literature_reviewers_report.md` — Edison literature task `6ab94166`, field-wide (not RSI-restricted).
- `own_sweep_report.md` — in-repo Crossref keyword sweep + manual curation.

Emails/institutions verified 2026-08-11 against institutional directories,
staff profiles, or published corresponding-author records (source noted per
row). "Consensus" = named independently by ≥2 of the three sweeps.

## Slate placed in the cover letter (5)

| Name | Institution | Email (verified source) | Pillar | Consensus |
|---|---|---|---|---|
| Florian Kargl | RWTH Aachen / DLR Inst. of Materials Physics in Space, Cologne | florian.kargl@dlr.de (DLR staff page) | Furnace/instrument design, vacuum | Own + Edison-analysis (both rank him top) |
| Cheng-Chi Tai | National Cheng Kung Univ., EE, Taiwan | ctai@mail.ncku.edu.tw (NCKU directory) | Induction heating + feedback control | Own + Edison-analysis |
| Stefan Zaefferer | MPI for Sustainable Materials (MPIE), Düsseldorf | s.zaefferer@mpie.de (MPIE/guest-faculty pages) | EBSD | Own + Edison-analysis. COI check closed: R. Guymon searched and found no co-authored papers or joint projects with O. K. Johnson (PR #12, 2026-08-11) |
| Jian Luo | UC San Diego, Chemical and Nano Engineering | jluo@ucsd.edu (published corresponding-author) | Ultra-high-T ceramics / rapid sintering / YSZ pillar | Edison-literature (rank 4) |
| Hsin Wang | Oak Ridge National Laboratory | wangh2@ornl.gov (ORNL staff profile) | Pyrometry / IR thermometry | Edison-literature (rank 2) |

## Alternates with verified contacts (swap candidates)

| Name | Institution | Email (verified source) | Pillar | Named by |
|---|---|---|---|---|
| Laurent Gallais | Institut Fresnel / Centrale Méditerranée, Marseille | laurent.gallais@fresnel.fr (Fresnel/Scholar) | High-T annealing instruments + radiometric T control | All three sweeps |
| Ke An | ORNL (VULCAN) | kean@ornl.gov (ORNL profile) | High-T vacuum furnace practice, automation | Own + Edison-analysis |
| Stephen D. Wilson | UC Santa Barbara, Materials | stephendwilson@ucsb.edu (UCSB group page) | High-T apparatus / atmosphere integration | Edison-analysis (rank 5) |
| Gregory S. Rohrer | Carnegie Mellon, MSE | gr20@andrew.cmu.edu (CMU directory) | EBSD/grain-boundary stereology (Zaefferer substitute) | Edison-literature |
| Sylvain Marinel | CRISMAT, ENSICAEN/UNICAEN, Caen | sylvain.marinel@ensicaen.fr (CRISMAT annuaire) | Rapid sintering, susceptors, atmosphere furnaces | Edison-literature (rank 5) |
| Gopalan Jagadeesh | IISc Bangalore, Aerospace | jaggie@iisc.ac.in (IISc pages) | Ratio pyrometry in tube furnace (closest single-paper match) | Own + both Edison (stretch) |
| Yuzhong Zhang | Hefei Univ. of Technology, Precision Instrument lab | zhangyuzhong@hfut.edu.cn (published record) | Pyrometer calibration, emissivity | Edison-analysis (rank 3)¹ |
| A. K. (Ajay Kumar) Shukla | CSIR-National Physical Laboratory, New Delhi | likely ajayshukla@nplindia.org — **recheck before use** (inferred from NPL profile document name) | RF induction + vacuum/Ar automated furnace | Edison-literature (rank 1) |

¹ Name discrepancy to resolve: for the same four HFUT RSI pyrometry DOIs
(10.1063/1.5034233 etc.), `own_sweep_report.md` credited **Shuangbao Shu**
and the Edison analysis credited **Yuzhong Zhang** — both appear to be HFUT
coauthors on that series. Web check confirms Yuzhong Zhang is the HFUT
emissivity/pyrometry PI with the verified email above; confirm which is the
senior author before nominating.

## Deeper bench (no email lookup done; see the three reports)

Andreas Bauer / Christian Pfleiderer (TU München — closest UHV induction-furnace
hardware, older papers); Jérôme Mendonça (NewTec Scientific / ICSM Montpellier —
RSI microfurnace trilogy); G. Lohöfer (DLR — RF levitation); Ashkan Salamat
(UNLV); Saurabh Kabra (ORNL); Sébastien Weber (CNRS, PyMoDAQ — open-source DAQ
angle); António Araújo (multi-wavelength pyrometry — possibly cited in
manuscript, check); J. Madison (Sandia/Alabama group — Ni-200 abnormal grain
growth + EBSD); Kenneth Vecchio (UCSD — avoid together with Luo); Diletta
Sciti (CNR-ISTEC); Joshua Pearce (open hardware); Marco Minissale (CNRS PIIM);
Mattia Biesuz (Trento); Watkins/Trofimov (ORNL — avoid together with Wang);
Revel/Chiariotti/Giulietti (Italian emissivity-metrology cluster — pick one);
S. Jiménez (LIFTEC Zaragoza); Y. Pontillon (CEA); Sonja Steinbach /
C. Dreißigacker (DLR — overlap Kargl); Jennifer Niedziela, Dante Quirinale
(ORNL — substitutes for Ke An).

**Anti-clustering rules** (from the Edison reports): pick at most one of
{Wang, Watkins, Trofimov}, {Luo, Vecchio}, {Marinel, Biesuz}, {Gallais,
Minissale, Pontillon}, {Kargl, Dreißigacker, Steinbach}, {Bauer, Pfleiderer},
{Revel, Chiariotti, Giulietti}.

**COI screens applied** in all three sweeps: no BYU affiliation; no coauthorship
found with any manuscript author; Baird's U. Utah / Toronto Acceleration
Consortium ties checked. These are negative screens on public records only —
authors must still confirm informal/unpublished ties before nominating.
