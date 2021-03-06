# ------------------------------------------------------------------
# Element [SFlags "Desc" "Name" "Value" MX MY TX TY Tdir Tscale TSFlags]
# ------------------------------------------------------------------
Element["" "WS2812-PLCC6" "" "" 1000 1000 0nm -1000000nm 0 100 ""]
(
# ------------------------------------------------------------------
# Pad[      rX1   rY1   rX2  rY2   Thickn  Clr   Msk   Nm Nr     Fl  ]
#-------------------------------------------------------------------
	Pad[-2750000nm -1600000nm -2150000nm -1600000nm 900000nm 408000nm 980000nm "1" "1" "square"]
	Pad[-2750000nm 0nm -2150000nm 0nm 900000nm 408000nm 980000nm "2" "2" "square"]
	Pad[-2750000nm 1600000nm -2150000nm 1600000nm 900000nm 408000nm 980000nm "3" "3" "square"]
	Pad[2150000nm 1600000nm 2750000nm 1600000nm 900000nm 408000nm 980000nm "4" "4" "square"]
	Pad[2150000nm 0nm 2750000nm 0nm 900000nm 408000nm 980000nm "5" "5" "square"]
	Pad[2150000nm -1600000nm 2750000nm -1600000nm 900000nm 408000nm 980000nm "6" "6" "square"]
	ElementLine [-3950000nm -2750000nm -3700000nm -2500000nm 155000nm]
	ElementLine [-3950000nm -2750000nm -3700000nm -3000000nm 155000nm]
	ElementLine [-3450000nm -2750000nm -3700000nm -2500000nm 155000nm]
	ElementLine [-3450000nm -2750000nm -3700000nm -3000000nm 155000nm]
	ElementLine [-3450000nm -2500000nm -3450000nm 40000nm 155000nm]
	ElementLine [-3450000nm -2500000nm -1160000nm -2500000nm 155000nm]
	ElementLine [-3450000nm 2500000nm -3450000nm -40000nm 155000nm]
	ElementLine [-3450000nm 2500000nm -1160000nm 2500000nm 155000nm]
	ElementLine [3450000nm -2500000nm 1160000nm -2500000nm 155000nm]
	ElementLine [3450000nm -2500000nm 3450000nm 40000nm 155000nm]
	ElementLine [3450000nm 2500000nm 1160000nm 2500000nm 155000nm]
	ElementLine [3450000nm 2500000nm 3450000nm -40000nm 155000nm]
)
