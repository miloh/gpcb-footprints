# element_flags, description, pcb-name, value, mark_x, mark_y,
# text_x, text_y, text_direction, text_scale, text_flags
Element["" "Standard SMT resistor, capacitor etc" "" "0603" 0 0 -3150 -3150 0 100 ""]
(
# 
# Pad[x1, y1, x2, y2, thickness, clearance, mask, name , pad number, flags]
	Pad[-2559 -492
		-2559 492
		2952 2000 3552 "A" "1" "square"]
	    Pad[2559 -492
		2559 492
		2952 2000 3552 "K" "2" "square"]
	# - sign
	ElementLine [-25.00mil -35.00mil -45.00mil -35.00mil 6.00mil]
	# this is a diode symbol, probably overlaps the part
	#ElementLine [-5.00mil 25.00mil -5.00mil 55.00mil 6.00mil]
	#ElementLine [-5.00mil 55.00mil 10.00mil 40.00mil 6.00mil]
	#ElementLine [10.00mil 40.00mil -5.00mil 25.00mil 6.00mil]
	#ElementLine [-25.00mil 40.00mil -5.00mil 40.00mil 6.00mil]
	#ElementLine [10.00mil 40.00mil 25.00mil 40.00mil 6.00mil]
	#ElementLine [10.00mil 55.00mil 10.00mil 25.00mil 6.00mil]
	#ElementLine [15.00mil 5.00mil 15.00mil 5.00mil 0.08mil]
	# this is a +  sign
	ElementLine [25.00mil -35.00mil 45.00mil -35.00mil 6.00mil]
	ElementLine [-35.00mil -45.00mil -35.00mil -25.00mil 6.00mil]
)
