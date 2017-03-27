#!/usr/bin/python
import footgen

f = footgen.Footgen("QFN16-MMA8452Q")
f.mirror = True
f.pitch = 0.5
f.pins = 16
f.width = 3.0
f.height = 3.0
f.padheight = 0.30
f.padwidth = 0.600 #nudged up from MMA8452Q datasheet
f.pinswide = 3.0
f.silk_crop(3.3, pin1="diamond",rotate='-90')
f.rowofpads([-f.height/2+f.padwidth/2,0],"up",1,5)
f.rowofpads([0,-f.width/2+f.padwidth/2],"right",6,3)
f.rowofpads([f.width/2-f.padwidth/2,0],"down",9,5)
f.rowofpads([0,f.width/2-f.padwidth/2],"left",14,3)
f.finish()
