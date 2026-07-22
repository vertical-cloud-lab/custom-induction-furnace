# Repository agent guide

This file captures durable, **throughout-the-document** conventions for the journal
manuscript in `paper/` (and related artifacts), distilled from PR review feedback.
The manuscript targets **Review of Scientific Instruments (RSI)** as of 2026-07-02
(REVTeX 4.2, `aip,rsi`); it was previously drafted for HardwareX, and that version
is archived in `paper/archive/`.
When a reviewer flags something "that applies throughout" and points at one example,
the rule is recorded here so it is applied consistently and recognized in future
sessions. See also `.github/copilot-instructions.md` for tooling/environment notes.

## Manuscript authoring conventions (`paper/paper.tex`)

These apply to the **whole manuscript**, not just the line a reviewer happened to mark.

1. **Write to the reader, not to "us" as the authors.** Address the potential reader
   who will reproduce the build. Avoid first-person lab narration where it should be
   reader-facing instruction.
   - Bad: "the VI we wrote emails *us* status alerts."
   - Good: "the VI can email status alerts."

2. **Use actual figures wherever they exist.** Prefer real figures (rendered
   schematics, hardware photos, software screenshots) over prose placeholders. Source
   schematics live as editable PowerPoint in `docs/` (e.g.
   `docs/induction-furnace-schematic.pptx`) and are rendered by
   `paper/build_schematic_figures.py`; real screenshots/photos live under `docs/`
   (e.g. `docs/equipment-reference/frontPanel_200219.PNG`). Only when no real figure
   exists, use a proper `figure` environment placeholder **with a real, descriptive
   caption** (not a bare "planned" sentence). This applies throughout.

3. **Remove BYU-/facility-specific detail unhelpful to a general reader.** Strip
   hyperspecific local details that a reader cannot use.
   - Removed example: "Open the facility cooling-water valve (~45°, half open)" →
     "Check for leaks and confirm flow before applying RF power."
   - Legitimate exceptions: author affiliation, acknowledgements, and brief historical
     origin context.

4. **Anchor the reproducible design + BOM on the current USA induction heater.** The
   reproducible build is the CEIA "Power Cube" (model PW3-90/50) + Power Controller
   C-V3 Plus, procured through East Coast Induction (quote `210203AP`, in
   `docs/quotes/EastCoastInduction-CEIA.docx`). The ~1970 LEPEL furnace is the
   *originating prototype* and the rejected CYSI/GP-15A import is documented only as
   historical context — neither is a BOM line item.

5. **Follow the AIP/RSI manuscript structure, not HardwareX's.** RSI has no
   mandatory specifications table or design-files/BOM sections; the bill of
   materials and design-file inventory live in **appendices**, and the required
   AIP order is: title → abstract (≤250 words, one paragraph) → text (ending in a
   Conclusions section) → Supplementary Material → Acknowledgments → Author
   Declarations (Conflict of Interest, Ethics, CRediT Author Contributions) →
   Data Availability → appendices → references. Build-dependent values (vacuum
   level, temperatures, coil geometry) belong in the "Technical specifications"
   table in the System design section. See `paper/template/rsi/RSI_GUIDE_FOR_AUTHORS.md`.

6. **Use the minted Zenodo DOI for the archival deposit; keep the GitHub link too.**
   Wherever a permanent DOI is required (Data availability, Supplementary material),
   use `https://doi.org/10.5281/zenodo.20878017`, and keep the development repository
   link `https://github.com/vertical-cloud-lab/custom-induction-furnace` in
   appropriate places. A bare GitHub URL is not an acceptable archival location.

7. **Mark used/eBay-sourced BOM items as "used" with an approximate/estimated cost,
   and prefer verifiable part numbers.** For items bought used (eBay, surplus), label
   them "used" and give an estimated cost (re-check a current listing, or fall back to
   the recorded quote price), e.g. the LumaSense ISR 6 pyrometer was $241 used vs.
   ~$5,500 new list (quote `00161403`). Prefer catalog part numbers where they exist
   (e.g. McMaster-Carr `1357T12` for the 2"×1/16" ultra-high-temperature quartz disc;
   McMaster stocks only imperial sizes, so the 55 mm metric disc is a custom-cut part
   with a vendor not recorded in the parts list).

