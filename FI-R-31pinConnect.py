#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

f = footgen.Footgen("FI-R-31")
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.1524
f.pins = 31
f.pitch = 0.5 
f.height = bodyheight + f.padwidth/2  
# following values are from datasheet
# for 31 pin device
f.dimA = 21
f.dimB = 15
f.dimC = 25.35
f.dimD = 4
f.dimE = None
f.dimF = 25.95
f.dimG = 24.75
f.dimH = 27.85
# widths for differnt pin counts in this family
# width(21)=10
# width(31)=15
# width(41)=20
# width(51)=25 
f.width = 15
f.padheight = 0.25
f.padwidth = 0.7 
f.silkboxwidth  = 29.95
f.silkboxheight = 15
f.rowofpads([0,0],"right",1,31)
# add_pad(self,name,x,y,xsize,ysize)
# add smt pads for the case (2 on the end and it looks like 4 support tabs /10
# conductors, along the length of the connector)
f.rowofpads([x,y],"right",1,floor(
f.add_pad("mnt1",f.dimE,1.55,1.3) 
f.add_pad("mnt2",4+D,,1.55,1.3) 
f.add_pad("mnt3",4+E,,1.55,1.3) 
f.add_pad("mnt4",4+0,,1.55,1.3) 
f.add_pad("mnt5",4+0,,1.55,1.3) 
f.add_pad("mnt6",f.dimG-3,,1.55,1.3) 
f.finish()

