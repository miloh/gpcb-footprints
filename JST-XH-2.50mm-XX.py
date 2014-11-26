#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

# implements SMT side entry type only!!! through hole components still needed to be added
# following values are from datasheet
#
XH_basename = "JST-XHP-"
XH_pins = [1,2,2,3,4,5,6,6,7,8,9,10,11,12,13,14,15,16,20] 
XH_special = ["","","(10.0)-U","","","","","(5.0)-U","","","","","","","","","","",""] 
XH_dimA = [None,2.5,10.0,5.0,7.5,10.0,12.5,25.0,15.0,17.5,20.0,22.5,25.0,27.5,30.0,32.5,35.0,37.5,47.5] 
XH_dimB = [3.2,5.7,13.2,8.2,10.7,13.2,15.7,28.2,18.2,20.7,23.2,25.7,28.2,30.7,33.2,35.7,38.2,40.7,50.7]
XH_dimC = [4.8,7.3,14.8,9.8,12.3,14.8,17.3,29.8,19.8,22.3,24.8,27.3,29.8,32.3,34.8,37.3,39.8,42.3,52.3]
for i in range(len(XH_pins)):
    f = footgen.Footgen(XH_basename + str(XH_pins[i]) + XH_special[i])
    f.pins = XH_pins[i] 
    f.height = XH_dimC[i]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 2.50
    f.width = 13.0
    f.padheight = 1.30
    f.padwidth = 11-6.5  
    f.box_corners( (f.pitch*f.pins-1)/2+2.3+1.8+1 , (f.width+2)/2 , -(f.pitch*f.pins-1)/2-2.3-1.8-1 , (-(f.width+2)/2))
    # should create a function for creating a pin1 diamond
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+1)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+f.padheight/2 , -(f.width+2)/2)
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+1)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-f.padheight/2 , -(f.width+2)/2)
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+3)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+f.padheight/2 , -(f.width+2)/2)
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+3)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-f.padheight/2 , -(f.width+2)/2)
    #signal pads
    f.rowofpads([ 0 , -f.width/2+f.padwidth/2],"left",1,f.pins)
    #side wing gnds
    f.add_pad("MNT", -(f.pitch*f.pins-1)/2-2.3-1.8/2 , f.width/2-3.9/2 ,1.8,3.9) 
    f.add_pad("MNT", +(f.pitch*f.pins-1)/2+2.3+1.8/2 , f.width/2-3.9/2 ,1.8,3.9) 
    f.finish()
