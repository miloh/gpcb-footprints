#Author: R. Miloh Alexander
#License: public domain
#Use: unrestricted 
# 1206 SMD modified for kelvin connection 4 terminal sym
# Element [ SFlags "Desc" "pcb-name" "value" MX MY TX TY TDir Scale TSFlags](
Element["" "SMT resistor with 4 terminal for kelvin connections" "" "1206-kc" 0 0 -3150 -3150 0 100 ""]
(
# Pad[x1, y1, x2, y2, thickness, clearance, mask, name , pad number, flags]
 	Pad[-1.6mm   0.25mm 
	    -1.6mm  -0.25mm
	     1.4mm 0.20mm  1.5mm "1" "1" "square,"]
 	Pad[ 1.6mm   0.25mm 
	     1.6mm  -0.25mm
	     1.4mm 0.20mm  1.5mm "4" "4" "square,"]
 	Pad[-0.90mm   0mm 
	    -0.90mm   0mm
	      0.30mm 0.15mm  0.34mm "2" "2" ""]
 	Pad[ 0.90mm   0mm 
	     0.90mm   0mm
	      0.30mm 0.15mm  0.34mm "3" "3" ""]
)	
