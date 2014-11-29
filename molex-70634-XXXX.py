#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen


# Molex SDA-70634 family of SMT 0.1" pitch pcb headers
# implements SMT side entry type only!!! through hole components still needed to be added
# following values are from datasheet "015912045_sd.pdf
# all units mm

molex_70634_basename = "molex-70634-02"
molex_70634_pins = [2,3,4] # more pins in the complete sheet 
molex_70634_dimA = [2.54,5.08,7.62] 
molex_70634_dimB = [5.33,8.13,10.67]
molex_70634_dimC = [8.64,11.43,13.97]
molex_70634_dimD = [5.33,7.87,10.41] 
molex_70634_dimE = [0.13,0.13,0.13]
molex_70634_dimF = [2.79,3.05,3.95]
molex_70634_dimG = [4.32,4.57,4.57]
for i in range(len(molex_70634_pins)):
    f = footgen.Footgen(molex_70634_basename + str(molex_70634_pins[i]).zfill(2) ) 
    f.pins = molex_70634_pins[i] 
    outer_Xedge = molex_70634_dimC[i]
    f.height = molex_70634_dimD[i]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 2.54
    f.width = 13.59 + 3.18
    f.padheight = 1.65
    f.padwidth = 5.33 
    f.silk_line( -outer_Xedge/2,-13.59-f.padheight/2,-outer_Xedge/2,0)
    f.silk_line( +outer_Xedge/2,-13.59-f.padheight/2,+outer_Xedge/2,0)
    f.silk_line( -outer_Xedge/2,-13.59-f.padheight/2,+outer_Xedge/2,-13.59-f.padheight/2)
    #f.box_corners(-f.height/2, 10.69/2,+f.height/2,
    #f.box_corners( (f.pitch*f.pins-1)/2+2.3+1.8+1 , (f.width+2)/2 , -(f.pitch*f.pins-1)/2-2.3-1.8-1 , (-(f.width+2)/2))
    # should create a function for creating a pin1 diamond
    diamond_xcenter = molex_70634_dimA[i]/2
    diamond_ycenter = -13.59-f.padheight/2
    diamond_size = 1
    f.silk_line(diamond_xcenter - diamond_size, diamond_ycenter, diamond_xcenter, diamond_ycenter + diamond_size)
    f.silk_line(diamond_xcenter - diamond_size, diamond_ycenter, diamond_xcenter, diamond_ycenter - diamond_size)
    f.silk_line(diamond_xcenter + diamond_size, diamond_ycenter, diamond_xcenter, diamond_ycenter + diamond_size)
    f.silk_line(diamond_xcenter + diamond_size, diamond_ycenter, diamond_xcenter, diamond_ycenter - diamond_size)

    #signal pads
    f.rowofpads([ 0 , 0],"left",1,f.pins)
    #side wing gnds
    f.add_via(pin="circle" ,x= -f.height/2, y= -10.69, size= 3.404 ,pad=3.404) 
    f.add_via(pin="masked" ,x= f.height/2, y= -10.69, size= 3.404,pad=3.404) 
    f.finish()
