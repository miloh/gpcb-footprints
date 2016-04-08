# ------------------------------------------------------------------
# Element [SFlags "Desc" "Name" "Value" MX MY TX TY Tdir Tscale TSFlags]
# ------------------------------------------------------------------
Element["" "muRATA AUDIO ALERTER ENCLOSED PIEZO" "KM13EPYH4000" "" 0mm 0mm -3mm -7mm 0 100 ""]
(
# ------------------------------------------------------------------
    #Pin[x y thickness clearance mask drillholedia name number flags] 
#-------------------------------------------------------------------
# pins
    Pin [  -2.5mm 0mm  3.1mm 10mil 2.9mm 2.6mm "POS" "1" "pin"]
    Pin [  2.5mm 0mm  3.1mm 10mil 2.9mm 2.6mm "NEG" "2" "pin"]
    #Pin [  2.5mm 0mm  0.7mm 10mil 2.9mm 0.6mm "POS" "1" "pin"]
    #Pin [ - 2.5mm 0mm  0.7mm 10mil 2.9mm 0.6mm "NEG" "2" "pin"]
# locating tabs -- should be "hole" flag 
    Pin [  0mm 3.5mm  0mm 0.1mm 1.0mm 1.0mm "" "" "hole"]
    Pin [  0mm -3.5mm 0mm 0.1mm 1.0mm 1.0mm "" "" "hole"]
# ------------------------------------------------------------------
#Arc [X Y Width Height Thickness Clearance StartAngle DeltaAngle SFlags]
# ------------------------------------------------------------------
    #Arc [ -6.5mm 2.5mm 0.4mm 0.4mm 1.5mm 0mm 0 360 ""]
# ------------------------------------------------------------------
# ElementArc [rX rY Width Height StartAngle DeltaAngle Thickness]
# ------------------------------------------------------------------
    ElementArc [0mm 0mm 6.3mm 6.3mm 0 360 200]
    ElementArc [0mm 0mm 6.0mm 6.0mm 0 360 200]
    

#   ElementLine[rX1 rY1 rX2 rY2 Thickness]
    
)

