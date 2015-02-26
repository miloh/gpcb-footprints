# ------------------------------------------------------------------
#Element [element_flags desc pcb-name val mark_x mark_y text_x text_y text_dir text_scale text_flags]
# ------------------------------------------------------------------

Element["" "PLCC6" "WS2812B" "" 0mil 0mil 20mil 35mil 4 70""]
(
# ------------------------------------------------------------------
# Pad[ rX1   rY1   rX2   rY2  Thickn  Clr  Msk  Nm  Nr Fl ]
#-------------------------------------------------------------------
	Pad[ -0.25mm    0mm 0.25mm    0mm  1.0mm 18mil 43mil "3" "3" "square"]
	Pad[ -0.25mm  3.2mm 0.25mm  3.2mm  1.0mm 18mil 43mil "4" "4" "square"]
	Pad[4.65mm  3.2mm 5.15mm  3.2mm  1.0mm 18mil 43mil "1" "1" "square"]
	Pad[4.65mm    0mm 5.15mm    0mm  1.0mm 18mil 43mil "2" "2" "square"]

	ElementLine [-0.525mm -1.15mm 6.15mm -1.15mm 5mil]
	ElementLine [-1.25mm  -0.525mm -1.25mm 4.35mm 5mil]
	ElementLine [-1.25mm  4.35mm 6.15mm 4.35mm 5mil]
	ElementLine [6.15mm  -1.15mm 6.15mm 4.35mm 5mil]
	ElementLine [-0.525mm -1.15mm -1.25mm -0.525mm 5mil]
	)
