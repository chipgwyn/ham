# POTA 710 & Doublet Project

Been using my Yaesu FT-710 as a base station radio for a while.  Changed to a full SDR setup which freed the 710 up for other uses.  Figured I could
make it into a nice 100W POTA setup.  Ok, so that's our starting point.  I've always heard how well a ladder line fed doublet performed and thought
this might make a good pairing.  To finish it out I would need a tuner and I wanted to have an excuse to play with manual tuners, so located and
purchased a used MFJ-945C tuner.  Having all the base bits sorted, time to get busy designing!

# The Classic 44ft Doublet

Since this will be for portable operations and I have a POTA33H mast already, that seemed like a good place to begin.  Mast is 33ft tall, elements
are 44ft each.  Assuming I want to keep with the general rule of about 120 degrees between elements, we do some triangle math.  I came up with 
an acceptable foot print of 52ft to each side of the mast.  Tent stakes at each side of the mast, 52ft from the mast.  String from tent stake to the
end of the element. 

## Why 44ft

There seems to be a general guideline that when designing your doublet, shoot for resonant length at the lowest frequency you plan to operate on.
Since 40m was my limit I had planned on building for that length (1/2 wave dipole for 40m, gives about 33ft per element).  However, after doing 
additional reading some had mentioned that making it perfectly resonant on 40m would make tuning a bit difficult on 20m.  The solution to that was
going just further down than 40m.  Sure it made 40m require _some_ tuning but would make 20m even easier.  Since we'll be using a tuner anyway and
since the goal of all this is for POTA, and 20M is where _most_ of the action is, this seemed like an easy decision.  So...44ft it is!

## The Ladder Line

General idea for open-wire ladder line is to shoot for 450-500 ohm.  The distance between the wires dictates the resistance based also on wire
thickness.  I wanted to go light so 20ga wire was my target.  I use the BNTechGo Silicon Rubber Tinned Copper 20ga wire.  Wire thickness is 0.92mm
and insulation is about .44mm, so 1.8mm overall.  


$$
Z_c = 120 * cosh^-1 \frac{D}{d}
$$

Stuff


