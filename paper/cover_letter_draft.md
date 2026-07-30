# Cover letter draft — Review of Scientific Instruments

Text only, per S. Baird's request (PR #12, 2026-07-29); the letterhead/template
will be supplied by the authors later. Bracketed items are placeholders for
the authors to fill in or confirm.

Revised 2026-07-30 per S. Baird: leads with the two key results, plainer
language throughout; then revised again per Edison Scientific editorial
feedback (task b69eaa93, report in paper/cover_letter_query/) on flow,
conciseness, tone, readability, and accuracy against the manuscript.

---

Dear Editor,

We submit our manuscript, "Retrofitting a commercial RF induction generator into a computer-controlled, vacuum and gas integrated annealing system for reactive-metal grain growth," for consideration as a regular contributed article in *Review of Scientific Instruments*.

The manuscript reports two results that demonstrate the instrument's performance. First, nickel annealed in the furnace yielded high-quality electron backscatter diffraction (EBSD) patterns without grinding, polishing, or etching; the specimens were transferred directly from the furnace to the scanning electron microscope. The manuscript discusses how the near-solidus anneal, low-oxygen environment, and surface diffusion may contribute to this result. Second, changing the materials in the sample assembly extended the furnace to yttria-stabilized zirconia (YSZ), which does not couple directly to the radiofrequency field. The system coarsened YSZ grains from approximately 20 to 90 µm in 45 min at 2500 °C, compared with approximately 10 to 80 µm after 228 h at 1600 °C in a conventional box furnace.

These results were obtained with the open, documented retrofit described in the manuscript. Commercial turn-key vacuum induction furnaces capable of near-melting-point annealing under controlled atmospheres typically cost $50,000–$200,000 or more. Bare commercial radiofrequency induction generators are widely available but lack the computer control, vacuum and gas handling, and optical temperature feedback needed for this application. The retrofit adds these components. Because it requires only a monotonic analog power-control input, it can be transferred between generator makes and models, with recalibration for each configuration. The reference build uses a 6 kW solid-state generator and costs approximately $38,000.

The manuscript validates the instrument quantitatively. For a fixed configuration, the power–temperature calibration was approximately linear from 1200 to 1400 °C (R² = 0.991). Across eight separate 12 h nickel anneals, the mean hold temperature was 1201.2 ± 1.3 °C, corresponding to a 0.11% coefficient of variation; feedback-controlled holds remained stable for as long as 40 h.

The manuscript provides the files and data needed to reproduce the system and evaluate the reported runs. Design files, an itemized bill of materials, LabVIEW control software, and data supporting the findings are available on GitHub (https://github.com/vertical-cloud-lab/custom-induction-furnace), with an archival copy deposited at Zenodo (https://doi.org/10.5281/zenodo.20878017). The supplementary material links each reported specimen to its raw furnace log.

[Optional, if posted before journal submission: A preprint of this manuscript has been posted to arXiv (arXiv:XXXX.XXXXX), consistent with AIP Publishing's preprint policy.]

[Optional, only if genuinely helpful for assessing novelty: one or two directly related prior publications by the author group. Edison's convention check found the "list related work" cover-letter guidance applies to Applied Physics Letters, not RSI, so this can simply be cut.]

This manuscript is original, has not been published previously, and is not under consideration elsewhere. All authors have approved its submission and have no conflicts of interest to disclose.

Thank you for considering our manuscript.

Sincerely,

[Corresponding author name]
on behalf of the authors: Sterling G. Baird, Ryan Weber, Christopher Nyborg, Ronnie Guymon, Gage Erickson, and Oliver Johnson
Department of Mechanical Engineering, Brigham Young University, Provo, Utah 84602, USA
[Email address]
[Date]
