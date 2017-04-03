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
	ElementLine[-2.10mm -0.90mm 2.10mm -0.90mm 0.153mm]
	ElementLine[-2.10mm 0.90mm 2.10mm 0.90mm 0.153mm]
#bitty encaps showing body
	ElementLine[-2.10mm -0.90mm -2.10mm -0.87mm 0.153mm]
	ElementLine[-2.10mm 0.90mm -2.10mm 0.87mm 0.153mm]
	ElementLine[2.10mm 0.90mm 2.10mm 0.87mm 0.153mm]
	ElementLine[2.10mm -0.90mm 2.10mm -0.87mm 0.153mm]
# this is a diode symbol, probably overlaps the part
	ElementLine [-5.00mil 40.00mil -5.00mil 70.00mil 6.00mil]
	ElementLine [-5.00mil 70.00mil 10.00mil 55.00mil 6.00mil]
	ElementLine [10.00mil 55.00mil -5.00mil 40.00mil 6.00mil]
	ElementLine [-25.00mil 55.00mil -5.00mil 55.00mil 6.00mil]
	ElementLine [10.00mil 55.00mil 25.00mil 55.00mil 6.00mil]
	ElementLine [10.00mil 70.00mil 10.00mil 45.00mil 6.00mil]
)
