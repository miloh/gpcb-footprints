# element_flags, description, pcb-name, value, mark_x, mark_y,
# text_x, text_y, text_direction, text_scale, text_flags
Element["" "UP3B-100 inductor" "L1" "UP3B" 0 0 5mm -6.0mm 0 100 ""]
(
# Pad[x1, y1, x2, y2, thickness, clearance, mask, name , pad number, flags]
	Pad[-7.75mm -2.45mm
	    -7.75mm  2.45mm
	    3.8mm 0.20mm 3.9mm "1" "1" "square"]
	Pad[7.75mm -2.45mm
	     7.75mm  2.45mm
	     3.8mm 0.20mm 3.9mm "1" "1" "square"]
    ElementArc [ 0mm  0.5mm 6.35mm 6.35mm  40  100 500]
    ElementArc [ 0mm -0.5mm 6.35mm 6.35mm -40 -100 500]
# ElementArc [ rX rY Width Height StartAngle DeltaAngle Thickness]
    ElementLine[-9.80mm -4.55mm -4.90mm -4.55mm 500]
    ElementLine[ 9.80mm -4.55mm  4.90mm -4.55mm 500]
    ElementLine[-9.80mm  4.55mm -4.90mm  4.55mm 500]
    ElementLine[ 9.80mm  4.55mm  4.90mm  4.55mm 500]
)
