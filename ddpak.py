#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution


import footgen

#
# Implements footprints for IRF5305S from infineon
# datasheet source irf5305spbf.pdf
#
f = footgen.Footgen("irf5305s")
f.silkwidth = 0.254 
f.pins = 3
f.width = 11.43 # mm
f.height = 17.78 #mm 
f.epadwidth = f.width # mm
f.epadheight = 8.89 # mm
f.padwidth = 2.08  # mm
f.padheight = 3.81 # mm
f.add_pad( str(1), (-f.width + f.padwidth)/2, f.height-(f.padheight)/2, f.padwidth, f.padheight) 
f.add_pad( str(2), 0.0, f.epadheight/2,                    f.epadwidth, f.epadheight) 
f.add_pad( str(3), (f.width - f.padwidth)/2, f.height-(f.padheight)/2, f.padwidth, f.padheight) 

f.finish()

