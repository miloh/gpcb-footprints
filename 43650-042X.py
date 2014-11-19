#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

MMF_names = ["43650-042X"]
MMF_pins = [4]
# following values are from datasheet
MMF_dimA = [ 15.65]
MMF_dimB = [ 9.00]
MMF_dimC = [ 20.20]
for i in range(len(MMF_names)):
    f = footgen.Footgen(MMF_names[i])
    f.pins = MMF_pins[i] 
    f.height = MMF_dimC[i]
    
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.1524
f.pitch = 3.00
f.width = 4.37+1.20
f.padheight = 1.27
f.padwidth = 2.54
f.silkboxwidth  = f.width + 2
f.silkboxheight = f.height + 2
# add_pad(self,name,x,y,xsize,ysize)
# add smt pads for the case (2 on the end and it looks like 4 support tabs /10
# conductors, along the length of the connector)
print f
print f.pins

#signal pads
f.rowofpads([0,-2.15-2.54/2],"right",1,f.pins)

# header case gnds at the back
f.add_pad("end pad left ",-f.height/2 + 3.43/2, 0  ,3.43,1.65) 
f.add_pad("end pad right",f.height/2  - 3.43/2, 0  ,3.43,1.65) 
f.finish()

