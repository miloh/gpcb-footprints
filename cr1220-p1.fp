# ------------------------------------------------------------------
# Element [SFlags "Desc" "Name" "Value" MX MY TX TY Tdir Tscale TSFlags]
# ------------------------------------------------------------------
Element["" "LINXTECHNOLOGIES CR1220 BATTERY HOLDER" "" "BAT-HLD-001" 0mm 0mm -3mm -7mm 0 100 ""]
(
# ------------------------------------------------------------------
    #Pin[x y thickness clearance mask drillholedia name number flags] 
#-------------------------------------------------------------------
    # Right Oval Pin
    Pin [  6.5mm 0.4mm  1.5mm 8mil 1.56mm 0.78mm "POS" "1" "pin"]
    Pin [  6.5mm 0.0mm  1.5mm 8mil 1.56mm 0.78mm "POS" "1" "pin"]
    Pin [  6.5mm -0.4mm  1.5mm 8mil 1.56mm 0.78mm "POS" "1" "pin"]
    # Left Oval pin
    Pin [  -6.5mm -0.4mm 1.5mm 8mil 1.56mm 0.78mm "POS" "1" "pin"]
    Pin [  -6.5mm 0.0mm 1.5mm 8mil 1.56mm 0.78mm "POS" "1" "pin"]
    Pin [  -6.5mm 0.4mm 1.5mm 8mil 1.56mm 0.78mm "POS" "1" "pin"]
    Pad [ 0.00mm 0.00mm  0.00mm 0.00mm 7.5mm 8mil  7.56mm "NEG" "2" ""]

# ------------------------------------------------------------------
# ElementArc [rX rY Width Height StartAngle DeltaAngle Thickness]
# ------------------------------------------------------------------
    ElementArc [0mm 0mm 5.75mm 5.75mm 0 360 200]
    

#   ElementLine[rX1 rY1 rX2 rY2 Thickness]
    
)

