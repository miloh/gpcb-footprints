
# release: pcb 1.99z

# To read pcb files, the pcb version (or the git source date) must be >= the file version
# rma

# Element[element_flags, description, pcb-name, value, mark_x, mark_y, text_x, text_y, text_direction, text_scale, text_flags
Element["" "0.50mil pitch 3 connection header" "" "0500SIP3" 1000 1000 110.00mil -40.00mil 3 100 ""]
(

# Pin [rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
	Pin[-5000  0.0000 46.00mil 12.00mil 52.00mil 0.69mm "1" "1" ""]
	Pin[    0  0.0000 46.00mil 12.00mil 52.00mil 0.69mm "2" "2" ""]
	Pin[ 5000  0.0000 46.00mil 12.00mil 52.00mil 0.69mm "3" "3" ""]
	#ElementLine [-50.00mil 0.0000 -50.00mil 0.0000 20.00mil]
	#ElementLine [-0.00mil 0.0000 50.00mil 0.0000 20.00mil]
	#ElementLine [-50.00mil 50.00mil 50.00mil 50.00mil 10.00mil]
	#ElementArc [0.0000 0.0000 50.00mil 50.00mil 180 180 20.00mil]
#ElementArc[rX rY Width Height StartAngle DeltaAngle Thickness]  

	ElementArc [-5000 0 30.00mil 30.00mil  220   280  6.00mil]
	ElementArc [    0 0 30.00mil 30.00mil  322.5  -105  6.00mil]
	ElementArc [    0 0 30.00mil 30.00mil  37.5  105  6.00mil]
	ElementArc [ 5000 0 30.00mil 30.00mil  40    280  6.00mil]

	)
