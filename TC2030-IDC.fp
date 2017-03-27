#Author: R. Miloh Alexander
#License: 
#Use: unrestricted with attribution

# 6 pin needle adapter for swd (serial wire debug) programming of arm targets
# this is a footprint for tag-connect needle programmers, which are also used in segger products
# unit base is mils

# Element [ element-flags desc.  pcb-name value .... ]
Element[ "" "Tag Connect 6 pin needle programming adpater" "TC2030-IDC"  "" 2000mil  200mil 120mil 150mil 1 60""]
(
	# Pin [rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
	Pin [-100.00mil  -100.00mil 93.50mil 10.00mil 98.50mil 93.50mil "" "" ""]
	Pin [25.00mil    -100.00mil 93.50mil 10.00mil 98.50mil 93.50mil "" "" ""]
	Pin [-100.00mil   100.00mil 93.50mil 10.00mil 98.50mil 93.50mil "" "" ""]
	Pin [25.00mil     100.00mil 93.50mil 10.00mil 98.50mil 93.50mil "" "" ""]
	
	Pin [-100.00mil   0.00mil 39.0mil 10.00mil 43.00mil 39.00mil "" "" ""]
	Pin [ 100.00mil -40.0mil 39.00mil 10.00mil 43.00mil 39.00mil "" "" ""]
	Pin [ 100.00mil  40.0mil 39.00mil 10.00mil 43.00mil 39.00mil "" "" ""]

	# Pad [ x1 y1 x2 y2 thickness clear mask "name" "pad_number" sflags]
	Pad [-50.0mil  25.0mil -50.0mil  25.0mil  31.00mil 20.0mil 35.0mil "1" "1" ""]
	Pad [-50.0mil -25.0mil -50.0mil -25.0mil  31.00mil 20.0mil 35.0mil "2" "2" ""]
	Pad [ 0.00mil  25.0mil  0.00mil  25.0mil  31.00mil 20.0mil 35.0mil "3" "3" ""]
	Pad [ 0.00mil -25.0mil  0.00mil -25.0mil  31.00mil 20.0mil 35.0mil "4" "4" ""]
	Pad [50.00mil  25.0mil 50.00mil  25.0mil  31.00mil 20.0mil 35.0mil "5" "5" ""]
	Pad [50.00mil -25.0mil 50.00mil -25.0mil  31.00mil 20.0mil 35.0mil "6" "6" ""]

	ElementLine [-160.00mil -160.00mil 150.00mil -160.00mil 10.00mil]
	ElementLine [150.00mil -160.00mil 150.00mil 160.00mil 10.00mil]
	ElementLine [150.00mil 160.00mil -160.00mil 160.00mil 10.00mil]
	ElementLine [-160.00mil 160.00mil -160.00mil -160.00mil 10.00mil]

	)
