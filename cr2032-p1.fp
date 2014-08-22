# ------------------------------------------------------------------
# Element [SFlags "Desc" "Name" "Value" MX MY TX TY Tdir Tscale TSFlags]
# ------------------------------------------------------------------
Element["" "LINXTECHNOLOGIES CR2032 BATTERY HOLDER" "BAT-HLD-001" "BAT-HLD-001" 0mm 0mm -3mm -7mm 0 100 ""]
(
# ------------------------------------------------------------------
# Pad[      rX1   rY1   rX2  rY2   Thickn  Clr   Msk   Nm Nr     Fl  ]
#-------------------------------------------------------------------
    Pad [ -11.45mm 1.3mm  -11.45mm -1.3mm 2.5mm 8mil  2.70mm "MNTPAD" "1" "square"]
    Pad [  11.45mm 1.3mm  11.45mm -1.3mm 2.5mm 8mil  2.70mm "MNTPAD" "1" "square"]
    Pad [ 0.00mm 0.00mm  0.00mm 0.00mm 8.9mm 8mil  9.05mm "MNTPAD" "1" ""]

# ------------------------------------------------------------------
# ElementArc [rX rY Width Height StartAngle DeltaAngle Thickness]
# ------------------------------------------------------------------
    ElementArc [0mm 0mm 8.9mm 8.9mm 0 360 150]
    

#   ElementLine[rX1 rY1 rX2 rY2 Thickness]
    
    ElementLine [10.55mm 3.00mm 10.55mm 7.35mm 1500]
    ElementLine [10.55mm -3.00mm 10.55mm -7.35mm 1500]
    ElementLine [-10.55mm 3.00mm -10.55mm 7.35mm 1500]
    ElementLine [-10.55mm -3.00mm -10.55mm -7.35mm 1500]
)

