# Cover letter draft — Review of Scientific Instruments

Text only, per S. Baird's request (PR #12, 2026-07-29); the letterhead/template
will be supplied by the authors later. Bracketed items are placeholders for
the authors to fill in or confirm.

Revised 2026-07-30 per S. Baird: leads with the two key results, plainer
language throughout; then revised again per Edison Scientific editorial
feedback (task b69eaa93, report in paper/cover_letter_query/) on flow,
conciseness, tone, readability, and accuracy against the manuscript.

Revised 2026-08-10 per R. Guymon against the AIP Publishing publication
criteria (originality; error-free; conclusions supported by data; clarity;
high impact within journal scope): added an explicit impact/scope-fit
paragraph, and aligned the originality statement with AIP's "not
copyrighted, submitted, published, or accepted elsewhere" wording. (The
page R. Guymon quoted is the AVS/JVST/Biointerphases author page; its
Peer X-Press portal and AVS Word template do NOT apply to RSI, but its
publication criteria and abstract guidance are AIP-general.)

Revised 2026-08-11 per S. Baird: added a suggested-reviewers section.
The five names are the consensus slate from three independent sweeps
(Edison analysis task 947fc0d9 over all 11,869 RSI articles 2015-2026,
Edison literature task 6ab94166 field-wide, and the in-repo Crossref
sweep in paper/reviewer_search/own_sweep_report.md). Emails verified
against institutional pages 2026-08-11. AUTHORS MUST CONFIRM the slate
(esp. no informal collaboration ties, and the Zaefferer/EBSD-community
caution re: O. K. Johnson) before submission — S. Baird asked to triage
this personally. A longer alternates list is in the PR discussion and
in paper/reviewer_search/.

Revised 2026-08-11 per R. Guymon: swapped H. Wang (ORNL, pyrometry
specialist) for L. Gallais (whole-annealing-system instrument builder) —
rationale: nothing novel was done with the pyrometer itself beyond
integrating it, so a reviewer who evaluates complete annealing systems
is a better fit than a single-instrument specialist. Also removed the
two bracketed optional paragraphs (arXiv preprint note; related-work
list, which was APL guidance, not RSI). Reviewer slate still awaits
S. Baird's confirmation before submission.

Revised 2026-08-11 per R. Guymon: Ronald Guymon set as corresponding
author (rguymon2@byu.edu), dated 2026-08-11 — provisional, to be swapped
if S. Baird prefers to be corresponding author. "Ronnie" changed to
"Ronald" in the author list here, in real_person_paper.tex (\author and
Author Contributions), and in SI.tex; a matching \email{} was added to
the Ronald Guymon \author block in real_person_paper.tex.

Revised 2026-08-11 per S. Baird ("Change me to corresponding author"):
corresponding author switched from R. Guymon to Sterling G. Baird, here
and in real_person_paper.tex (\email moved to the Baird \author block).
Email sgbaird@byu.edu is the address on record in this repo's Crossref
scripts — S. Baird to confirm it is the address he wants on the
submission.

---

Dear Editor,

We submit our manuscript, "Retrofitting a commercial RF induction generator into a computer-controlled, vacuum and gas integrated annealing system for reactive-metal grain growth," for consideration as a regular contributed article in *Review of Scientific Instruments*.

The manuscript reports two results that demonstrate the instrument's performance. First, nickel annealed in the furnace yielded high-quality electron backscatter diffraction (EBSD) patterns without grinding, polishing, or etching; the specimens were transferred directly from the furnace to the scanning electron microscope. The manuscript discusses how the near-solidus anneal, low-oxygen environment, and surface diffusion may contribute to this result. Second, changing the materials in the sample assembly extended the furnace to yttria-stabilized zirconia (YSZ), which does not couple directly to the radiofrequency field. The system coarsened YSZ grains from approximately 20 to 90 µm in 45 min at 2500 °C, compared with approximately 10 to 80 µm after 228 h at 1600 °C in a conventional box furnace.

