##from:pcb
##for:diode
Element["" "Diodes Inc. BAT760-7" "" "" 48.00mil 43.00mil -20.0mil  -75.0mil 0 50 ""]
(
# Pad[x1, y1, x2, y2, thickness, clearance, mask, name , pad number, flags]
	Pad[ -0.85mm  0
	     -1.55mm  0
	      0.65mm  0.20mm 0.75mm "A" "2" "square"]
	Pad[  1.55mm 0
	      0.85mm 0
	      0.65mm  0.20mm 0.75mm "C" "1" "square"]
	ElementLine[0.40mm -0.35mm 0.40mm 0.35mm 0.10mm]

	ElementLine[-0.90mm -0.65mm 0.90mm -0.65mm 0.10mm]
	ElementLine[-0.90mm -0.65mm -0.90mm -0.60mm 0.10mm]
	ElementLine[0.90mm -0.65mm 0.90mm -0.60mm 0.10mm]
	ElementLine[-0.90mm 0.65mm 0.90mm 0.65mm 0.10mm]
	ElementLine[-0.90mm 0.65mm -0.90mm 0.60mm 0.10mm]
	ElementLine[0.90mm 0.65mm 0.90mm 0.60mm 0.10mm]
)
