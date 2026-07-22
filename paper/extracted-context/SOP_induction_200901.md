# LEPEL Induction Furnace Standard Operating Procedure (Sept 2020)

> Extracted from [`docs/induction_SOP_200901.docx`](../../docs/induction_SOP_200901.docx). Auto-extracted text for reference; the binary file is the source of record.

LEPEL Induction Furnace Usage

Introduction

This induction furnace is from ~1970 and belongs to the mechanical engineering department.

The Johnson group uses it primarily to anneal (i.e. heat treat) metals close to their melting temperature which promotes grain growth. Currently this is the only machine available to the mechanical engineering department that heat metals such as iron and nickel to their melting temperatures (~1400-1500°C +). We couple it with a high-vacuum turbo-molecular pump that can reach ~1E-6 to ~1E-8 torr (outer space ranges between ~1E-6 to ~1E-17 torr) to prevent unwanted oxidation of the sample in metals such as iron and nickel. In Aug. 2019, a “remote control” functionality was implemented to control the induction furnace power via a computer rather than the front panel “power control” knob (it can be easily switched back to manual mode if necessary – ask Kevin Cole - cole@byu.edu - or Sterling Baird – ster.g.baird@gmail.com). A LabVIEW DAQ Assistant generates a current between 0 and 5 mA, corresponding to “off” and “full power”, respectively, that controls the power.

Copper wires (see below) carry the oscillating electric current and the water for cooling.

