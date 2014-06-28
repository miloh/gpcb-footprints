# author: andrew mccubbin
# email: andrewm@thehacktory.com
# dist-license: GPL 2
# use-license: unlimited

# IPC 7351 ref SON50PP300X300X80-11WEED3M
# Dimensions taken from allegro datasheet

# Element[element_flags, description, pcb-name, value, mark_x,
# mark_y, text_x, text_y, text_direction, text_scale, text_flags
Element[0x00000000 "Dual-Flat-Nolead-DFN-10pin-0.5mm-pitch-exposed-pad-package-3x3x0.8mm" "" "" 1000 1000 -13000 8000 1 100 0x00000000]
(

# Silk screen around package
	ElementLine[ 6405  8785  6405 -8785 1000]
	ElementLine[ 6405 -8785 -6405 -8785 1000]
	ElementLine[-6405 -8785 -6405  8785 1000]
	ElementLine[-6405  8785  6405  8785 1000]
# Pin 1 indicator
	ElementLine[-7005  9385 -6405  8785 1000]


# Pad[X1, Y1, X2, Y3, width, clearance,
#     soldermask, "pin name", "pin number", flags]

# bottom row
	Pad[-3937  7185 -3937  5020 1181 1600 1381 "1"  "1"   0x00000100]
	Pad[-1969  7185 -1969  5020 1181 1600 1381 "2"  "2"   0x00000100]
	Pad[    0  7185     0  5020 1181 1600 1381 "3"  "3"   0x00000100]
	Pad[ 1969  7185  1969  5020 1181 1600 1381 "4"  "4"   0x00000100]
	Pad[ 3937  7185  3937  5020 1181 1600 1381 "5"  "5"   0x00000100]

# top row
	Pad[ 3937 -7185  3937 -5020 1181 1600 1381 "6"  "6"   0x00000100]
	Pad[ 1969 -7185  1969 -5020 1181 1600 1381 "7"  "7"   0x00000100]
	Pad[    0 -7185     0 -5020 1181 1600 1381 "8"  "8"   0x00000100]
	Pad[-1969 -7185 -1969 -5020 1181 1600 1381 "9"  "9"   0x00000100]
	Pad[-3937 -7185 -3937 -5020 1181 1600 1381 "10" "10"  0x00000100]

# Exposed paddle (if this is an exposed paddle part)
	Pad[ -1457     0  1457    0 6496 1600 6796 "11" "11"  0x00000100]
)
