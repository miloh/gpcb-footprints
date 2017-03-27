#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

# Implements pcb mount camera sockets from molex 
# standard mobile imaging architecture (SMIA) compliant
# camera sockets 
# these sockets typically come in on-board and through-board designs
# http://www.molex.com/molex/products/family?key=camera_sockets&channel=products&chanName=family&pageTitle=Introduction

import footgen

basename = "Molex-105028-{0}"
# work in progress
f = footgen.Footgen(basename.format("1001"))
f.pins = 32
f.pinshigh = f.pins/4
f.pinswide = f.pinshigh
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.080
f.pitch = 0.90
f.width = 7.78
f.height = f.width
f.padheight = 0.50
f.padwidth = 9.46-7.78
## 8 rows of pads to create
## rowofpads(self, pos, whichway, startnum, numpads)
## pos is the center position [x,y]
## whichway is up down left or right
## inner ring of pads 
f.sm_pads()
#f.rowofpads()
#f.rowofpads()
#f.rowofpads()
#f.rowofpads()
## outer ring of pads, note 7 per row only,
#f.rowofpads()
#f.rowofpads()
#f.rowofpads()
#f.rowofpads()
## edge pads on the outer ring, 2 per row 
#f.rowofpads()
#f.rowofpads()
#f.rowofpads()
#f.rowofpads()
f.finish()

f = footgen.Footgen(basename.format("3011-b"))
f.pins = 32
f.pinshigh = f.pins/4
f.pinswide = f.pinshigh
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.080
f.pitch = 0.90
f.width = 7.78
f.height = f.width
f.padheight = 0.50
f.padwidth = (9.46-7.78)/2
f.mirror = 0 
f.qfn()
# set up for outside rows of pads
f.pins = 4
f.padheight = (11.26-6.55)/2
f.padwidth = 0.65
f.pitch = 6.55+f.padheight
f.width = 11.26 - 0.65*2.0
f.height = f.width
f.pinshigh = 2
f.pinswide = f.pinshigh
f.sm_pads()
f.finish()

# an alternate method of building the footprint for this part
f = footgen.Footgen(basename.format("3011"))
f.pins = 32
f.pinshigh = f.pins/4
f.pinswide = f.pinshigh
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.080
f.pitch = 0.90
f.width = 7.78
f.height = f.width
f.padheight = 0.50
f.padwidth = (9.46-7.78)/2
f.mirror = 0 
f.qfn()
xsize = 0.65
ysize = (11.26-6.55)/2
x = (11.26-0.65)/2
y = (11.26 - ysize)/2
# set up for outside rows of pads
f.add_pad("mount",x,y,xsize,ysize)
f.add_pad("mount",-x,y,xsize,ysize)
f.add_pad("mount",-x,-y,xsize,ysize)
f.add_pad("mount",x,-y,xsize,ysize)
f.add_pad("mount",y,x,ysize,xsize)
f.add_pad("mount",-y,x,ysize,xsize)
f.add_pad("mount",-y,-x,ysize,xsize)
f.add_pad("mount",y,-x,ysize,xsize)
f.finish()
