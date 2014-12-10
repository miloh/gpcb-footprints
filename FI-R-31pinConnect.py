#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

f = footgen.Footgen("FI-R-31")
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.080
f.pins = 31
f.pitch = 0.5 
# following values are from datasheet
# for 31 pin device
dimA = 21.0
dimB = 15.0
dimC = 25.35
dimD = 4.0
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
f.padwidth = 1.55 
f.silkboxwidth  = 29.95
f.silkboxheight = 15.0
f.silkbox(w=f.silkboxwidth,h=f.silkboxheight)
# add_pad(self,name,x,y,xsize,ysize)
# add smt pads for the case (2 on the end and it looks like 4 support tabs /10
# conductors, along the length of the connector)

#signal pads
#f.rowofpads([dimH/2,5.1/2-1.55/2],"right",1,31)
f.rowofpads([0,-3.75/2-f.padwidth/2],"right",1,31)
# header case gnds at the back
f.add_pad("gnd mnt1",-dimB/2      ,  3.75/2  ,1.3,1.5) 
f.add_pad("gnd mnt2",-dimB/2 + dimD , 3.75/2 ,1.3,1.5) 
f.add_pad("gnd mnt3",+dimB/2        ,  3.75/2  ,1.3,1.5) 
f.add_pad("gnd mnt4",+dimB/2 - dimD , 3.75/2 ,1.3,1.5) 
# four corner gnds
#f.add_pad("gnd mnt left ",-dimA/2,3.75/2+1.55/2,2.50,1.55) 
f.add_pad("gnd mnt left ",-dimA/2,-3.75/2-1.55/2,2.50,1.55) 
#f.add_pad("gnd mnt right",dimA/2,3.75/2+1.55/2,2.50,1.55) 
f.add_pad("gnd mnt right",dimA/2,-3.75/2-1.55/2,2.50,1.55) 

f.add_pad("end pad right",-dimG/2-2.05/2,3.75/2-2.5/2,2.05,2.50) 
f.add_pad("end pad left",dimG/2+2.05/2,3.75/2-2.5/2,2.05,2.50) 

f.finish()

