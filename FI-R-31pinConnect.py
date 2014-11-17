#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

f = footgen.Footgen("FI-R Connects")
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.1524
f.pins = 31
f.pitch = 0.5 
f.width = 23
f.padheight = 0.8128
f.padwidth = 2.2 
f.rowofpads([height,YYY],"left",1,31)
f.finish()
