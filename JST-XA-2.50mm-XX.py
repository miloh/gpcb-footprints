#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

### need to fix this to implement PTH as well as SMT
import footgen

# implements XA side entry type only!!! through hole components still needed to be added
# following values are from datasheet
#
XA_basename = "S{:02d}B-XASK-1"
XA_circuits = [2,3,4,5,6,7,8,9,10,11,12,13,14] 
XA_dimA = [2.5,5.0,7.5,10.0,12.5,15.0,17.5,20.0,22.5,25.0,27.5,30.0,32.5] 
XA_dimB = [7.5,10.0,12.5,15.0,17.5,20.0,22.5,25.0,27.5,30.0,32.5,35.0,37.5]
XA_dimD = [1.25,2.50,3.75,5.00,6.25,7.50,8.75,10.00,11.25,12.50,13.75,15.00,16.25]
for i in range(len(XA_circuits)):
    f = footgen.Footgen(XA_basename.format(XA_circuits[i]))
    f.pins = XA_circuits[i]
    f.height = 12.6
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.080
    f.pitch = 2.50
    f.width = XA_dimA[i] 
    f.box_corners( (f.pitch*f.pins-1)/2+2.3+1.8+1 , (f.width+2)/2 , -(f.pitch*f.pins-1)/2-2.3-1.8-1 , (-(f.width+2)/2))
    # should create a function for creating a pin1 diamond
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+1)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+f.padheight/2 , -(f.width+2)/2)
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+1)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-f.padheight/2 , -(f.width+2)/2)
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+3)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+f.padheight/2 , -(f.width+2)/2)
    f.silk_line( -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch , -((f.width+3)/2) , -(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-f.padheight/2 , -(f.width+2)/2)
    #signal pads
  f.via_array(f.pins,1,f.pitch,[ -0 , -f.width/2+f.padwidth/2],"left",1,f.pins)
via_array(self, columns=None, rows=None, pitch=None, size=0.3302, pad=0.7,
pin=None)

    #side wing gnds
    f.add_pad("MNT", -(f.pitch*f.pins-1)/2-2.3-1.8/2 , f.width/2-3.9/2 ,1.8,3.9) 
    f.add_pad("MNT", -(f.pitch*f.pins-1)/2-2.3-1.8/2 , f.width/2-3.9/2 ,1.8,3.9) 
    f.add_pad("MNT", -(f.pitch*f.pins-1)/2-2.3-1.8/2 , f.width/2-3.9/2 ,1.8,3.9) 
    f.add_pad("MNT", +(f.pitch*f.pins-1)/2+2.3+1.8/2 , f.width/2-3.9/2 ,1.8,3.9) 
    f.finish()
