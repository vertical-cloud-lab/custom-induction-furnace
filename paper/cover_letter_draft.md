# Cover letter draft — Review of Scientific Instruments

Text only, per S. Baird's request (PR #12, 2026-07-29); the letterhead/template
will be supplied by the authors later. Bracketed items are placeholders for
the authors to fill in or confirm.

---

Dear Editor,

We are pleased to submit our manuscript, "Retrofitting a commercial RF induction generator into a computer-controlled, vacuum and gas integrated annealing system for reactive-metal grain growth," for consideration as a regular contributed article in *Review of Scientific Instruments*.

High-temperature vacuum annealing near a metal's melting point is essential for controlled grain-growth studies, but it is normally the province of expensive turn-key vacuum induction furnaces. Many laboratories own, or can affordably acquire, a bare commercial radiofrequency induction generator; what they lack is the surrounding layer of computer control, vacuum and gas handling, and optical temperature feedback that turns the generator into a scientific instrument. Our manuscript fills that gap with a fully documented, open retrofit. Because the retrofit's only interface requirement is a monotonic analog power-control input, it is agnostic to the generator's make and model; our reference build, based on a 6 kW solid-state generator, brings the entire system to about $38k.

The manuscript validates the instrument quantitatively: a power–temperature calibration linear to R² = 0.991 over 1200–1400 °C, eight independent 12 h nickel anneals that reproduced their soak temperature to 1201.2 ± 1.3 °C (a coefficient of variation of 0.11%), and stable closed-loop soaks up to 40 h. Two findings should be of particular interest to the journal's readership. First, nickel specimens annealed in this system produced high-quality electron-backscatter-diffraction (EBSD) patterns with zero specimen preparation — taken directly from the furnace chamber to the SEM, with no grinding, polishing, or etching — which we attribute to the system's high-purity annealing environment. Second, a modified sample assembly extends the same furnace to non-coupling ceramics: it coarsened yttria-stabilized zirconia grains in 45 min at 2500 °C, compared with 228 h at 1600 °C in a conventional box furnace.

In keeping with the instrument-building tradition of *Review of Scientific Instruments*, the work is fully reproducible: complete design files, an itemized bill of materials, the LabVIEW control software, and all underlying run data are openly available on GitHub (https://github.com/vertical-cloud-lab/custom-induction-furnace), with an archival snapshot deposited at Zenodo (https://doi.org/10.5281/zenodo.20878017). The supplementary material links the reported specimens to their raw furnace run logs.

[Optional, if posted before journal submission: A preprint of this manuscript has been posted to arXiv (arXiv:XXXX.XXXXX), consistent with AIP Publishing's preprint policy.]

[Related work by the authors, per the journal's cover-letter guidance — list any prior publications by the author group on grain growth, grain-boundary characterization, or instrument development, e.g., publications by O. Johnson's group that motivated the furnace.]

This manuscript is original, has not been published previously, and is not under consideration elsewhere. All authors have approved the submission and declare no conflicts of interest. This work was supported by the National Science Foundation under Grant No. 1610077.

Thank you for your consideration. We look forward to your response.

Sincerely,

[Corresponding author name]
on behalf of the authors: Sterling G. Baird, Ryan Weber, Christopher Nyborg, Ronnie Guymon, Gage Erickson, and Oliver Johnson
Department of Mechanical Engineering, Brigham Young University, Provo, Utah 84602, USA
[Email address]
[Date]
