#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

MMF_names = ["43650-022X","43650-032X","43650-042X","43650-052X","43650-062X","43650-072X","43650-082X","43650-092X","43650-102X","43650-112X","43650-122X"]
MMF_pins = range(2,13)
# following values are from datasheet
MMF_dimA = [9.65,12.65,15.65,18.65,21.65,24.65,27.65,30.65,33.65,36.65,39.65] 
MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
MMF_dimC = [14.20,17.20,20.20,23.20,26.20,29.20,32.20,35.20,38.20,41.20,44.20]
for i in range(len(MMF_names)):
    f = footgen.Footgen("Molex-"+MMF_names[i])
    f.pins = MMF_pins[i] 
    f.height = MMF_dimC[i]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 3.00
    f.width = 4.37
    f.padheight = 1.27
    f.padwidth = 2.54
    f.box_corners((f.height+2)/2,f.width/2,-(f.height+2)/2,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+1.0,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-1.0,-(f.width+f.padwidth))
    #signal pads
    f.rowofpads([0,-2.15-2.54/2],"left",1,f.pins)
    # header case gnds at the back
    f.add_pad("MNT",-f.height/2 + 3.43/2, 0  ,3.43,1.65) 
    f.add_pad("MNT",f.height/2  - 3.43/2, 0  ,3.43,1.65) 
    f.finish()
