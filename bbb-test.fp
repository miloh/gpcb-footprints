# footprint for a bbb - beaglebone black	

Element["" "BBB-footprint" "BBB-footprint" "" 0.00mil 0.00mil 1500.00mil -1000.00mil 0 100 ""]
(
Pin[775mil -1975mil 81mil 39.37mil 84.94mil 42mil "P8" "1" "edge2,square"]
Pin[775mil -175mil 81mil 39.37mil 84.94mil 42mil "P9" "2" "edge2,square"]
Pin[275mil -650mil 81mil 39.37mil 84.94mil 42mil "P6" "3" "edge2,square"]

Pin[3175mil -250mil 120mil 39.37mil 84.94mil 42mil "mount" "3" "edge2"]
Pin[3175mil -1900mil 120mil 39.37mil 84.94mil 42mil "mount" "3" "edge2"]
Pin[575mil -2025mil 120mil 39.37mil 84.94mil 42mil "mount" "3" "edge2"]
Pin[575mil -250mil 120mil 39.37mil 84.94mil 42mil "mount" "3" "edge2"]

ElementLine [250.00mil 0mil 2900.00mil 0.00mil 5.00mil]
ElementLine [3400.00mil -500mil 3400mil -1650mil 5.00mil]
ElementLine [2900.00mil -2150.00mil 200mil -2150mil 5.00mil]

ElementLine [0mil -250mil 0mil -825mil 5.00mil]
ElementLine [0mil -825mil 800mil -825mil 5.00mil]
ElementLine [800mil -825mil 800mil -1525mil 5.00mil]
ElementLine [800mil -1525mil 800mil -1525mil 5.00mil]
ElementLine [800mil -1525mil 200mil -1525mil 5.00mil]
ElementLine [200mil -1525mil 200mil -2150mil 5.00mil]
#
#I forget the format of some of these geda:pcb tags
#ElementArc [rX rY Width Height StartAngle DeltaAngle Thickness]
ElementArc [ 2900mil -500mil 500mil 500mil 90 90 5.0mil] 
ElementArc [ 2900mil -1650mil 500mil 500mil 180 90 5.0mil] 
ElementArc [ 250mil -250mil 250mil 250mil 0 90 5.0mil] 
)
