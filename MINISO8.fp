
# ST LM2904 datasheet for reference to this package, 'MiniSO-8'

# Element[element_flags, description, pcb-name, value, mark_x, mark_y, text_x, text_y, text_direction, text_scale, text_flags
Element[""  "MiniSO-8" "" "" 1000 1000 -9000 5100 1 100 ""]
(

# Silk screen around package
	ElementLine[ 6700  11250  6700 -11250 600]
	ElementLine[ 6700 -11250 -6700 -11250 600]
	ElementLine[-6700 -11250 -6700  11250 600]
	ElementLine[-6700  11250  6700  11250 600]
# Silk screen Pin 1 indicator
	ElementLine[-7200  11750 -6700  11250 600]


# Pad[X1, Y1, X2, Y3, width, clearance, soldermask, "pin name", "pin number", flags]

# bottom row
	Pad[-3900  9550 -3900  7150 1600 1200 2750 "1" "1"  0x00000100]
	Pad[-1300  9550 -1300  7150 1600 1200 2750 "2" "2"  0x00000100]
	Pad[ 1300  9550  1300  7150 1600 1200 2750 "3" "3"  0x00000100]
	Pad[ 3900  9550  3900  7150 1600 1200 2750 "4" "4"  0x00000100]

# top
	Pad[-3900 -9550 -3900 -7150 1600 1200 2750 "8" "8"  0x00000100]
	Pad[-1300 -9550 -1300 -7150 1600 1200 2750 "7" "7"  0x00000100]
	Pad[ 1300 -9550  1300 -7150 1600 1200 2750 "6" "6"  0x00000100]
	Pad[ 3900 -9550  3900 -7150 1600 1200 2750 "5" "5"  0x00000100]

)