These results were obtained with the open, documented retrofit described in the manuscript. Commercial turn-key vacuum induction furnaces capable of near-melting-point annealing under controlled atmospheres typically cost $50,000–$200,000 or more. Bare commercial radiofrequency induction generators are widely available but lack the computer control, vacuum and gas handling, and optical temperature feedback needed for this application. The retrofit adds these components. Because it requires only a monotonic analog power-control input, it can be transferred between generator makes and models, with recalibration for each configuration. The reference build uses a 6 kW solid-state generator and costs approximately $38,000.

The manuscript validates the instrument quantitatively. For a fixed configuration, the power–temperature calibration was approximately linear from 1200 to 1400 °C (R² = 0.991). Across eight separate 12 h nickel anneals, the mean hold temperature was 1201.2 ± 1.3 °C, corresponding to a 0.11% coefficient of variation; feedback-controlled holds remained stable for as long as 40 h.

The manuscript provides the files and data needed to reproduce the system and evaluate the reported runs. Design files, an itemized bill of materials, LabVIEW control software, and data supporting the findings are available on GitHub (https://github.com/vertical-cloud-lab/custom-induction-furnace), with an archival copy deposited at Zenodo (https://doi.org/10.5281/zenodo.20878017). The supplementary material links the reported specimens to their raw furnace logs, so the conclusions can be checked against the underlying data.

We believe the work falls squarely within the journal's scope and will be useful to its readership. It gives laboratories a documented, low-cost route to near-melting-point vacuum annealing using widely available induction generators, and the preparation-free EBSD result removes an entire metallographic step between annealing and characterization in grain-growth studies.

We respectfully suggest the following potential reviewers, whose published work spans the manuscript's main elements — furnace and instrument design, induction heating and closed-loop temperature control, optical pyrometry, EBSD, and ultra-high-temperature ceramic processing. None is affiliated with our institution, and to our knowledge none has collaborated with the author group.

- Prof. Dr. Florian Kargl, RWTH Aachen University and DLR Institute of Materials Physics in Space, Cologne, Germany (florian.kargl@dlr.de) — has published a sustained series of custom high-temperature furnace instruments in *Review of Scientific Instruments* (e.g., DOI 10.1063/5.0151523).
- Prof. Cheng-Chi Tai, Department of Electrical Engineering, National Cheng Kung University, Tainan, Taiwan (ctai@mail.ncku.edu.tw) — induction-heating systems with feedback temperature control (e.g., DOI 10.1063/5.0066308).
- Dr. Stefan Zaefferer, Max Planck Institute for Sustainable Materials, Düsseldorf, Germany (s.zaefferer@mpie.de) — EBSD instrumentation and methodology (e.g., DOI 10.1063/5.0087945).
- Prof. Jian Luo, Aiiso Yufeng Li Family Department of Chemical and Nano Engineering, University of California San Diego, USA (jluo@ucsd.edu) — rapid ultra-high-temperature ceramic processing and grain growth (e.g., DOI 10.1126/sciadv.abn8241).
- Prof. Laurent Gallais, Institut Fresnel, Centrale Méditerranée, Marseille, France (laurent.gallais@fresnel.fr) — has published a series of complete high-temperature annealing instruments with radiometric temperature control in *Review of Scientific Instruments* (e.g., DOI 10.1063/5.0202933).

This manuscript presents original findings that have not been published previously by the authors or others. It has not been copyrighted, submitted, published, or accepted for publication elsewhere. All authors have approved its submission and have no conflicts of interest to disclose.

Thank you for considering our manuscript.

Sincerely,

Sterling G. Baird
on behalf of the authors: Sterling G. Baird, Ryan Weber, Christopher Nyborg, Ronald Guymon, Gage Erickson, and Oliver Johnson
Department of Mechanical Engineering, Brigham Young University, Provo, Utah 84602, USA
sgbaird@byu.edu
August 11, 2026
