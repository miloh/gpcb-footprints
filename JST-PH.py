#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen
format = "geda"

# implements board headers for JST PH type crimping wire to board header connects
# following values are from datasheet ePH.pdf available at
# http://www.jst-mfg.com/product/pdf/eng/ePH.pdf

# JST SMT PH Top Entry Headers
PH_basename = "JST-{0}{1}B-PH-SM4-TB"
PH_EntryType = {'Top':'B','Side':'S'}
PH_pins = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 
PH_dimA = [2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0] 
PH_dimB = [7.95,9.95,11.95,13.95,15.95,17.95,19.95,21.95,23.95,25.95,27.95,29.95,31.95,33.95,35.95]
for i in range(len(PH_pins)):
    f = footgen.Footgen(PH_basename.format(PH_EntryType['Top'],PH_pins[i]),output_format=format)
    f.pins = PH_pins[i] 
    f.height = PH_dimA[i]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.080
    f.pitch = 2.00
    f.width = 7.5  
#    f.padheight = 1.0
    f.padwidth = 1.0
    f.padheight = 5.5
#    f.padwidth = 5.5
    mntpadwidth = 3.0  # increase this value for improved mechanical strength
    mntpadheight = 1.6 # change this as well 
    mntpad_x_offset = 1.6
    mntpad_y_offset = 3.25 #1.0
# silk box must be made in segments since the pads extend past the bounds
    #f.box_corners( -PH_dimB[i]/2 , f.padwidth/2-7.5, +PH_dimB[i]/2 , f.padwidth/2+1 )
# silk at "end face of wafer on the mating side"
    f.silk_line( -PH_dimB[i]/2 , f.padheight/2-7.5, +PH_dimB[i]/2 , f.padheight/2-7.5 )
    f.silk_line( -PH_dimB[i]/2 , f.padheight/2-7.0, -PH_dimB[i]/2 , f.padheight/2-7.5 )
    f.silk_line( +PH_dimB[i]/2 , f.padheight/2-7.0, +PH_dimB[i]/2 , f.padheight/2-7.5 )
# silk at the back
    f.silk_line( -PH_dimB[i]/2 , f.padheight/2+0.25 , +PH_dimB[i]/2 , f.padheight/2+0.25 )
    f.silk_line( -PH_dimB[i]/2 , f.padheight/2-2.0, -PH_dimB[i]/2 , f.padheight/2+0.25)
    f.silk_line( +PH_dimB[i]/2 , f.padheight/2-2.0, +PH_dimB[i]/2 , f.padheight/2+0.25 )
#signal pads
    f.rowofpads([ 0 , 0],"right",1,f.pins)
# diamond mark at pin1
    f.silk_diamond(-PH_dimA[i]/2,f.padheight/2-7.5,0.5,0.254)
#side wing gnds
    f.add_pad("MNT", -PH_dimA[i]/2-mntpad_x_offset-mntpadheight/2 , +f.padwidth/2-f.width+mntpad_y_offset+mntpadwidth/2 ,mntpadheight,mntpadwidth) 
    f.add_pad("MNT", +PH_dimA[i]/2+mntpad_x_offset+mntpadheight/2 , +f.padwidth/2-f.width+mntpad_y_offset+mntpadwidth/2 ,mntpadheight,mntpadwidth) 
    f.finish()

