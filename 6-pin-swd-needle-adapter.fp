#Author: R. Miloh Alexander
#License: 
#Use: unrestricted with attribution

# 6 pin needle adapter for swd (serial wire debug) programming of arm targets
# this is a footprint for tag-connect needle programmers, which are also used in segger products
# unit base is mils

Element["" "6pin needle adapter" "6pinneedleadapter" "6pinneedleadpaetr" 200mil  200mil -100mil -100mil0 100 ""]
(
	# Pin [rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
	Pin [-100.00mil  -100.00mil 93.50mil 25.00mil 93.50mil 93.50mil "x" "x" ""]
	Pin [25.00mil    -100.00mil 93.50mil 39.37mil 93.50mil 93.50mil "x" "x" ""]
	Pin [-100.00mil   100.00mil 93.50mil 39.37mil 93.50mil 93.50mil "x" "x" ""]
	Pin [25.00mil     100.00mil 93.50mil 39.37mil 93.50mil 93.50mil "x" "x" ""]
	
	Pin [-100.00mil   0.00mil 39.0mil  40.00mil 39.00mil 39.00mil "1" "1" ""]
	Pin [ 100.00mil -40.0mil 39.00mil 40.00mil 39.00mil 39.00mil "1" "1" ""]
	Pin [ 100.00mil  40.0mil 39.00mil 40.00mil 39.00mil 39.00mil "1" "1" ""]

	Pad [-50.0mil  25.0mil -50.0mil  25.0mil  31.00mil 20.0mil 35.0mil "1" "1" ""]
	Pad [-50.0mil -25.0mil -50.0mil -25.0mil  31.00mil 20.0mil 35.0mil "2" "2" ""]
	Pad [ 0.00mil  25.0mil  0.00mil  25.0mil  31.00mil 20.0mil 35.0mil "3" "3" ""]
	Pad [ 0.00mil -25.0mil  0.00mil -25.0mil  31.00mil 20.0mil 35.0mil "4" "4" ""]
	Pad [50.00mil  25.0mil 50.00mil  25.0mil  31.00mil 20.0mil 35.0mil "5" "5" ""]
	Pad [50.00mil -25.0mil 50.00mil -25.0mil  31.00mil 20.0mil 35.0mil "6" "6" ""]

	#ElementLine [100.00mil 100.00mil 300.00mil 100.00mil 10.00mil]
	#ElementLine [300.00mil 100.00mil 300.00mil 300.00mil 10.00mil]
	#ElementLine [300.00mil 300.00mil 100.00mil 300.00mil 10.00mil]
	#ElementLine [100.00mil 300.00mil 100.00mil 100.00mil 10.00mil]

	)
