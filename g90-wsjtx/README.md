# WJSTX and friends on the Xiegu G90

For my purposes I needed the following hardware:

 - Digirig Mobile (Cat Config: Logic Levls): https://digirig.net/product/digirig-mobile/
 - Digirig Xiegu G90 Cables: https://digirig.net/product/xiegu-g90-cables/

No CE-19 or DE-19 required!

To Note, this setup was done with v1.80 firmware on the G90

## Connections

 - Plug the serial connector (green) into the bottom port on the left side of the radio
 - Plug the audio connector (mini-din) into the back of the radio
 - USB goes to computer

## Radio Config

The radio must be configured to output audio via the audio port, usually this is done by depressing the "vol" knob
to toggle from speaker to external audio.

For audio input it must be configured to use "Line" instead of the mic.  Press the "FUNC" button, the yellow LED
should illuminate.  Then press the "POW" button until the screen shows "INPUT".  Rotate the VFO knob (big one on
the right) until INPUT indicates "LINE" instead of "MIC".  Depress the VFO knob to confirm.

Set the Automatic Gain Control by depressing the "AGC" button until "AGC-F" is displayed.  This sets it to "Fast".

Depress and Hold the "FUNC" button again to get into the menu system of the radio. Cycle to menu #5 "AUX IN Volum"
and set it to about "8".  Continue to cycle to menu #6 "AUX OUT Volum" and set it to "15".

Radio should be configured as needed.

## Installing Digirig Serial Drivers

Download the Digirig Serial Drivers from: https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads

I used the "CP210x Universal Windows Driver".  As of this writing, v11.4.0 12/18/2024

Once downloaded, unzip into a folder.  Then open "Device Manager", click on your computer in the list, and then
click "Action" from the menu, and then "Add drivers".  Navigate to the folder you unzipped the drivers to and
hit next, installing the drivers.

## WSJTX

Download WSJTX: https://wsjt.sourceforge.io/wsjtx.html as of this writing, 2.7.0 is the latest and install as
as directed.

Configure the radio in WJSTX as pictured here:









