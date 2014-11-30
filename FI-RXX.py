#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution


# Implements board headers for JAE FI-R type high density header connects
# following values are from datasheet  available from JAE 
# MB-0153-4E_FI-R.pdf (vendor provided)
# Note VF and HF dimension arrays are different, and that the SJ102934
# datasheet is incorrect 
# Note that SJ102934.pdf (mouser) is incorrect, and mixes values from HF and VF
# components 

import footgen

FI_RE_basename ="JAE-FI-R-E-{0}S-{1}"
FI_RE_EntryTypes = {'Top':'VF','Side':"HF"} #HF Horizontal (side entry) and VF Vertical 
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
    f = footgen.Footgen(FI_RE_basename.format(FI_RE_contacts[i],FI_RE_EntryTypes['Top']))
    f.generator.clearance = 0.204
    f.generator.mask_clearance = 0.102
    f.pins = FI_RE_contacts[i] 
    f.pitch = 0.5 
    f.height = FI_RE_VF_dimF[i]
    f.width = 5.1 
    f.padheight = 0.25
    f.padwidth = 1.55 
    f.rowofpads([0,0],"right",1,f.pins) #all contacts
#   silk component outlines
# horizontal line segments constructing corners near contacts
    f.silk_line(-FI_RE_VF_dimF[i]/2, f.padwidth/4, -FI_RE_VF_dimG[i]/2, f.padwidth/4)
    f.silk_line(FI_RE_VF_dimF[i]/2, f.padwidth/4,  FI_RE_VF_dimG[i]/2, f.padwidth/4)
# vertical line segments constructing corners near contacts
    f.silk_line(-FI_RE_VF_dimF[i]/2, f.padwidth/4, -FI_RE_VF_dimF[i]/2, f.width)
    f.silk_line(FI_RE_VF_dimF[i]/2, f.padwidth/4, FI_RE_VF_dimF[i]/2, f.width)
# segments outlining prohibition area at cable entry
    f.silk_line(-FI_RE_VF_dimF[i]/2, f.width, -FI_RE_VF_dimG[i]/2,f.width)
    f.silk_line(FI_RE_VF_dimF[i]/2, f.width, FI_RE_VF_dimG[i]/2,f.width)
    f.silk_diamond(-(f.pitch*(f.pins-1))/2,f.width+f.padwidth,f.padheight,0.25) # Pin1 diamond mark
# GND connection pads for the HF and VF version 
    f.add_pad("GND MNT",-float(FI_RE_VF_dimB[i])/2, f.width , 1.3, 1.55)
    f.add_pad("GND MNT",+float(FI_RE_VF_dimB[i])/2, f.width , 1.3, 1.55)
# GND connection pads for the VF version 
    f.add_pad("GND MNT",-float(FI_RE_VF_dimB[i])/2 + float(FI_RE_VF_dimD[i]) , f.width , 1.3, 1.55)
    f.add_pad("GND MNT",+float(FI_RE_VF_dimB[i])/2 - float(FI_RE_VF_dimD[i]) , f.width , 1.3, 1.55)
# GND connection pads for parts with 41 and 51 contacts
    if FI_RE_VF_dimE[i] is not None:
       f.add_pad("GND MNT",float(-FI_RE_VF_dimB[i])/2 + float(FI_RE_VF_dimD[i]) + float(FI_RE_VF_dimE[i]), f.width, 1.3, 1.55)
       f.add_pad("GND MNT",float(+FI_RE_VF_dimB[i])/2 - float(FI_RE_VF_dimD[i]) - float(FI_RE_VF_dimE[i]), f.width, 1.3, 1.55)

#  GND Connection Pads
    f.add_pad("GND MNT",float(-FI_RE_VF_dimA[i])/2, 0 ,   2.50, 1.55)
    f.add_pad("GND MNT",float(+FI_RE_VF_dimA[i])/2, 0 ,   2.50, 1.55)
    f.add_pad("GND MNT",float(-FI_RE_VF_dimA[i])/2, f.width , 2.50, 1.55)
    f.add_pad("GND MNT",float(+FI_RE_VF_dimA[i])/2, f.width , 2.50, 1.55)
# GND connection pad on the side -- possibly for HF side entry type only
#f.add_pad("GND MNT",-FI_RE_VF_dimG[i]/2-2.05/2,   ,2.05,2.50)
#f.add_pad("GND MNT",FI_RE_VF_dimG[i]/2+2.05/2, f.width-f.padwidth/2-2.5/2 ,2.05,2.50)

    f.finish()

