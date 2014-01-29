Element["" "molex_microfit3.0_436500415" "" "Val" 10 10 0 0 3 100 ""]
(
# 	Pin[rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]

# 	0.052inch drill  is 1.321mm and corresponds to #55 bit
	Pin[ -1.96mm -7500000nm 54mil 15mil 55mil 52mil "mount" "mount" ""]

# 	0.043inch is 1.092mm and corresponds to #57 bit
	Pin[ 0nm -4500000nm 95mil 18mil 75mil 43mil "4" "4" ""]
	Pin[ 0nm -1500000nm 95mil 18mil 75mil 43mil "3" "3" ""]
	Pin[ 0nm 1500000nm  95mil 18mil 75mil 43mil "2" "2" ""]
	Pin[ 0nm 4500000nm  95mil 18mil 75mil 43mil  "1" "1" "square, edge2"]

# 	0.052inch drill  is 1.321mm and corresponds to #55 bit
	Pin[ -1.96mm  7500000nm 54mil 15mil 55mil 52mil "mount" "mount" ""]

# Body Outline
	ElementLine [-2.545mm -8.0953mm 2.185mm -8.0953mm 6mil]
	ElementLine [2.185mm -8.0953mm 2.185mm  8.0953mm 6mil]
	ElementLine [2.185mm  8.0953mm -2.545mm  8.0953mm 6mil]
	ElementLine [-2.545mm  8.0953mm -2.545mm -8.0953mm 6mil]
# Pin Outlines
	ElementLine [-1500000nm -6000000nm 1500000nm -6000000nm 6mil]
	ElementLine [1500000nm -6000000nm 1500000nm 6000000nm 6mil]
	ElementLine [1500000nm 6000000nm -1500000nm 6000000nm 6mil]
	ElementLine [-1500000nm 6000000nm -1500000nm -6000000nm 6mil]
# First Pin Marker
	ElementLine [1500000nm -3000000nm -1500000nm -3000000nm 6mil]
# Latch Outline
	ElementLine [3.385mm -1.5mm 3.385mm 1.5mm 6mil]
	ElementLine [2.185mm 1.5mm 3.385mm  1.5mm 6mil]
	ElementLine [2.185mm -1.5mm 3.385mm -1.5mm 6mil]
)

