#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution


# implements board headers for JAE FI-R type high density header connects
# following values are from datasheet  available from JAE 
# MB-0153-4E_FI-R.pdf (vendor provided)
# Note VF and HF dimension arrays are different, and that the SJ102934
# datasheet is incorrect 
# Note that SJ102934.pdf (mouser) is incorrect, and mixes values from HF and VF
# components 

import footgen

FI_RE_basename ="FI-R-E-{0}S-{1}"
FI_RE_EntryTypes = ["VF","HF"] #HF Horizontal (side entry) and VF Vertical 
FI_RE_contacts = [21, 31, 41, 51]
#
FI_RE_VF_dimA = [16, 21, 26, 31]
FI_RE_VF_dimB = [10, 15, 20, 25]
FI_RE_VF_dimC = [20.35, 25.35, 30.35, 35.35]
FI_RE_VF_dimD = [3, 4, 4, 5]
FI_RE_VF_dimE = [None, None,  4, 5]
FI_RE_VF_dimF = [20.95, 25.95, 30.95, 35.95]
FI_RE_VF_dimG = [19.75, 24.75, 29.75, 34.75]
FI_RE_VF_dimH = [21.85, 26.85, 31.85, 36.85]
for i in range(len(FI_RE_contacts)):
    f = footgen.Footgen(FI_RE_basename.format(FI_RE_contacts[i],FI_RE_EntryTypes[0]))
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pins = FI_RE_contacts[i] 
    f.pitch = 0.5 
    f.height = float(FI_RE_VF_dimG[i])+2.15+2.15
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
    f.add_pad("GND MNT",-float(FI_RE_VF_dimB[i])/2      ,  3.75/2  ,1.3,1.5) 
    f.add_pad("GND MNT",-float(FI_RE_VF_dimB[i])/2 + float(FI_RE_VF_dimD[i]) , 3.75/2 ,1.3,1.5)
    f.add_pad("GND MNT",+float(FI_RE_VF_dimB[i])/2        ,  3.75/2  ,1.3,1.5) 
    f.add_pad("GND MNT",+float(FI_RE_VF_dimB[i])/2 - float(FI_RE_VF_dimD[i]) , 3.75/2 ,1.3,1.5)
    # four corner gnds
    f.add_pad("GND MNT",-FI_RE_VF_dimA[i]/2,-3.75/2-1.55/2,2.50,1.55) 
    f.add_pad("GND MNT",FI_RE_VF_dimA[i]/2,-3.75/2-1.55/2,2.50,1.55) 
    f.add_pad("GND MNT",-FI_RE_VF_dimG[i]/2-2.05/2,3.75/2-2.5/2,2.05,2.50) 
    f.add_pad("GND MNT",FI_RE_VF_dimG[i]/2+2.05/2,3.75/2-2.5/2,2.05,2.50) 
    f.finish()

FI_RE_HF_dimA = [16, 21, 26, 31]
FI_RE_HF_dimB = [10, 15, 20, 25]
FI_RE_HF_dimC = [21.35, 26.35, 31.35, 36.35]
FI_RE_HF_dimD = [None, None, None, None]
FI_RE_HF_dimE = [None, None, None, None]
FI_RE_HF_dimF = [20.95, 25.95, 30.95, 35.95]
FI_RE_HF_dimG = [19.75, 24.75, 29.75, 34.75]
FI_RE_HF_dimH = [22.85, 27.85, 32.85, 37.85]
for i in range(len(FI_RE_contacts)):
    f = footgen.Footgen(FI_RE_basename.format(FI_RE_contacts[i],FI_RE_EntryTypes[0]))
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pins = FI_RE_contacts[i]
    f.pitch = 0.5 
    f.height = float(FI_RE_HF_dimG[i])+2.15+2.15
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
    f.add_pad("GND MNT",-float(FI_RE_HF_dimB[i])/2      ,  3.75/2  ,1.3,1.5) 
    f.add_pad("GND MNT",-float(FI_RE_HF_dimB[i])/2 + float(FI_RE_HF_dimD[i]) , 3.75/2 ,1.3,1.5)
    f.add_pad("GND MNT",+float(FI_RE_HF_dimB[i])/2        ,  3.75/2  ,1.3,1.5) 
    f.add_pad("GND MNT",+float(FI_RE_HF_dimB[i])/2 - float(FI_RE_HF_dimD[i]) , 3.75/2 ,1.3,1.5)
    # four corner gnds
    f.add_pad("GND MNT",-FI_RE_HF_dimA[i]/2,-3.75/2-1.55/2,2.50,1.55) 
    f.add_pad("GND MNT",FI_RE_HF_dimA[i]/2,-3.75/2-1.55/2,2.50,1.55) 
    f.add_pad("GND MNT",-FI_RE_HF_dimG[i]/2-2.05/2,3.75/2-2.5/2,2.05,2.50) 
    f.add_pad("GND MNT",FI_RE_HF_dimG[i]/2+2.05/2,3.75/2-2.5/2,2.05,2.50) 
    f.finish()
