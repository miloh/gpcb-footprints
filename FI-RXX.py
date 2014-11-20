#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

FI_RE_names = ["FI-RE-21", "FI-RE-31", "FI-RE-41", "FI-RE-51"]
FI_RE_pins = [21, 31, 41, 51]
FI_RE_dimA = [16, 21.0, 26, 31]
FI_RE_dimB = [10, 15.0, 20, 25]
FI_RE_dimC = [20.35, 25.35, 30.35, 35.35]
FI_RE_dimD = [3, 4.0, 4.0, 5.0]
FI_RE_dimE = [None, None,  4.0, 5.0]
FI_RE_dimF = [20.95, 25.95, 30.95, 35.95]
FI_RE_dimG = [19.75, 24.75, 29.75, 34.75]
FI_RE_dimH = [22.85, 27.85, 32.85, 37.85]
for i in range(len(FI_RE_names)):
    f = footgen.Footgen(FI_RE_names[i])
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pins = FI_RE_pins[i] 
    f.pitch = 0.5 
    f.height = FI_RE_dimG[i]+2.15+2.15
    f.width = 4.35 
    f.padheight = 0.25
    f.padwidth = 1.55 
    f.box_corners((f.height+2)/2,(3.75+1.5+1.55)/2,-(f.height+2)/2,-(f.width+f.padwidth))
    # Pin One Notch 
    f.silk_line(-(f.pitch*(f.pins-1))/2,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+f.pitch,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2-f.pitch,-(f.width+f.padwidth))
    #signal pads
    f.rowofpads([0,-3.75/2-f.padwidth/2],"right",1,f.pins)
    # prohibition area -- still need to figure out how to make this area
    # header case gnds at the back
    f.add_pad("GND MNT",-FI_RE_dimB[i]/2      ,  3.75/2  ,1.3,1.5) 
    f.add_pad("GND MNT",-FI_RE_dimB[i]/2 + FI_RE_dimD[i] , 3.75/2 ,1.3,1.5)
    f.add_pad("GND MNT",+FI_RE_dimB[i]/2        ,  3.75/2  ,1.3,1.5) 
    f.add_pad("GND MNT",+FI_RE_dimB[i]/2 - FI_RE_dimD[i] , 3.75/2 ,1.3,1.5)
    # four corner gnds
    #f.add_pad("gnd mnt left ",-FI_RE_dimA[i]/2,3.75/2+1.55/2,2.50,1.55) 
    f.add_pad("GND MNT",-FI_RE_dimA[i]/2,-3.75/2-1.55/2,2.50,1.55) 
    #f.add_pad("gnd mnt right",FI_RE_dimA[i]/2,3.75/2+1.55/2,2.50,1.55) 
    f.add_pad("GND MNT",FI_RE_dimA[i]/2,-3.75/2-1.55/2,2.50,1.55) 
    f.add_pad("GND MNT",-FI_RE_dimG[i]/2-2.05/2,3.75/2-2.5/2,2.05,2.50) 
    f.add_pad("GND MNT",FI_RE_dimG[i]/2+2.05/2,3.75/2-2.5/2,2.05,2.50) 
    f.finish()

