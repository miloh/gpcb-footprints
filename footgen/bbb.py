#!/usr/bin/python
import footgen

f = footgen.Footgen("bbb-basic-cape")
f.maskclear = 0.125 
f.polyclear = 0.33
f.pins = 30
f.pitch = 1.27 # mm
f.width = 23
f.padheight = 0.8128 # mm
f.padwidth = 2.2 # mm
#f.height = 2.16
#f.silkboxwidth = 22.6568
#f.silkboxheight = 17.4244
#f.rowofpads("right",[22.6568/2+4.064,17.4244],1,15)
#f.rowofpads("down",[17.4244/2,22.6568],16,6)
#f.rowofpads("left",[22.6568/2+4.064,0],22,15)
f.soh()
f.finish()

