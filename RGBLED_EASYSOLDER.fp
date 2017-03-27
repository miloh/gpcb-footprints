# $Id: led_5x2mm.fp,v 1.1 2009/02/25 23:07:21 alexander_kurz Exp $
Element["" "5MM CA RGBLED EASY SOLDER" "RGBLED-CA " "" 26575 15000 5500 -16500 0 100 ""]
(
       #Pin[ rX  rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
	Pin[ 1.95mm  0.0mm 1.10mm 0.30mm 1.3mm 0.70mm "1" "1" ""]
	Pin[ 0.65mm  0.0mm 1.10mm 0.30mm 1.3mm 0.70mm "2" "2" ""]
	Pin[-0.65mm  0.0mm 1.10mm 0.30mm 1.3mm 0.70mm "3" "3" ""]
	Pin[-1.95mm  0.0mm 1.10mm 0.30mm 1.3mm 0.70mm "4" "4" ""]
       #Pad[ x1 y1 x2 y2 thickness clear mask "name" "pad_number" sflags]
        Pad[ 1.95mm  0.05mm  1.95mm -1.10mm 1.10mm 0.30mm 1.2mm "1" "1" "onsolder"]
        Pad[ 0.65mm  -0.05mm 0.65mm 1.10mm 1.10mm 0.30mm 1.2mm "2" "2" "onsolder"]
        Pad[-0.65mm  0.05mm -0.65mm -1.10mm 1.10mm 0.30mm 1.2mm "3" "3" "onsolder"]
        Pad[-1.95mm  -0.05mm -1.95mm 1.10mm 1.10mm 0.30mm 1.2mm "4" "4" "onsolder"]
	# the element box
        #ElementArc [ rX rY Width Height StartAngle DeltaAngle Thickness]
	ElementArc [0 0 3.1mm 3.1mm 205 310 500]
	ElementArc [0 0 3.3mm 3.3mm 205 310 500]
        #ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
        ElementLine [ 2.8096mm -1.3101mm 2.8096mm 1.3101mm 500]
        ElementLine [ 2.991mm -1.395mm 2.991mm 1.395mm 500]

	
	)