# JST SMT PH Side Entry Headers
# Reuse the basename and EntryType from above 
PH_pins = [2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
PH_dimA = [2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0] 
PH_dimB = [7.9,9.9,11.9,13.9,15.9,17.9,19.9,21.9,23.9,25.9,27.9,29.9,31.9,33.9,35.95]
for i in range(len(PH_pins)):
    f = footgen.Footgen(PH_basename.format(PH_EntryType['Side'],PH_pins[i]), output_format=format)
    f.pins = PH_pins[i] 
    f.height = PH_dimA[i]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.080
    f.pitch = 2.00
    f.width = 9.0  
    f.padwidth = 1.0
    f.padheight = 3.5
    mntpadwidth = 3.4 # increase this value for improved mechanical strength
    mntpadheight = 1.5 # change this as well 
    mntpad_x_offset = 1.6 # do not adjust unless correcting errors
    mntpad_y_offset = -1.05 # do not adjust unless correcting errors
# silk box must be made in segments since the pads extend past the bounds
    # silk at "end face of wafer on the mating side"
    f.silk_line( -PH_dimA[i]/2-f.padwidth, f.padheight/2-9.0,+PH_dimA[i]/2+f.padwidth, f.padheight/2-9.0 )
# silk at the back
    f.silk_line( -PH_dimB[i]/2 , f.padheight/2+0.25 , +PH_dimB[i]/2 , f.padheight/2+0.25 )
    f.silk_line( -PH_dimB[i]/2 , f.padheight/2-4.5, -PH_dimB[i]/2 , f.padheight/2+0.25)
    f.silk_line( +PH_dimB[i]/2 , f.padheight/2-4.5, +PH_dimB[i]/2 , f.padheight/2+0.25 )
#signal pads
    f.rowofpads([ 0 , 0],"left",1,f.pins)
    f.silk_diamond(+PH_dimA[i]/2,f.padwidth/2-9.0,0.5,0.254) # silk diamond mark at pin1
#side wing gnds, note the change in placement and dim w/r/t the PH top entry headers
    f.add_pad("MNT", -PH_dimA[i]/2-mntpad_x_offset-mntpadheight/2, +f.padwidth/2-f.width-mntpad_y_offset+mntpadwidth/2 , mntpadheight , mntpadwidth) 
    f.add_pad("MNT", +PH_dimA[i]/2+mntpad_x_offset+mntpadheight/2, +f.padwidth/2-f.width-mntpad_y_offset+mntpadwidth/2 , mntpadheight , mntpadwidth) 
    f.finish()



# JST PTH PH side and top entry Headers
# new basename for these parts
PH_basename = "JST-{0}{1}B-PH-K-S"
PH_dimA = [2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0] 
PH_dimB = [5.9,7.9,9.9,11.9,13.9,15.9,17.9,19.9,21.9,23.9,25.9,27.9,29.9,31.9,33.9]
for i in range(len(PH_pins)):
    f = footgen.Footgen(PH_basename.format(PH_EntryType['Top'],PH_pins[i]),output_format=format)
    f.pins = PH_pins[i] * 2 
    f.height = PH_dimA[i]
    f.generator.clearance = 0.254/2
    f.generator.mask_clearance = 0.0254
    f.pitch = 2.00
    f.drill = 0.778
    f.diameter = f.drill+ 0.508 
    f.width = 0   # this needs to be zero to get a single line of pins
    xsize = 4.5
    silk_xmin = -1.7
    silk_xmax = silk_xmin + xsize
    f.draw_silk = False
# silk box must be made in segments since the pads extend past the bounds
    f.box_corners( silk_xmin ,  -PH_dimB[i]/2 , silk_xmax , +PH_dimB[i]/2  )
## silk at back of the connector 
#    f.silk_line( -3.0,-PH_dimB[i]/2 , -3.0,  +PH_dimB[i]/2  )
#    f.silk_line( -3.0,-PH_dimB[i]/2 , -2.0,  -PH_dimB[i]/2  )
#    f.silk_line( -3.0,+PH_dimB[i]/2 , -2.0,  +PH_dimB[i]/2  )
## silk at the open end of the mating side 
#    f.silk_line( 1.5,-PH_dimB[i]/2 , 1.5,  +PH_dimB[i]/2  )
#    f.silk_line( 0.5, -PH_dimB[i]/2 ,1.5,  -PH_dimB[i]/2 )
#    f.silk_line( 0.5, +PH_dimB[i]/2 ,1.5,  +PH_dimB[i]/2  )
#signal pins
    f.dip(pitch=-f.pitch,pins=f.pins,drill=f.drill,diameter=f.diameter,width=f.width,draw_silk=f.draw_silk)
# diamond mark at pin1
    f.silk_diamond(silk_xmax, PH_dimA[i]/2, 0.5, 0.254)
    f.finish()

## JST PTH PH Side Entry Headers
## reuse basename and entrytype from above
PH_dimA = [2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0] 
PH_dimB = [5.9,7.9,9.9,11.9,13.9,15.9,17.9,19.9,21.9,23.9,25.9,27.9,29.9,31.9,33.9]
for i in range(len(PH_pins)):
    f = footgen.Footgen(PH_basename.format(PH_EntryType['Side'],PH_pins[i]),output_format=format)
    f.pins = PH_pins[i] * 2 
    f.height = PH_dimA[i]
    f.generator.clearance = 0.254/2
    f.generator.mask_clearance = 0.0254
    f.pitch = 2.00
    f.drill = 0.778 
    f.diameter = f.drill + 0.508 
    f.width = 0  
    xsize = 7.6
    silk_xmin = -1.6
    silk_xmax = silk_xmin + xsize
    f.draw_silk = False
# silk box must be made in segments since the pads extend past the bounds
    f.box_corners( silk_xmin , -PH_dimB[i]/2 ,silk_xmax , +PH_dimB[i]/2   )
#    # silk at back of the connector 
#    f.silk_line( -5.5,-PH_dimB[i]/2 , -5.5,  +PH_dimB[i]/2  )
#    f.silk_line( -5.5,-PH_dimB[i]/2 , -2.0,  -PH_dimB[i]/2  )
#    f.silk_line( -5.5,+PH_dimB[i]/2 , -2.0,  +PH_dimB[i]/2  )
## silk at the open end of the mating side 
#    f.silk_line( 1.0,-PH_dimB[i]/2 , 1.0,  +PH_dimB[i]/2  )
#    f.silk_line( 0, -PH_dimB[i]/2 ,1.5,  -PH_dimB[i]/2 )
#    f.silk_line( 0, +PH_dimB[i]/2 ,1.5,  +PH_dimB[i]/2  )
# signal pins
    f.dip(pitch=-f.pitch,pins=f.pins,drill=f.drill,diameter=f.diameter,width=f.width,draw_silk=f.draw_silk)
# diamond mark at pin1
    f.silk_diamond(silk_xmin , PH_dimA[i]/2,0.5,0.254)
    f.finish()
