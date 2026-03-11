# wobb

**Category:** Commands > Acquire > Tune

## NAME

**wobb** - Manual tuning and matching of the probe


## DESCRIPTION

The command wobb allows you to manually tune and match the probe. It opens the wobble window showing the wobble curve.
 
The buttons have the following functions:
 Change the number of wobble steps [wbst].
 Change the wobble sweep width [wbsw].
 Change the wobble frequency.
 Switch to the next channel/nucleus (if available).
 Stop the wobble procedure.
Turn the tuning and matching knobs on the probe until the wobble curve is exactly in the middle and its minimum reaches the zero line.
An NMR probe must be tuned and matched because it is a resonance circuit. If its resonance frequency and impedance are the same as the transmitter frequency and impedance, respectively, the full transmitter power is transferred to the probe. However, if either or both are different, part of the transmitter power is reflected by the probe. This results in a longer 90° pulse or, for a given pulse length, a smaller flip angle.
### NOTE

Note that a multi nuclear probe has a resonance circuit for each nucleus and each nucleus must be tuned and matched separately.
 
The command wobb is normally used without argument. It can, however, be used with arguments. For example:
1. wobb high
- Starts with the nucleus with the highest frequency and continues in the order of decreasing frequency.
2. wobb ext50
- Uses an external 50 ohm resistor as a reference.
3. wobb f1
- Starts with frequency channel f1. It continues with the next higher frequency or, if the argument high is also used, with the next lower frequency.
4. wobb f2
- Starts with frequency channel f2. It continues with the next higher frequency or, if the argument high is also used, with the next lower frequency.
5. wobb f<x> f<y>: simultaneous wobbling of channels F<x> and F<y> in edasp. For WBSW the respective array entries are used, i.e. WBSW[0] for channel F1, WBSW[1] for channel F2 etc. If WBSW[x] is 0 then WBSW[0] is used as a fallback.
6. wobb all: simultaneous wobbling of all channels in edasp using the respective WBSW entries.
7. wobb wbst 1024 f1 wbsw 4.5 f2 wbsw 60: simultaneous wobbling of channels f1 and f2 with WBST=1024, and f1 using 4.5MHz and f2 using 60MHz for WBSW
 
The wobb command allows you to optimize both the probes resonance frequency (tuning) and impedance (matching). It sends a low power RF signal to the probe and sweeps that signal over a certain frequency range. The number of steps (frequencies) within that range is defined by the acquisition parameter WBST. The width of the frequency range is defined by WBSW. The center frequency depends on the nucleus; SFO1 for NUC1, SFO2 for NUC2 etc. The deviation of the probe impedance from the nominal 50 ohm is shown as function of the frequency in the TopSpin data field. This is the so-called wobble curve. At the probe’s resonance frequency, the curve shows a dip, the minimum reflected power. Tuning the probe means adjusting its resonance frequency until it reaches SFO1. Matching the probe means adjusting its impedance until the reflected power reaches zero.
The entire wobble procedure involves the following steps:
1. Stop the sample rotation if this is on, for example with ro off, or by pressing the SPIN ON/OFF button through the BSMS display.
2. Setup the nucleus or nuclei for the current experiment with edasp.
- This will automatically set the parameters SFO1, SFO2 etc.
3. Click Acquire | Observe fid window or enter acqu to switch to the TopSpin acquisition menu. If, however, tuning and matching is observed on the preamplifier, this step can be skipped (see below).
4. Enter wobb. The wobble curve will appear in the TopSpin data field showing a dip at a certain frequency. At the center of the data field, you will see a vertical line. If you do not see the dip, it probably lies outside of the data field. In that case, you should click the  button or enter wbsw to increase the sweep width. You can do this while wobb is running.
5. When the dip is visible, you can start tuning and matching as follows:
1. Turn the tuning knob until the dip lies across the vertical line.
2. Turn the matching knob until the dip has reached a minimum. Matching influences tuning, so the dip probably moves away from the center.
3. Turn the tuning knob until the dip lies at the center again. Tuning influences matching, so the dip probably moves up again.
4. Turn the matching knob until the dip reaches a minimum again.
5. Continue this process until the dip lies exactly across the vertical line and reaches the x-axis.
6. In case of a multi nuclei experiment, you have to switch to the next nucleus. For multiple channel experiments (2D, 3D etc.) tuning and matching of the cannels (e.g. 1H, 13C, 15N) interdependent. The command wobb all will work on all nuclei in parallel. Note that wobb automatically starts with the nucleus with the lowest basic frequency. You can switch to the nucleus with the next higher frequency in two possible ways:
1. Press Channel Select at the HPPR. This will automatically select the nucleus with the next higher frequency.
2. Click  or enter wbsw in TopSpin. Answer the question "Do you want to change the nucleus" with yes.
3. Repeat step 5 for the current nucleus.
7. If your experiment involves more than two nuclei, repeat step 6 for each further nucleus.
8. Click  or enter stop on the command line to finish the wobble procedure.
A probe has a tuning knob (labeled T) and matching knob (labeled M) for each resonance circuit. Most probes have two, one for 1H and one for X-nuclei. When the tuning knob reaches the end of its range before the probe is properly tuned, you should turn it to the middle of its range, adjust matching, then tuning, then matching etc. A similar procedure can be used if the matching knob reaches the end of its range.
The process of tuning and matching can also be followed on the HPPR preamplifier. Some people find that more convenient and it is necessary when the computer screen is not visible from the position of the probe. The horizontal row of LED’s indicates tuning, the vertical row indicates matching. When you turn the tuning or matching knob at the probe, you will see how the number of lit LED’s changes. The probe is perfectly tuned when only one LED (a green one) is lit. The same holds for matching. In practice, proper tuning, and matching means that only green LEDs are lit. If the LED update seems to be very slow, this might be caused by the time-consuming update of the wobble curve in the TopSpin acquisition display. In that case, you can simply click to close the wobble window.
Broadband probes usually have sliders for tuning and matching rather than turning knobs. These have the advantage that their positions are numbered. The default slider positions for each nucleus are usually written on cards that are kept with the probe. When wobbling is started with these default values, only some fine tuning and matching is required.
The probe resonance frequency and impedance are dependent on the sample. This can be a problem in automation, where several samples are measured but the probe is only matched and tuned on one of them. Bruker ATM probes support automatic tuning and matching which can be performed on every sample during automation (see description of the commands atmm and atma).


## INPUT PARAMETERS

1. Set by the user with eda or by typing wbst, wbsw etc.:
1. WBST - number of wobble steps
2. WBSW - wobble sweep width 
2. Set by the user with edasp or eda => NUC1:
1. NUC1 - NUC4 - the nuclei for which the probe is tuned and matched
2. SFO1 - SFO4 - irradiation frequency


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. <tshome>/prog/wobble/
1. acqu_go4 - wobble parameters 
2. Pulsprog_X - wobble pulse program


## SEE ALSO

atma, atmm
© 2025 Bruker BioSpin GmbH & Co. KG
