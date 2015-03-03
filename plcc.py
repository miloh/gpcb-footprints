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
f.padheight =0.9 
f.padwidth = 1.5 
f.pinswide= 1.5 
## rowofpads(self, pos, whichway, startnum, numpads)
f.rowofpads([-f.height/2 - f.padwidth/2, 0],"down",1,2)
f.rowofpads([f.height/2 + f.padwidth/2 , 0],"up",3,2)
## silk component outlines
# silk_crop(self,w,h,pin1,croplength=0.25,silkwidth=0.155,rotate=0)
# note.  need pinswide & better docs on what it is doing
f.silk_crop(w=6.9, h=5, pin1="diamond",silkwidth=0.155,rotate='180')
f.finish()

f = footgen.Footgen("PLCC4")
f.generator.clearance = 0.204
f.generator.mask_clearance = 0.080
f.pins = 4
f.pitch = 3.3 
f.height = 3.4 
f.width = 2.4
f.silkwidth = 0.254 
f.padheight =0.9 
f.padwidth = 1.5 
f.pinswide= 1.5 
## rowofpads(self, pos, whichway, startnum, numpads)
f.rowofpads([-f.height/2 - f.padwidth/2, 0],"down",1,2)
f.rowofpads([f.height/2 + f.padwidth/2 , 0],"up",3,2)
## silk component outlines
# silk_crop(self,w,h,pin1,croplength=0.25,silkwidth=0.155,rotate=0)
# note.  need pinswide & better docs on what it is doing
f.silk_crop(w=6.9, h=5, pin1="diamond",silkwidth=0.155,rotate='0')
f.finish()

f = footgen.Footgen("PLCC6-WS2812")
f.generator.clearance = 0.204
f.generator.mask_clearance = 0.080
f.pins = 6
f.pitch = 1.1 
f.height = 3.4 
f.width = 2.4
f.silkwidth = 0.254 
f.padheight =0.9 
f.padwidth = 1.5 
f.pinswide= 1.5 
## rowofpads(self, pos, whichway, startnum, numpads)
f.rowofpads([-f.height/2 - f.padwidth/2, 0],"down",1,3)
f.rowofpads([f.height/2 + f.padwidth/2 , 0],"up",4,3)
## silk component outlines
# silk_crop(self,w,h,pin1,croplength=0.25,silkwidth=0.155,rotate=0)
# note.  need pinswide & better docs on what it is doing
f.silk_crop(w=6.9, h=5, pin1="diamond",silkwidth=0.155,rotate='0')
f.finish()
