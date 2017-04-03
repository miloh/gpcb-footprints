Element["" "so(n=6,pad_thickness=0.60mm,row_spacing=2.7mm,pad_spacing=0.95mm,ext_bloat=0.2525mm,int_bloat=0.2525mm,line_thickness=0.1mm,pad_mask=0.74mm)" "U1" "6*2.7mm" 0 0 2750 -11100 0 100 ""]
(
	Pad[ -6309 -3740 -4320 -3740 2362 1000 2913 "" "1" "square"]
	Pad[ 4320 -3740 6309 -3740 2362 1000 2913 "" "6" "square"]
	Pad[ -6309 0 -4320 0 2362 1000 2913 "" "2" "square"]
	Pad[ 4320 0 6309 0 2362 1000 2913 "" "5" "square"]
	Pad[ -6309 3740 -4320 3740 2362 1000 2913 "" "3" "square"]
	Pad[ 4320 3740 6309 3740 2362 1000 2913 "" "4" "square"]
	ElementLine[-8179 -5610 -8179 5610 600]
	ElementLine[8179 5610 -8179 5610 600]
	ElementLine[8179 5610 8179 -5610 600]
	ElementLine[-8179 -5610 -1870 -5610 600]
	ElementLine[1870 -5610 8179 -5610 600]
	ElementArc[0 -5610 1870 1870 0 180 600]
	# exposed pad and heatsink mount modification for use with tps54302
	# 
# Pin [ rX  rY Thickness Clearance Mask Drill "Name" "Number" SFlag]
	Pin[ 0nm -2.5mm 1000000nm 609600nm 1100000nm 550000nm "1" "1" ""]
	Pin[ 0nm +2.5mm 1000000nm 609600nm 1100000nm 550000nm "1" "1" ""]
# Pad [ x1 y1 x2 y2 thickness clear mask "name" "pad_number" sflags]
	Pad[ 0 -2.00mm 0 2.00mm 1.0mm 0.4mm 1.05mm "" "1" "square"]
)
