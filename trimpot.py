#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen

# Implement footprint for BI technologies/TT Electronics 84PRxx 1/4" multiturn smd cermet trim pot

trimpot_basename = "84{0}"
trimpot_types = {'Top':'W','Side':'X','SideShort':'P'}
f = footgen.Footgen(trimpot_basename.format(trimpot_types['Top']))
#f = footgen.Footgen(trimpot_basename.format(trimpot_types['Side']))
f.silkwidth = 0.254 # mm
f.pins = 3
f.width = 6.35  # mm
f.height =  7.49  # mm
f.padwidth = 1.02 # mm
f.padheight =  2.8 # mm
#f.box_corners( f.width/2 , f.height/2, -f.width/2, -f.width/2 )
# silk box must be made in segments since the pads extend past the bounds
# left bracket
f.silk_line( -(f.width+0.5)/2   , -f.height/2 , -(f.width)/4     , -f.height/2 )
f.silk_line( -(f.width+0.5)/2   ,  f.height/2 , -(f.width+0.5)/2 , -f.height/2 )
f.silk_line( -(f.width+0.5)/2   ,  f.height/2 , -(f.width)/2     ,  f.height/2 )
# right bracket
f.silk_line(  (f.width) /4    ,   -f.height/2 ,  (f.width+0.5)/2 , -f.height/2 )
f.silk_line(  (f.width+0.5)/2 ,    f.height/2,   (f.width+0.5)/2 , -f.height/2 )
f.silk_line(  (f.width) /2    ,    f.height/2 ,  (f.width+0.5)/2 ,  f.height/2 )
f.add_pad ( "1", -2.54 , (f.height-f.padheight)/2, f.padwidth, f.padheight)
f.add_pad ( "2", 0     , -(f.height-f.padheight)/2,  f.padwidth, f.padheight)
f.add_pad ( "3", 2.54  , (f.height-f.padheight)/2, f.padwidth, f.padheight)
f.finish()

trimpot_basename = "84{0}"
trimpot_types = {'Top':'W','Side':'X','SideShort':'P'}
#f = footgen.Footgen(trimpot_basename.format(trimpot_types['Top']))
f = footgen.Footgen(trimpot_basename.format(trimpot_types['Side']))
f.silkwidth = 0.254 # mm
f.pins = 3
f.width = 6.35  # mm
f.height =  7.49  # mm
f.padwidth = 1.02 # mm
f.padheight =  2.8 # mm
#f.box_corners( f.width/2 , f.height/2, -f.width/2, -f.width/2 )
# silk box must be made in segments since the pads extend past the bounds
# left bracket
f.silk_line( -(f.width+0.5)/2   , -f.height/2 , -(f.width)/4     , -f.height/2 )
f.silk_line( -(f.width+0.5)/2   ,  f.height/2 , -(f.width+0.5)/2 , -f.height/2 )
f.silk_line( -(f.width+0.5)/2   ,  f.height/2 , -(f.width)/2     ,  f.height/2 )
# right bracket
f.silk_line(  (f.width) /4    ,   -f.height/2 ,  (f.width+0.5)/2 , -f.height/2 )
f.silk_line(  (f.width+0.5)/2 ,    f.height/2,   (f.width+0.5)/2 , -f.height/2 )
f.silk_line(  (f.width) /2    ,    f.height/2 ,  (f.width+0.5)/2 ,  f.height/2 )
f.add_pad ( "1", -2.54 , (f.height-f.padheight)/2, f.padwidth, f.padheight)
f.add_pad ( "2", 0     , -(f.height-f.padheight)/2,  f.padwidth, f.padheight)
f.add_pad ( "3", 2.54  , (f.height-f.padheight)/2, f.padwidth, f.padheight)
f.finish()