# Horizontal Entry aka Side Entry parts
FI_RE_HF_dimA = [16, 21, 26, 31]
FI_RE_HF_dimB = [10, 15, 20, 25]
FI_RE_HF_dimC = [21.35, 26.35, 31.35, 36.35]
FI_RE_HF_dimD = [None, None, None, None]
FI_RE_HF_dimE = [None, None, None, None]
FI_RE_HF_dimF = [20.95, 25.95, 30.95, 35.95]
FI_RE_HF_dimG = [19.75, 24.75, 29.75, 34.75]
FI_RE_HF_dimH = [22.85, 27.85, 32.85, 37.85]
for i in range(len(FI_RE_contacts)):
    f = footgen.Footgen(FI_RE_basename.format(FI_RE_contacts[i],FI_RE_EntryTypes['Side']))
    f.generator.clearance = 0.204
    f.generator.mask_clearance = 0.102
    f.pins = FI_RE_contacts[i] 
    f.pitch = 0.5 
    f.height = FI_RE_HF_dimG[i]
    f.width = 5.1 
    f.padheight = 0.25
    f.padwidth = 1.55 
    f.rowofpads([0,0],"right",1,f.pins) #all contacts 
#   silk component outlines
# horizontal line segments constructing corners near contacts
    f.silk_line(-FI_RE_HF_dimF[i]/2, f.padwidth/4, float(-FI_RE_HF_dimA[i])/2-2.5/2-0.5, f.padwidth/4)
    f.silk_line(FI_RE_HF_dimF[i]/2, f.padwidth/4, float(FI_RE_HF_dimA[i])/2+2.5/2+0.5, f.padwidth/4)
# vertical line segments constructing corners near contacts
    f.silk_line(-FI_RE_HF_dimF[i]/2, f.padwidth/4, -FI_RE_HF_dimF[i]/2, f.padwidth/2)
    f.silk_line(FI_RE_HF_dimF[i]/2, f.padwidth/4, FI_RE_HF_dimF[i]/2, f.padwidth/2)
# segments outlining prohibition area at cable entry
    f.silk_line(-FI_RE_VF_dimF[i]/2, f.width, -FI_RE_VF_dimG[i]/2,f.width)
    f.silk_line(FI_RE_VF_dimF[i]/2, f.width, FI_RE_VF_dimG[i]/2,f.width)
    f.silk_line(-FI_RE_VF_dimF[i]/2, f.width, -FI_RE_VF_dimF[i]/2, f.width-f.padwidth/4)
    f.silk_line(FI_RE_VF_dimF[i]/2, f.width, FI_RE_VF_dimF[i]/2, f.width-f.padwidth/4)
    f.silk_line(-float(FI_RE_HF_dimB[i])/2+1.3, f.width,float(FI_RE_HF_dimB[i])/2-1.3,f.width)
    f.silk_diamond(float(-FI_RE_VF_dimB[i])/2,f.width+f.padwidth,f.padheight,0.25) # Pin1 diamond mark
# GND connection pads for the HF and VF versions
    f.add_pad("GND MNT",float(-FI_RE_VF_dimB[i])/2, f.width , 1.3, 1.55)
    f.add_pad("GND MNT",float(+FI_RE_VF_dimB[i])/2, f.width , 1.3, 1.55)
#  GND connection pads
    f.add_pad("GND MNT",float(-FI_RE_HF_dimA[i])/2, 0 ,   2.50, 1.55)
    f.add_pad("GND MNT",float(+FI_RE_HF_dimA[i])/2, 0 ,   2.50, 1.55)
    f.add_pad("GND MNT",float(-FI_RE_HF_dimA[i])/2, f.width , 2.50, 1.55)
    f.add_pad("GND MNT",float(+FI_RE_HF_dimA[i])/2, f.width , 2.50, 1.55)
# GND connection pad on the side -- possibly for HF side entry type only
    f.add_pad("GND MNT",-FI_RE_VF_dimG[i]/2-2.05/2,f.width-f.padwidth/2-2.5/2, 2.05, 2.50)
    f.add_pad("GND MNT",FI_RE_VF_dimG[i]/2+2.05/2, f.width-f.padwidth/2-2.5/2, 2.05, 2.50)
    f.finish()
