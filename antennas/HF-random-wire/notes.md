# HF Random Wire Build

# Parts and General Engineering

## Random Wire
 - NOT resonant
 - has about 450 Ohms of resistance
 - General coax is 50 Ohms so 450 / 50 = 9, therefore 9:1 Transformer
 

## 71-76 ft as per:
 - Covers 80-40-30-20-17-15-12-10
 - https://k7mem.com/Ant_End_Fed.html#Not_Random_Multi (75-78ft)
 - https://udel.edu/~mm/ham/randomWire/ (68-74)
 - https://www.hamuniverse.com/randomwireantennalengths.html (71Ft)
 - https://www.dxengineering.com/parts/cew-viz24-pnk100
 

## 9:1 transformer:
 - https://hamradiooutsidethebox.ca/2023/08/17/91-41-11-or-nonenone/
 - https://ashishrd.com/2024/01/06/random-wire-antennas/#:~:text=A%20random%20wire%20antenna%20has%20an%20unpredictable,the%20impedance%20down%20to%20a%20workable%20range.
 - Using 16 AWG and a FT140 torroid, should be ok for 200W
     - https://www.pa9x.com/the-broadband-common-mode-choke/


## Mix 61 Torroid
 - https://palomar-engineers.com/ferrite-products/ferrite-cores/ferrite-mix-selection
 - Mix 61 will withstand high power in multi ratio (2:1, 4:1, 9:1) impedance transformers (baluns/ununs). Currie temperature > 300 C
 - https://palomar-engineers.com/ferrite-products/ferrite-cores/FT140-61-ID=-9-RFI-Range-200-2000-MHz-TX36-23-15-4C25-Replacement-p74396404
 - FT140-61, ID=.9", RFI Range 200-2000 MHz - TX36/23/15-4C25 Replacement
 - $3.89

## Enameled Copper Wire for Coil
 - https://a.co/d/3CU0YEQ
 - 16 AWG
 - $8.79
 - 2 oz, ~ 15ft\
 - 0.0492 Dia

## Torroid Sizing
 - 3 wires x 9 Turns = 27 turns
 - 0.0492 * 27 = 1.3"
 - 1.25MM * 27 = 33.75MM 
 - 2mm spacing * 10 = 20mm 
 - + 3 extra spaces * 2mm = 6mm
 - = 26mm total spacing + 33.75mm wire = 59.75mm
 - 59.75mm inside circumference = 19.01 mm inside diameter (0.748 inches)

## Feed line choke:
 - aka 1:1 transformer
 - https://a.co/d/d560U2d
 - Use RG-316 coax
 - Use FT240-31 Torroid
 - 2.5mm 
 - 8-12 turns
 - https://forums.radioreference.com/threads/common-mode-choke-question.480451/

## Radials / Counterpoise:
 - 4 radials around 3-5m (9-16ft)
 - https://youtu.be/ciX1KlQrcrs?si=lmw6CwUZHWPo0aNo&t=293
 - https://www.antennasbyn6lf.com/
 - 4 * 16 ft = 64 ft
 - https://a.co/d/4e4I0kO
 - https://www.digikey.com/en/products/detail/mueller-electric-co/BU-25/304566
 - https://www.globalindustrial.com/p/banana-jack-ring-terminal-0020in
 - https://www.youtube.com/watch?v=pTNojRg8x40


# Build



