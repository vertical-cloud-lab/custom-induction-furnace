# Cover letter draft — Review of Scientific Instruments

Text only, per S. Baird's request (PR #12, 2026-07-29); the letterhead/template
will be supplied by the authors later. Bracketed items are placeholders for
the authors to fill in or confirm.

Revised 2026-07-30 per S. Baird: lead with the two key results, plainer
language throughout.

---

Dear Editor,

We are pleased to submit our manuscript, "Retrofitting a commercial RF induction generator into a computer-controlled, vacuum and gas integrated annealing system for reactive-metal grain growth," for consideration as a regular contributed article in *Review of Scientific Instruments*.

Two results should be of particular interest to your readers. First, nickel annealed in this furnace produced high-quality electron backscatter diffraction (EBSD) patterns with no specimen preparation at all: samples went straight from the furnace chamber into the electron microscope, with no grinding, polishing, or etching. We attribute this to the purity of the annealing environment. Second, a small change to the sample assembly extends the same furnace to ceramics, which do not couple to the induction field. It coarsened yttria-stabilized zirconia grains in 45 minutes at 2500 °C — a treatment that took 228 hours at 1600 °C in a conventional box furnace.

The instrument behind these results is a fully documented, open retrofit. Annealing a metal near its melting point without oxidizing it normally requires an expensive turn-key vacuum induction furnace. Many laboratories own, or can affordably buy, a bare commercial radiofrequency induction generator; what they lack is the computer control, vacuum and gas handling, and optical temperature feedback that turn it into a scientific instrument. Our manuscript supplies that missing layer. Because it needs only the generator's analog power-control input, the retrofit is independent of the generator's make and model; the reference build, on a 6 kW solid-state generator, brings the entire system to about $38k.

The manuscript validates the instrument quantitatively: a power–temperature calibration linear to R² = 0.991 over 1200–1400 °C, eight independent 12-hour nickel anneals that reproduced their soak temperature to 1201.2 ± 1.3 °C (a variation of 0.11%), and stable closed-loop soaks up to 40 hours.

The work is fully reproducible. Complete design files, an itemized bill of materials, the LabVIEW control software, and all underlying run data are openly available on GitHub (https://github.com/vertical-cloud-lab/custom-induction-furnace), with an archival copy deposited at Zenodo (https://doi.org/10.5281/zenodo.20878017). The supplementary material links the reported specimens to their raw furnace run logs.

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
