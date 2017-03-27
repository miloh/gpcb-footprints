# element_flags, description, pcb-name, value, mark_x, mark_y,
# text_x, text_y, text_direction, text_scale, text_flags
Element["" "0402 with polarity mark" "" "" 48.00mil 43.00mil -20.0mil  -75.0mil 0 50 ""]
(
# 
# Pad[x1, y1, x2, y2, thickness, clearance, mask, name , pad number, flags]
	Pad[-15.74mil -2.83mil -15.74mil 5.03mil 19.68mil 20.00mil 39.68mil "1" "1" "square"]
	Pad[15.74mil -2.83mil 15.74mil 5.03mil 19.68mil 20.00mil 39.68mil "2" "2" "square"]
# ElementLine [x1 y1 x2 y2 line-thickness]	
	# - sign
	ElementLine [-25.00mil -30.00mil -45.00mil -30.00mil 6.00mil]
	# Diode symbol
	ElementLine [-5.00mil 25.00mil -5.00mil 55.00mil 6.00mil]
	ElementLine [-5.00mil 55.00mil 10.00mil 40.00mil 6.00mil]
	ElementLine [10.00mil 40.00mil -5.00mil 25.00mil 6.00mil]
	ElementLine [-25.00mil 40.00mil -5.00mil 40.00mil 6.00mil]
	ElementLine [10.00mil 40.00mil 25.00mil 40.00mil 6.00mil]
	ElementLine [10.00mil 55.00mil 10.00mil 25.00mil 6.00mil]
	ElementLine [15.00mil 5.00mil 15.00mil 5.00mil 0.08mil]
	# + sign
	ElementLine [25.00mil -30.00mil 45.00mil -30.00mil 6.00mil]
	ElementLine [-35.00mil -40.00mil -35.00mil -20.00mil 6.00mil]

	)