An electrically conductive sample (e.g. iron, nickel, graphite) is positioned within the solenoid (i.e. loop of coils, see picture below) and experiences an oscillating electromagnetic field that heats the sample (see https://en.wikipedia .org/wiki/Eddy_current)

The frequency of the electromagnetic field ranges between ~200 kHz to 450 kHz for this induction furnace. The grid frequency control knob should affect this (not sure in which direction, but the operator manual may describe), which will in turn affect the efficiency of heating the sample. A high efficiency value is typically ~25 for iron. The max power (i.e. the RF power delivered to the sample @ 5 mA) can be attenuated or increased by “shorting” to a smaller or larger # of coils for an internal transformer, respectively (ask Kevin Cole - cole@byu.edu - or Sterling Baird – ster.g.baird@gmail.com if you need a finer range or a higher max power. Note: This requires a lockout tagout procedure and involves accessing the top panel facing the wall to the left of the furnace when facing the control panel).

Keep anything metallic or conductive away from the coils. The conductive sample should not contact the coils when powered (it will spark). Keep hair/ jewelry/ phones/ watches/ electronics away from the coils (at least ~6”-12”). Other conductive parts of the machine near the induction coils (e.g. screws on the dark brown box through which the copper coils go through) may deliver a moderate shock if you touch them while the machine is powered on, so avoid contact. Wear clean nitrile gloves when loading/unloading samples to prevent oil contamination of the vacuum system from your hands. If a phone is brought too close to the induction coils while powered (e.g. < 6”), the induction furnace may write a message to you via your phone’s keyboard, and possibly cause data-loss or damage. The induction furnace is a very useful, old, high-power machine (up to ~35 kW). Treat it carefully and cautiously.

Procedure

Load the sample

Remove the flange connecting the quartz tube to the flexible metal vacuum hosing and verify that it’s at atmospheric pressure by lifting the tube up and placing it back

Note: if the tube is still under vacuum, verify that the turbo and roughing pumps are not maintaining an active vacuum (see TurboStation directions for turning off the pumps, if turbo pump is off display should read 0%) and open up the small, black, knurled, rubber manual vent valve by turning counter-clockwise. DO NOT OPEN THIS VALVE WHILE THE TURBO PUMP IS RUNNING. Doing so could destroy the turbo pump (~$5000-$10000) (think turbo blade soup)

Stack the following vertically in order from top to bottom: sample|alumina plate(optional)|ceramic cylinder|Teflon tubing (small diameter, thick tube inside large diameter, thin tube) and hold in one hand

Lift the quartz tube with your other hand and insert the “sample stack” from above into the tube. This may require some “finagling.” Be careful not to torque the quartz tube (if cracked, replacement is ~$40-$60)

Bring the quartz tube back down with the O-ring in-between and clamp it together using the flange

Note: The flange does not need to be very tight to operate effectively. If overtightened, it will likely damage the flange and can make the seal less effective. There is a finger-tightening wingnut there for a reason, think finger-tight without needing to strain.

Adjust the vertical position of the sample by adjusting the height of the clamps for the lab stand

Note: be careful of the Edwards vacuum gauge. If dropped and damaged, this could be up to ~$1000 to repair/replace. The “flexible” metal hosing can be difficult to move around and can have a sort of unexpected “spring” or bounce-back. This is one of the main concerns for dropping the vacuum gauge.

Turn the vacuum pump on

Note: make sure that the small, black, knurled, rubber manual vent valve attached to the turbo pump is closed by turning it clockwise, finger-tight, no need to strain.

Turn the water on halfway

Locate the blue handle to the right of the induction furnace (see picture on left)

Note: Perpendicular to the pipes = closed. Parallel to the pipes = fully open.

Turn the handle to ~45° so it is half open to give the machine enough cooling water without creating enough pressure to cause leaks.

Check cooling water lines for leaks. Don’t run the machine if the cooling water is leaking; this could cause major problems with the electricity.

Check the exit line to make sure water is running through the system. The line exits into the drain just below the blue handle water valve (see picture)

Turn on the induction furnace using power switch below control panel

Note: you should hear the machine start (loud, rhythmic hum)

Turn the solenoid knob to “ON” (if inadequate water light turns on & water valve is @~45°, contact Kevin Cole - cole@byu.edu. The water line may be blocked somewhere. Do not turn the water handle past ~45°

Press the “Filament On” button

Note: the corresponding light should turn on

Wait until the overload reset button lights up (~30-60 s) & press it

Note: the button light should turn off when pressed

Open induction_ramping.vi on the laptop (should be an icon on the desktop)

Press Ctrl+E or Window->View Block Diagram to open the block diagram

Double click “simulate arbitrary signal” icon within the block diagram

Click “values”

Input values corresponding to the desired ramping procedure

Note: finding the right values requires calibration to know what current corresponds to the melting temperature. Linear correlation can be assumed, or more rigorous calibration can be done in combination with the melting temperature test by using thermal chalk for lower temperatures.

Note: As an example, the following table will produce the following ramp procedure:

Note: The “DC Amperes Plate” indicator dial (top-right of picture below) should read ~0. If it doesn’t, press the “Set Current to Zero” button, run the VI, verify the dial has dropped to 0, and stop the program. If it still reads a current, there may be an issue with the LabVIEW program (contact Kevin Cole cole@byu.edu or Sterling Baird ster.g.baird@gmail.com), in which case turn off the induction furnace (see directions near end)

Press the “Plate On” button

Note: the corresponding light should turn on

Press the “RF Power” button

Note: the corresponding light should turn on

If you have verified that the ramping procedure is correct, run the LabVIEW VI program

Note: the current vs. time should be displayed graphical on the LabVIEW front panel. As the current increases, this should correspond to an increase in the readings on the “DC Amperes Plate” dial indicator on the induction furnace

Note: Unless the procedure you are running has been tested at least once before, do not leave the induction furnace running unattended for long periods of time (e.g. > 30-60 minutes). The sample could melt and drip, contaminating the vacuum hosing or pumps. The setup could get hot enough to melt the Teflon and/or the quartz tube (in the latter case this could cause serious problems for the turbo pump).

Once the procedure is complete, turn off the induction furnace by reversing the startup order as follows:

Press the “RF Off” button

Press the “Plate Off” button

Press the “Filament Off” button

Turn the water solenoid valve switch to “off”

Turn off the machine (black power switch below control panel)

Turn the blue handle water valve off by turning it perpendicular to the pipes

Turn off the turbo and roughing pumps (without turning off the entire vacuum machine)

Press far right button

When flashing STOP, press far left button

Note: you should hear a click corresponding to the pumps shutting off. The turbo pump will slow down until it reaches 0% power. The roughing pump will also shut off.

Wait for the turbo pump to power down to 0%, then turn the small, black, knurled, rubber manual vent valve situated on the side of the turbo pump counterclockwise to vent the rest of the way (~60 s?)

Turn off the entire vacuum pump machine using the power strip switch it’s connected to

If the temperature ramp down was slow enough (e.g. 1-3 hours), the setup may be cool enough already to remove the sample by reversing the load order as follows (if not wait ~15 minutes for it to cool, then proceed):

Remove the flange

Raise the tube and remove the “sample stack” (sample, ceramic, Teflon tube)

Replace the quartz tube to its original position and clamp the flange on with the O-ring in-between

Other comments

You may see a plasma form near the top of the tube. This is normal (see https://en.wikipedia.org/wiki/Inductively_coupled_plasma)


**Table 1:**


| Time (s) | Current (mA) |

| 0 | 0 |

| 3600 | 4 |

| 7200 | 4 |

| 10800 | 0 |
