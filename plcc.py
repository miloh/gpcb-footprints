#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution


# units in mm
import footgen
f = footgen.Footgen("PLCC4-WS2812B")
f.generator.clearance = 0.204
f.generator.mask_clearance = 0.080
f.pins = 4
f.pitch = 3.3 
f.height = 3.4 
f.width = 2.4
f.silkwidth = 0.254 
f.padheight = 1.6
f.padwidth = 0.9
f.pinswide= 3.4 
#   silk component outlines
f.rowofpads([-f.height/2 - f.padwidth/2, 0],"down",1,2)
f.rowofpads([f.height/2 + f.padwidth/2 , 0],"up",3,4)
# Pin1 diamond mark with 10mil silkwidth
f.silk_diamond(-(f.pitch*(f.pins-1))/2,f.width+f.padwidth,f.padheight,0.254)
#f.silk_crop(3.3, pin1="diamond",rotate='-90')
f.finish()