8. **Match the prose-first style of published RSI articles.** RSI apparatus
   papers describe construction with labeled schematics/photographs plus prose
   explaining how the parts are connected --- not numbered step-by-step build
   recipes or checklists --- and they use tables sparingly, only to relay data
   (specifications, per-run results, inventories). Rhetorical or comparative
   content (prior art, hazards/mitigations, migration history) belongs in prose,
   not tables. (Requested by R. Guymon in PR #3, 2026-07-06, after comparing the
   draft against recent RSI publications, e.g.
   https://pubs.aip.org/aip/rsi/article/97/6/063303/3394533.)

9. **At most one data table in the main text; no BOM or specs tables.** The
   exemplar RSI publication R. Guymon provided (Rev. Sci. Instrum. 97, 063303
   (2026), doi:10.1063/5.0299443) has exactly one table, presented while
   discussing the data, and no bill-of-materials table. The manuscript
   currently has **zero** main-text tables: the specimen ↔ thermal-history
   linkage moved to `paper/supplementary/specimen-run-linkage.md` (Table S1)
   per S. Baird's PDF annotations (PR #3, 2026-07-07). Technical
   specifications are prose in the System design
   section; the itemized bill of materials and design-file inventory live in
   `paper/supplementary/bill-of-materials.md` and
   `paper/supplementary/design-file-inventory.md` (referenced from the
   Supplementary Material section), NOT as manuscript appendices. Outstanding
   BOM corrections are tracked in the supplementary BOM file. (Requested by
   R. Guymon in PR #3, 2026-07-06.)

10. **No rhetorical bolding in the manuscript body.** `\textbf{}` is not used
    for emphasis in prose (S. Baird: "There's way too much bolded text here").
    Bold remains only in the CRediT author-contribution names and the
    draft-only status box. Use plain prose (or sparing `\emph{}`).

11. **No bullet or numbered lists in the manuscript body.** S. Baird: "All of
    these numbered lists are distracting and look weird" / "Stop with all the
    bullet points." Subsystem descriptions, audience statements, portability
    criteria, etc. are written as flowing prose paragraphs.

12. **No run-ID (`IFrunNNN`) level detail in the main text or figures.**
    S. Baird: run/specimen-ID-level detail "could be supporting information as
    long as the raw data is made available or hyperlinked." Run IDs live only
    in `paper/supplementary/specimen-run-linkage.md` (Table S1), whose rows
    hyperlink to the raw logs; the manuscript references that cross-reference.
    Specific specimen IDs (`Ni4N5_###`) are likewise not named in the main
    text or captions — write "a Ni4N5 specimen" and let Table S1 carry the
    IDs (R. Guymon, PR #3, 2026-07-08). Figure builders label
    plots by nominal condition / chronological run number, not run ID.

13. **The mass flow controller is optional equipment.** Everywhere the MFC is
    mentioned, describe it as optional; the manuscript wording is "helpful
    when continuous inert gas flow is required" (R. Guymon's PDF edit,
    2026-07-13, replacing the earlier "a regulator and needle valve
    suffice"); the MFC photo panel was removed from the vacuum-details
    figure. (S. Baird, PR #3, 2026-07-07.)

14. **Do not reinsert the LabVIEW front-panel screenshot as a figure.** The
    archived screenshot (`fig_control_panel.png` /
    `docs/equipment-reference/frontPanel_200219.PNG`) shows the old LEPEL-era
    interface; the original LabVIEW files were lost and no current-interface
    screenshot exists. The front panel is described in prose only.
    (S. Baird, PR #3, 2026-07-07.)

15. **Clean vs. draft PDFs.** `make pdf` builds the clean `paper.pdf` (no
    status box, no red \todo markers — the shareable version); `make draft`
    builds `paper-draft.pdf` with the notes rendered (`\DRAFTNOTES` toggle in
    the preamble). Keep both in sync when editing. (S. Baird, PR #3,
    2026-07-07.)

16. **Kevin Cole is acknowledged, not an author.** (S. Baird, PR #3,
    2026-07-06/07-07.) The LEPEL prototype is historical context and is not
    mentioned in the abstract.

17. **Never fabricate a reference.** Only cite entries already present in
    `paper/references.bib`, which is compiled and validated from the Edison
    literature-query artifacts in `literature-search/`. (S. Baird, PR #3,
    2026-07-07.)

18. **The paper must be 5 pages or less — and those 5 pages should be
    full.** (R. Guymon, PR #3, 2026-07-08, citing the AIP author
    instructions; and 2026-07-16: "make additions so all 5 pages of our
    page limit are filled with relevant information.") The main text
    carries eleven figures: system overview v2, assembled-furnace photo,
    disassembled-crucible photo, crucible loading sequence,
    vacuum/gas-handling photos, the raw Kikuchi pattern, the EBSD IPF maps
    (panel titles carry anneal conditions only, no specimen IDs), the
    thermal-grooving panel, the Ni4N5 microstructure panel, the
    as-recorded YSZ 2500 °C/45 min micrograph, and the YSZ charge-stack
    schematic. The disassembled-crucible, vacuum-details, EBSD, and
    YSZ-stack figures were promoted from the SI on 2026-07-16 to fill the
    page budget and were removed from the SI at the same time (a figure
    lives in the main text or the SI, never both); the SI now carries
    Figs. S1–S9. When adding content, keep body content within five
    pages' worth and fill the pages — move material between main text and
    SI rather than leaving page 5 half-empty or exceeding the limit.

19. **No LEPEL mentions anywhere in the manuscript.** (R. Guymon, PR #3,
    2026-07-08: "do not include anything about the LEPEL furnace, it is not
    necessary.") Generator portability may be stated as "the layer has been
    ported between two generators of very different designs" without naming
    or dating the prototype. This supersedes the earlier "brief historical
    origin context" allowance for LEPEL.

20. **No dates in the manuscript body** (no years like "prototyped in 2019",
    "quoted in 2021", "~1970"). `\date{\today}` on the title page is the
    only exception. (R. Guymon, PR #3, 2026-07-08.)

21. **No specific equipment model or brand names in the manuscript** — for
    now, per R. Guymon (PR #3, 2026-07-08). Use generic descriptions ("a
    6 kW solid-state induction generator", "a compact turbo pumping
    station", "a dual-wavelength ratio pyrometer, 800–2500 °C sensing
    range", "3000 °C-grade graphite stock"). Exact models/prices live only
    in `paper/supplementary/bill-of-materials.md`. Standards (KF40),
    material grades (Ni200, Ni4N5, YSZ), and the LabVIEW/DAQ software stack
    are not "models" and stay. The v2 schematic likewise says "Turbo
    Pumping Station", not "T-Station 85".

22. **Graphite is not "exclusively for metals" — susceptor choice for
    ceramics is chemical compatibility found by trial and error.**
    (Updated by R. Guymon, PR #3, 2026-07-15, after C. Nyborg's
    Extension-to-ceramics text; supersedes the strict-separation rule of
    2026-07-08.) The graphite crucible *primarily* serves the metal
    grain-growth charges, but graphite also works as a susceptor for some
    ceramic charges when the contact chemistry permits — "it really just
    takes trial and error to find what works." Do not write "used
    exclusively for metal grain growth", "ceramic charges are never loaded
    into it", or "entirely separate tantalum-susceptor stack". The
    demonstrated 2500 °C / 45 min YSZ result did use the tantalum-susceptor
    stack, so keep that attribution in the grain-growth figure caption. The
    manuscript's ceramic temperature claims are aligned to the demonstrated
    2500 °C (abstract, Sec. II working-range sentence, Conclusions) — the
    older "2000–2350 °C" / "beyond 2300 °C" phrasings are stale; do not
    reintroduce them.

23. **Keep the Supplementary Material section and the Sec. III safety prose
    short.** The hazard-by-hazard enumeration was removed, and the
    off-normal-conditions sentence (zero the command, remove RF power, lock
    out) was subsequently removed as well — Sec. III now ends at the
    run/shutdown description and contains no dedicated safety sentence; do
    not add safety prose back. The "Operationally, before RF power is
    applied…" preflight sentence (high vacuum/backfill, cooling water,
    sight line, conductive objects 6–12 in) was also removed by R. Guymon's
    PDF edit (2026-07-13) — do not reintroduce it. The dedicated
    "Supplementary Material" section was removed entirely by R. Guymon's PDF
    edit (2026-07-14) — do not reintroduce it; the in-text pointers to "the
    supplementary material" and the Data Availability section remain.
    (R. Guymon, PR #3, 2026-07-08.)

24. **Never self-generate a data figure for the main text — use the lab's
    actual uploaded graphs/datasets, verbatim.** (R. Guymon, PR #3,
    2026-07-08: "Don't generate your own figures … Fig 5 should be replaced
    with one of the actual graphs/datasets either I or Sterling Baird
    uploaded.") The synthesized YSZ grain-growth dumbbell chart was replaced
    by the as-recorded 2500 °C/45 min YSZ micrograph extracted verbatim from
    p. 14 of `Grain Growth Summary.pdf` (repo root, S. Baird's upload), and
    the raw Kikuchi pattern R. Guymon selected
    (`raw-kikuchi-patterns/191026_Ni_003b1a/reg1a/reg1a_x4100y1628.jpg`,
    panel (c) of the earlier five-panel survey figure; PR #3, 2026-07-09)
    is included byte-for-byte.
    `paper/extract_uploaded_figures.py` (in `make figures`) only extracts or
    copies these records — it draws nothing. Other real uploaded records to
    draw on: `RyanWeber.pdf` (poster), `Grain Growth Summary.pdf` heating
    profiles, `docs/YSZ/Tantalum-Heat-Curve.xlsx`,
    `docs/SEM/raw-kikuchi-patterns/`.

25. **Do not state the "runs longer than 3 h contaminated the specimen"
    claim as a general rule.** The parenthetical on slide 2 of
    `docs/YSZ/Induction-Furnace-Key-Takeaways.pdf` ("90 um clean samples
    achieved with setup #3 after 45 min. Anything longer than 3hrs
    contaminated sample") is scoped to the surveyed YSZ susceptor/crucible
    contact configurations, and R. Guymon flagged the generalized "soaks
    past ~3 h contaminate" phrasing as contradicting other observations
    (PR #3, 2026-07-08). The manuscript states only that the extended-soak
    survey runs gave the contact reactions time to act while the 45 min
    anneal stayed clean, without a numeric duration rule. The "two practical
    rules" sentence was subsequently removed from Sec. V A entirely; do not
    reintroduce rule-style guidance there — the survey outcomes speak for
    themselves and the chemistry-as-constraint lesson lives in the
    Conclusions. (R. Guymon, PR #3, 2026-07-09.)

27. **Do not state that annealed nickel went "straight from the furnace into
    the microscope" (or similar no-preparation claims) as a general
    workflow.** That was a detail specific to one instance, not the standard
    practice. (R. Guymon, PR #3, 2026-07-09.)

28. **Prefer short declarative sentences over em-dash/semicolon splices.**
    R. Guymon's PDF edits (2026-07-13) systematically split "… — …" and
    "…; …" constructions into separate sentences (e.g. "…bill of
    materials. This is a small fraction…", "…mapping. Even at the coarse…",
    "…extreme temperature. Every failure mode…"). Follow that style in new
    prose.

29. **The Introduction carries no licensing sentence.** The "All design
    files … openly available … CERN-OHL-S v2 / MIT (proposed)" sentence was
    deleted by R. Guymon's PDF edit (2026-07-13, resolving his earlier RG1
    annotation); availability is covered by the back-matter Data
    Availability section only. The "already demonstrated by moving the
    layer between two generators of very different designs" clause was
    likewise removed — portability is stated without that claim.

30. **The "Extension to ceramic charges: YSZ" subsection is R. Guymon's
    verbatim replacement text (2026-07-14).** The whole subsection prose was
    replaced wholesale at his request; do not rewrite it. Its content: the
    furnace processes refractory ceramics by modifying only the materials in
    direct specimen contact (generator, vacuum system, pyrometer, cooling
    system, and control software unchanged); non-coupling materials need a
    susceptor, selected primarily for chemical compatibility with the
    specimen and support materials rather than RF heating performance;
    graphite and tantalum both serve as susceptors; grain growth follows
    Arrhenius kinetics, so for the 8 mol% YSZ specimens growth from ~10 to
    90 µm took 228 h at 1600 °C in a conventional box furnace vs. 45 min at
    2500 °C in the induction furnace; graphite–alumina contact is avoided
    because of a eutectic reaction lowering the interface melting point to
    ~1800 °C (solved with a boron nitride diffusion barrier, or by replacing
    graphite with tantalum). The earlier survey-outcome sentences (2500 °C/
    3.5 h Ta contamination, 2000 °C/168 h carbon consumption, 2130 °C/80.4 h
    Ta–BN shell, "2500 °C reliably reached", coil-overheating ceiling) are no
    longer in the manuscript — the Conclusions still carry the
    chemistry-as-constraint lesson. The only additions to the verbatim text
    are the LaTeX figure callout "(Fig.~\ref{fig:graingrowth})" and dropping
    a stray asterisk after "cooling system".

31. **Define repeated jargon at first use with a brief reader-facing gloss.**
    (R. Guymon, PR #3, 2026-07-16.) Terms the paper repeats that a general
    reader may not know — e.g. "soak" — get a compact parenthetical
    definition the first time they appear, and are used bare afterwards.
    Demonstrated in the abstract: "reproduced their soak temperature (the
    constant temperature held for the duration of the anneal)". Treated so
    far (R. Guymon, PR #3, 2026-07-16): "soak" (abstract gloss above, plus
    "(constant-temperature holds)" at first body use), "susceptor" (abstract
    parenthetical, plus a one-sentence definition at first body use in the
    Introduction — the YSZ subsection's own susceptor sentence is part of the
    protected verbatim text of convention 30 and stays), and each distinct
    sense of "stack": the modernization stack (abstract + Introduction), the
    charge stack (abstract + Introduction), and the chamber stack (Sec. II).
    The abstract must stand alone, so a term glossed there is glossed again
    at its first body use.

32. **Define abbreviations at first use — in the abstract and again in the
    body.** (R. Guymon, PR #3, 2026-07-16: "make sure to define
    abbreviations, such as RF, PID, and DAQ.") Defined: radio-frequency
    (RF), data-acquisition (DAQ) device, proportional--integral--derivative
    (PID), scanning electron microscopy (SEM), electron backscatter
    diffraction (EBSD), yttria-stabilized zirconia (YSZ), virtual
    instruments (VIs), standard cubic centimeters per minute (SCCM),
    palladium (Pd); KF40 gets a gloss ("a standard clamp-sealed vacuum
    flange") since the expansion (Klein Flansch) would not help a reader.
    The title keeps "RF" unexpanded per common RSI usage. Material grade
    designations (Ni200, Ni4N5, 8 mol% YSZ) are not abbreviations to
    expand.

26. **Do not describe the data as "archived" or write meta-information about
    the data — present the data itself and expound on it.** (R. Guymon,
    PR #3, 2026-07-08.) The reader is someone learning how the furnace
    retrofit works and understanding the Ni/YSZ grain-growth results, not
    the researcher who produced the record. Banned patterns: "the archive
    contains…", "retrospective operating record", dataset counts
    (specimen/file/pattern tallies), cross-reference script mechanics, and
    methodology caveats like the "where as-received baselines are
    unavailable…" sentence (explicitly removed). A single short pointer to
    the supplementary material for raw-log linkage is fine.

## Physical-configuration facts (from lab feedback)

- **The vacuum chamber has no support stand.** The chamber stack is joined by KF40
  flanges to the pyrometer housing, which is suspended from the ceiling by cables —
  the vertical stack hangs from above. The bolted support stand (8 short + 4 long
  sections, 12 corner braces, 4 floor mounts) carries the generator's **heating
  head/work coil**, not the chamber. Any text, caption, or schematic implying a
  stand-supported chamber or a "stand-mounted pyrometer holder" is wrong.
  (R. Guymon, PR #3, 2026-07-07.)
- **Three ceiling cables physically; draw two.** The pyrometer housing hangs from
  **three** cables to the ceiling. In the v2 overview schematic, however, only two
  are drawn — the third attachment sits behind the pyrometer in the flat side view
  and an angled third line read poorly, so it is deliberately omitted for clarity.
  Do not "fix" the schematic back to three. (R. Guymon, PR #3, 2026-07-07.)
- **The coolant is ethylene glycol, not water** (R. Guymon, PR #3, 2026-07-13).
  Do not write "cooling water" (or "water-cooled" where the coolant is named) in
  the manuscript, captions, or schematic labels — the manuscript says "ethylene
  glycol coolant" / "liquid-cooled", and the v2 schematic's loop label reads
  "Ethylene Glycol Coolant" with the chiller box labeled "Recirculating
  Chiller". The coolant runs in a series loop: chiller → generator → heating
  head/work coil → back to the chiller. (Order verified by R. Guymon, PR #3,
  2026-07-08; this corrects the head-first order stated on 2026-07-07.)
- **Why sapphire for the crucible-lid window:** "Sapphire is used for the
  window to increase transmittance in the wavelength ranges emitted from the
  sample relative to the pyrometry" (R. Guymon's PDF edit, 2026-07-14, added
  verbatim to the graphite-crucible section).
- **The crucible rests on an alumina support rod** inside the quartz-tube vacuum
  chamber, which positions it at coil height (both the graphite/metal and the
  tantalum/ceramic stacks). (R. Guymon, PR #3, 2026-07-08.)
- **The ceramic part under the Ta/YSZ/Ta sandwich is a heat-dissipation stub,
  not a crucible.** It is a solid stub whose job is to dissipate heat; it is
  boron nitride for best results (sometimes MgO). Never call it an "MgO
  crucible" (or any crucible) in text, captions, or schematics — the YSZ stack
  schematic draws it as a solid block labeled "BN Heat-Dissipation Stub".
  (R. Guymon, PR #3, 2026-07-10.) In the manuscript prose R. Guymon's
  2026-07-13 tracked change words it as "a boron nitride ceramic stand which
  sits on an alumina support rod".
- **Ceiling cables are drawn short.** In the v2 overview schematic the ceiling
  bar sits just above the pyrometer and the two cables are short stubs — the
  full-height run wasted figure space (R. Guymon, PR #3, 2026-07-08). The
  schematic renders are auto-cropped to content by
  `paper/build_schematic_figures.py`.
- **Overpressure relief valve** (0.5 psi cracking) hangs at the bottom of the chamber
  stack, at the KF40 cross where the bellows connects; every KF40 joint in the stack
  seals on an elastomer O-ring carried on its centering ring. (R. Guymon, PR #3,
  2026-07-07.)
- **The continuous argon flow is not ceramics-only.** The nickel grain-growth
  anneals also ran under a constant 20 SCCM argon flow (high vacuum → argon
  backfill → purge → constant 20 SCCM for the duration of the anneal). Do not
  word the atmosphere passage so that "continuous argon flow" reads as unique
  to the high-temperature ceramic work; what distinguishes the ceramic practice
  is only that the argon flowed while the turbopump was running. (R. Guymon,
  PR #3, 2026-07-15.)
- **P-Trap between the turbopump and the vacuum chamber** — it protects the
  turbopump from falling debris. Noted by R. Guymon (PR #3, 2026-07-13) with the
  explicit instruction **"don't include yet"**: this fact is NOT in the manuscript
  or schematics, and should not be added until the lab asks for it.

## Build

- Build the manuscript with `make pdf` in `paper/` (pdflatex × multiple passes +
  bibtex; REVTeX 4.2 class with the `aip,rsi` options); `make draft` builds the
  notes-visible `paper-draft.pdf`. Always rebuild both `paper/paper.pdf` and
  `paper/paper-draft.pdf` after editing `paper/paper.tex`.
- `paper/real_person_paper.tex` → `make real` → `paper/real_person_paper.pdf` is
  the "real person" restyled variant requested by R. Guymon (PR #3, 2026-07-14):
  the prose follows the Extension-to-ceramics section's style — no `$\sim$`
  approximations (write "approximately" or a plain range) and no
  em-dash/semicolon/colon splices (short declarative sentences).
  **`real_person_paper.tex` is now the live manuscript — make all content
  edits there. `paper.tex` / `paper.pdf` / `paper-draft.pdf` are frozen as the
  pre-restyle record; do not edit or rebuild them** (R. Guymon, PR #3,
  2026-07-15/16). Content differences from the frozen `paper.tex`: the
  thermal-grooving panel is a main-text figure, the AIP-required
  "Supplementary Material" section follows the Conclusions, and four figures
  were promoted from the SI on 2026-07-16 to fill the 5-page budget
  (disassembled crucible photo, vacuum/gas-handling photos, EBSD IPF maps,
  YSZ charge-stack schematic — main-text figure order: 1 overview, 2 furnace
  photo, 3 crucible parts, 4 loading sequence, 5 vacuum details, 6 Kikuchi,
  7 EBSD, 8 grooving, 9 microstructure, 10 YSZ grain growth, 11 YSZ stack).
  On length: AIP's RSI rule caps contributed Conference Articles
  at five pages, and its word-count method **excludes the abstract, author
  list, acknowledgments, and references** — so body content should stay
  within five pages' worth, but the reference list spilling onto a further
  page does not violate the limit.
- REVTeX 4.2f predates the 2023+ LaTeX kernel/array table internals; `paper.tex`
  disables REVTeX's begin-document tabular patching (see the commented
  `\switch@tabular` override in the preamble) — do not remove it, and do not use
  REVTeX's `ruledtabular` environment (use booktabs, as the manuscript already does).
- Regenerate figures with `make figures` in `paper/` (validation + characterization +
  schematic/photo figures).
- `paper/SI.tex` → `make si` → `paper/SI.pdf` is the supplementary-material PDF.
  The AIP author instructions (mirrored in `paper/template/rsi/`, "Using
  Supplementary Material in Your Manuscript") require SI as a **single separate
  PDF named `SI.pdf`** at initial submission, with alt text under each SI
  figure/table caption; after acceptance AIP deposits it in Figshare with its
  own DOI. **`SI.tex` is the editable source of record for the SI**; the files
  in `paper/supplementary/` are earlier working notes and are no longer
  mirrored. Contents: supplementary figures S1–S9 (four former SI figures
  moved to the main text on 2026-07-16), Table S1 specimen–run
  linkage with hyperlinked raw logs, Table S2 bill of materials, and a prose
  design-file inventory section (the Table S3 path listing was removed).
  Run-ID/specimen-ID detail and exact equipment models are allowed here (they
  are deliberately kept out of the main text); the no-LEPEL rule still applies.
- **No repository file paths in the SI body or captions.** (R. Guymon, PR #3,
  2026-07-16: "Rewrite it as though a real person wrote it, and just include
  the necessary information instead of redirecting a reader to a specific
  file.") Published SI reads as self-contained prose. The only repository
  mentions are (a) one availability sentence in the SI's opening paragraph
  (GitHub URL + Zenodo DOI) and (b) the Table S1 run IDs, which hyperlink to
  the raw run logs with the URL hidden behind the run-ID text (that linkage
  was S. Baird's explicit request). Do not reintroduce `\texttt{}`/`\path{}`
  repo paths, build-script/`make figures` narration, or "the complete
  cross-reference is <file>"-style redirections. The SI prose also follows
  the real-person style: no `$\sim$` (write "approximately"/"about") and
  short declarative sentences.
