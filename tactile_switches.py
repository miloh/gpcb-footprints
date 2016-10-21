#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution


import footgen

#
# Implements footprints for PTS645 from C&K
# datasheet source PTS645_7jan16-523842.pdf 
#
f = footgen.Footgen("PTS645-SMTR")
f.silkwidth = 0.254 
f.pins = 4
f.width =  9.5 # mm
f.height = 5.8 # mm
f.padwidth = (f.width - 6.4)/2 # mm
f.padheight = (f.height - 3.2)/2 # mm
f.add_pad( str(1),  (f.width-f.padwidth)/2,  (f.height-f.padheight)/2, f.padwidth, f.padheight) 
f.add_pad( str(2),  (f.width-f.padwidth)/2, -(f.height-f.padheight)/2, f.padwidth, f.padheight) 
f.add_pad( str(3), -(f.width-f.padwidth)/2, -(f.height-f.padheight)/2, f.padwidth, f.padheight) 
f.add_pad( str(4), -(f.width-f.padwidth)/2,  (f.height-f.padheight)/2, f.padwidth, f.padheight) 

# Implement footprint for  SKQG from ALPS

f = footgen.Footgen("SKQG-SMT")
f.silkwidth = 0.254 
f.pins = 4
f.width =  8 # mm
f.height = 4.8 # mm
f.padwidth = (f.width - 4.4)/2 # mm
f.padheight = (f.height - 2.6)/2 # mm
f.add_pad( str(1),  (f.width-f.padwidth)/2,  (f.height-f.padheight)/2, f.padwidth, f.padheight) 
f.add_pad( str(2),  (f.width-f.padwidth)/2, -(f.height-f.padheight)/2, f.padwidth, f.padheight) 
f.add_pad( str(3), -(f.width-f.padwidth)/2, -(f.height-f.padheight)/2, f.padwidth, f.padheight) 
f.add_pad( str(4), -(f.width-f.padwidth)/2,  (f.height-f.padheight)/2, f.padwidth, f.padheight) 

f.finish()

