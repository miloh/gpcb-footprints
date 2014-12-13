# ------------------------------------------------------------------
# Element [SFlags "Desc" "Name" "Value" MX MY TX TY Tdir Tscale TSFlags]
# ------------------------------------------------------------------
Element[ "" "SOJ 4 PIN" "" "SOJ-4" 500 500 0 500 0 100 ""]
(
# ------------------------------------------------------------------
# Pad[      rX1   rY1   rX2  rY2   Thickn  Clr   Msk   Nm Nr     Fl  ]
#-------------------------------------------------------------------

Pad[-2.75mm 1.30mm -2.75mm 1.90mm  1.3mm  0.25mm 1.90mm "1" "1" "square"]
Pad[2.75mm 1.30mm 2.75mm 1.90mm  1.3mm  0.25mm 1.90mm "2" "2" "square"]
Pad[2.75mm -1.30mm 2.75mm -1.90mm 1.3mm  0.25mm 1.90mm "3" "3" "square"]
Pad[-2.75mm -1.30mm -2.75mm -1.90mm  1.3mm  0.25mm 1.90mm "4" "4" "square"]
# ------------------------------------------------------------------
# ElementArc [rX rY Width Height StartAngle DeltaAngle Thickness]
ElementArc [-4.5mm 1.6mm 0 -0  0  6.28 15mil ]
# ------------------------------------------------------------------
#   ElementLine[rX1 rY1 rX2 rY2 Thickness]
ElementLine[-0.5mm 0mm   0.5mm  0mm     0.125mm  ]
ElementLine[0mm   0.5mm 0mm   -0.5mm   0.125mm  ]

ElementLine[-3.65mm 2.75mm -3.65mm -2.75mm 0.125mm  ]
ElementLine[-3.65mm -2.75mm 3.65mm -2.75mm 0.125mm  ]
ElementLine[3.65mm -2.75mm 3.65mm 2.75mm 0.125mm  ]
ElementLine[3.65mm 2.75mm -3.65mm 2.75mm 0.125mm  ]
)

