"""Submit an Edison Scientific literature task: why do as-annealed
(preparation-free) nickel surfaces from this furnace yield high-quality,
directly indexable EBSD Kikuchi patterns?

Follow-up requested by S. Baird (PR #12, 2026-07-22) to support the
no-prep-EBSD emphasis added to the main-text Kikuchi figure and the
Microstructural validation section.

No file upload is needed, so this uses the LITERATURE job type (per
CLAUDE.md, ANALYSIS is only required when uploading files).

Run from paper/ebsd_noprep_query/:  python3 submit_query.py
Writes the created task id to edison_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import TaskRequest

QUERY = """\
We built a custom vacuum induction annealing furnace (manuscript in
preparation for Review of Scientific Instruments) and observed something we
want to explain and cite properly: nickel specimens taken straight out of
the furnace produce high-quality, directly indexable EBSD (electron
backscatter diffraction) Kikuchi patterns with absolutely no metallographic
sample preparation - no grinding, no polishing, no etching, no
electropolishing. The specimens were literally removed from the furnace
chamber and placed directly into the SEM/EBSD chamber.

Experimental context:
- Specimens: Ni200 and 4N5-purity (99.995%) nickel sheet, plus some
  palladium thermal-evaporation charges.
- Anneals: 900-1400 C soaks (typically 1200-1325 C for 12-40 h), near the
  Ni melting point, in a machined graphite crucible/susceptor. The specimen
  is sandwiched between alumina discs inside the closed graphite crucible.
- Atmosphere: the fused-quartz chamber is pumped to 1e-6 to 1e-8 Torr,
  then backfilled with argon flowing continuously at 20 SCCM during the
  anneal.
- Observations: even at the detector's coarse 8x8 binning the Kikuchi
  bands and zone axes are crisply resolved; orientation maps index hundreds
  of grains; grain boundaries are delineated by deep thermal grooves
  (several spanning the full ~100 um sheet thickness); grains are large
  (tens to hundreds of microns) and equiaxed.

Questions:
1. What mechanisms explain diffraction-quality, as-annealed surfaces with
   no preparation? Please assess candidates with literature support:
   (a) absence of near-surface plastic deformation - the anneal removes
   the deformed layer that polishing normally has to remove, and EBSD
   samples only the top few tens of nanometers; (b) an oxide-free or
   ultra-thin-oxide surface, from the high-vacuum + flowing-argon
   environment and/or carbothermal / low-pO2 conditions inside the closed
   graphite crucible (CO/CO2 buffering, NiO reduction or dissociation at
   these temperatures); (c) surface smoothing / faceting by evaporation-
   condensation and surface diffusion near the melting point; (d) anything
   else documented (e.g., sublimation cleaning of adsorbates).
2. What is the precedent? Find published examples of successful EBSD on
   as-annealed, unprepared metal surfaces (any metal, ideally nickel), and
   of vacuum/inert-atmosphere annealing used deliberately as the final
   surface-preparation step for EBSD. How unusual is our observation?
3. What are the limits/caveats we should acknowledge - e.g., how thick can
   a native or grown NiO film be before pattern quality degrades, carbon
   contamination from the graphite crucible, thermal grooving and faceting
   affecting the effective surface tilt, and any bias this introduces into
   indexed maps (e.g., unindexed points at grooves)?
4. Suggest 2-3 sentences, with the key citations, that we could adapt for
   the manuscript to explain why no-preparation EBSD works here.

Please give specific literature references (DOIs) for the mechanisms and
precedents.\
"""


def main():
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    task_data = TaskRequest(name=JobNames.LITERATURE, query=QUERY)
    responses = client.create_task(task_data)
    task_id = responses if isinstance(responses, str) else str(responses)
    with open("edison_task_id.txt", "w") as f:
        f.write(task_id + "\n")
    print("created task:", task_id)


if __name__ == "__main__":
    main()
