# element_flags, description, pcb-name, value, mark_x, mark_y,
# text_x, text_y, text_direction, text_scale, text_flags
Element[0x00000000 "Standard SMT resistor, capacitor etc" "" "0603" 0 0 0.3mm 
-1.4mm 0 60 ""]
(
# 
# Pad[x1, y1, x2, y2, thickness, clearance, mask, name , pad number, flags]
# centers = -0.75, 0,  +0.75, 0 
# line = 0.05 +/-y around center
# thickness = 0.70
	Pad[  -0.75mm -0.05mm
	      -0.75mm  0.05mm
		0.70mm 0.10mm 0.75mm "A" "1" "square"]
	    Pad[0.75mm -0.05mm
	        0.75mm  0.05mm
		0.70mm 0.10mm 0.75mm "K" "2" "square"]
	ElementLine [0.28mm -0.38mm 0.28mm 0.38mm 0.10mm]
)
