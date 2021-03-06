#Author: R. Miloh Alexander
#License: GPL
#Use: unrestricted with attribution

# 42mil drill for common 0.100" headers
# reducing drillin parts count for TAM-RC project 

Element["" "1x2PIN" "1x2PIN" "1x2PIN" 27.9999mm 196.85mil -39.37mil -118.11mil 0 100 ""]
(
#Pin [rX rY]
Pin [0.0000 0.0000 81.00mil 39.37mil 84.94mil 42.00mil "1" "1" "square,edge2"]
Pin [100.00mil 0.0000 81.00mil 39.37mil 84.94mil 42.00mil "2" "2" "edge2"]
#ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
ElementLine [-49.21mil 49.21mil -49.21mil -49.21mil 10.00mil]
ElementLine [-49.21mil -49.21mil 147.64mil -49.21mil 10.00mil]
ElementLine [147.64mil -49.21mil 147.64mil 49.21mil 10.00mil]
ElementLine [147.64mil 49.21mil -49.21mil 49.21mil 10.00mil]
)
