#/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

f = footgen.Footgen("xuntong-ptr9018")
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.1524
f.pins = 30
f.pitch = 1.27 # mm
f.width = 23
f.padheight = 0.8128 # mm
f.padwidth = 2.2 # mm
#f.height = 2.16
height = 17.4244
width = 22.6568
sidepads = 6
offset_width = 4.064
offset_height = 5.5118
f.rowofpads([(offset_width+(15-1)*f.pitch)/2, height-f.padwidth/3],"left",22,15)
f.rowofpads([width-f.padwidth,height/2],"down",16,sidepads)
f.rowofpads([(offset_width+(15-1)*f.pitch)/2,f.padwidth/3],"right",1,15)
f.finish()

