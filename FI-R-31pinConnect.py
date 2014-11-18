#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

f = footgen.Footgen("FI-R-31")
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.1524
f.pins = 31
f.pitch = 0.5 
# following values are from datasheet
# for 31 pin device
dimA = 21
dimB = 15
dimC = 25.35
dimD = 4
dimE = None
dimF = 25.95
dimG = 24.75
dimH = 27.85
# widths for differnt pin counts in this family
# width(21)=10
# width(31)=15
# width(41)=20
# width(51)=25 
f.height = dimF
f.width = 4.35 
f.padheight = 0.25
f.padwidth = 0.7 
f.silkboxwidth  = 29.95
f.silkboxheight = 15
# add_pad(self,name,x,y,xsize,ysize)
# add smt pads for the case (2 on the end and it looks like 4 support tabs /10
# conductors, along the length of the connector)

#signal pads
#f.rowofpads([dimH/2,5.1/2-1.55/2],"right",1,31)
f.rowofpads([0,-3.75+f.padwidth/2],"right",1,31)
# header case gnds at the back
f.add_pad("gnd mnt1",-dimA/2 + 3 + dimD , 4.35/2  ,1.55,1.3) 
#f.add_pad("gnd mnt2",-dimA/2 + 3 + dimD*2 , -4.35/2 ,1.55,1.3) 
f.add_pad("gnd mnt3",+dimA/2 - 3 - dimD , 4.35/2  ,1.55,1.3) 
#f.add_pad("gnd mnt4",+dimA/2 - 3 - dimD*2 , -4.35/2 ,1.55,1.3) 
# four corner gnds
f.add_pad("gnd mnt left ",-dimA/2,4.35/2+1.55/2,1.55,1.3) 
f.add_pad("gnd mnt left ",-dimA/2,-4.35/2-1.55/2,1.55,1.3) 
f.add_pad("gnd mnt right",dimA/2,4.35/2+1.55/2,1.55,1.3) 
f.add_pad("gnd mnt right",dimA/2,-4.35/2-1.55/2,1.55,1.3) 
f.finish()

