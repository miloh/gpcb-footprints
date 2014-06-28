Element["" "PLCC4" "PLCC4" "" 0mil 0mil 50mil -90mil 4 80 ""]
(
# ------------------------------------------------------------------
# Pad[ rX1   rY1   rX2   rY2  Thickn  Clr  Msk  Nm  Nr Fl ]
#-------------------------------------------------------------------
	Pad[  0mm    0mm 0.5mm    0mm  1.0mm 18mil 43mil "1" "1" "square"]
	Pad[  0mm  3.2mm 0.5mm  3.2mm  1.0mm 18mil 43mil "2" "2" "square"]
	Pad[4.9mm  3.2mm 5.4mm  3.2mm  1.0mm 18mil 43mil "3" "3" "square"]
	Pad[4.9mm    0mm 5.4mm    0mm  1.0mm 18mil 43mil "4" "4" "square"]

	ElementLine [-0.5mm -1.0mm 6.4mm -1.0mm 5mil]
	ElementLine [-1.0mm  -0.5mm -1.0mm 4.2mm 5mil]
	ElementLine [-1mm  4.2mm 6.4mm 4.2mm 5mil]
	ElementLine [6.4mm  -1mm 6.4mm 4.2mm 5mil]
	#pin 1 notch 
	ElementLine [-0.5mm -1.0mm -1.0mm -0.5mm 5mil]
	)
