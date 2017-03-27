# element_flags, description, pcb-name, value, mark_x, mark_y,
# text_x, text_y, text_direction, text_scale, text_flags
Element["" "Bourns Schottky barrier rectifier chip diode " "" "CD1607-B140LF" 48.00mil 43.00mil -20.0mil  -75.0mil 0 50 ""]
(
# Pad[x1, y1, x2, y2, thickness, clearance, mask, name , pad number, flags]
	Pad[ -1.75mm  0
	     -1.75mm  0
	      1.50mm  0.21mm 1.60mm "A" "2" "square"]
	Pad[  1.75mm 0
	      1.75mm 0
	      1.50mm  0.21mm 1.60mm "C" "1" "square"]
# cathode diode mark
	ElementLine[0.70mm -0.82mm 0.70mm 0.82mm 0.25mm]
#lines along body
	ElementLine[-2.10mm -0.90mm 2.10mm -0.90mm 0.10mm]
	ElementLine[-2.10mm 0.90mm 2.10mm 0.90mm 0.10mm]
#bitty encaps showing body
	ElementLine[-2.10mm -0.90mm -2.10mm -0.85mm 0.10mm]
	ElementLine[-2.10mm 0.90mm -2.10mm 0.85mm 0.10mm]
	ElementLine[2.10mm 0.90mm 2.10mm 0.85mm 0.10mm]
	ElementLine[2.10mm -0.90mm 2.10mm -0.85mm 0.10mm]
)
