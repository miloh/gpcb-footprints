# The following elements can be used to create a gEDA pcb layout footprint

# Element [ SFlags "Desc" "pcb-name" "value" MX MY TX TY TDir Scale TSFlags](
# Pad        [ x1 y1 x2 y2 thickness clear mask "name" "pad_number" sflags]
# Pin        [ rX  rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
# ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
# ElementArc [ rX rY Width Height StartAngle DeltaAngle Thickness]
#)

# notes:
#   "SFlags" == symbolic flags.  Note sflags is the leading attribute,
# however in following pad and pin elements it is the trailing attribute.
#
# SFlags is where the pin part gets various values:
# "", "pin, via, hole, showname, onsolder, square, octogon, edge2"
#

#These elements are used in layouts, but can be converted to the
#ElementLine element above in editor or gui
# Line [ x1 y1 x2 y2 thickness clear "sfflags"]
# Via  [ X1 y1 thickness  clearance  mask drill  "name" "sfflags?"]
# Arc[43.7965mm 9.9086mm 98.00mil 98.00mil 5.00mil 12.00mil 180 90 "clearline"]

Element ["" "snaptron GX06240 single sided" "single sided" "" 0mm 0mm 5mm 5mm 0 100 ""](
Pin  [0.25mm  -0.65mm 0mm 0mil 0mil 0.205mm "plated_vent" "" "via"]
Pin  [0mm 0mm 2.45mm 0mm 6mm 0.00245mm "contact_ring" "2" "via"]
Pad  [0.32mm 0mm 2.73mm 0mm 0.64mm 0 0 "tongue" "2" "square"]
Pad  [-2.505mm -1.96mm -2.505mm 1.96mm 1.09mm 0mm 0mm "left" "3" "square"]
Pad  [2.505mm -1.96mm 2.505mm -1.90mm 1.09mm 0mm 0mm "rightupper" "rightupper"4"square"]
Pad  [2.505mm 1.96mm 2.505mm 1.90mm 1.09mm 0mm 0mm "rightlower" "rightlower"4"square"]
Pad  [-1.415mm -3.05mm 1.415mm -3.05mm 1.09mm 0mm 0mm "top" "3" "square"]
Pad  [-1.415mm 3.05mm 1.415mm 3.05mm 1.09mm 0mm 0mm "bottom" "3" "square"]

Pad  [1.96mm -3.05mm 2.50mm -2.5mm 1.09mm 0mm 0.0mm "angleTR" "3" ""]
Pad  [-1.96mm -3.05mm -2.50mm -2.5mm 1.09mm 0mm 0.0mm "angleTL" "3" ""]
Pad  [-1.96mm 3.05mm -2.50mm 2.5mm 1.09mm 0mm 0.0mm "angleLL" "3" ""]
Pad  [1.96mm 3.05mm 2.50mm 2.5mm 1.09mm 0mm 0.0mm "angleLR" "3" ""]
)

