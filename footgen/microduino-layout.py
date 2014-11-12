#!/usr/bin/python
import footgen

f = footgen.Footgen("microduino-adapter")
f.maskclear = 0.006 
f.polyclear = 0.33
f.pins = 10 
f.width = 1
f.pitch = 2.54 mm 
f.paddia = 6 mils
f.drill = 50 mils
f.silkboxwidth = 1.2
f.silkboxheight = 1.2
f.dip()
f.finish()
