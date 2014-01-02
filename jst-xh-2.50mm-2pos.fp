#Author: R. Miloh Alexander
#License: GPL 2.0
#Use: unrestricted with attribution

# Following description is from Harry Eaton's Pcb-1.99z text. 
#Element[SFlags "Desc" "Name" "Value" MX MY TX TY TDir TScale TSFlags] () 
# SFlags = Symbolic or numeric flags, for the element as a whole.
# Nflags = Numeric flags, for the element as a whole
# Desc = the description of the element.  This is one of the three strings
# which can be displayed on the screen.
# Name = the name of the element, usually the reference designator.
# Value = The value of the element
# MX MY The location of the element's mark.  This is the reference point for
# placing the element and its pins and pads
# TX TY the upper left corner of the text (one of the three strins).
# TDir the relative direction of the text.  0 means left to right for an
# unrotated elemetn, 1 means up, 2 left ,3 down.
# TScale Size of the text, as a percentage of the "default size of the font(the
# default font is about 40mils high).  Default is 100(40mils)
# TSFlags symbolic or numeric flags for the text
#

#Element[SFlags "Desc" "Name" "Value" MX MY TX TY TDir TScale TSFlags] () 
Element["" "JST-XH-2.50mm" "B2B-XH-2" "B2B-XH-2"0 0 -2.25mm 3.7mm  0 100 ""]
(
#Pin [rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
Pin [-1.25mm 0mm 81.00mil 39.37mil 84.94mil 42.00mil "1" "1" "square,edge2"]
Pin [1.25mm 0mm 81.00mil 39.37mil 84.94mil 42.00mil "2" "2" "edge2"]
#ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
ElementLine [-3.7mm -2.2mm -3.7mm 3.55mm 10.00mil]
ElementLine [3.7mm -2.2mm 3.7mm 3.55mm 10.00mil]
ElementLine [-3.7mm -2.2mm 3.7mm -2.2mm 10.00mil]
ElementLine [-3.7mm 3.55mm 3.7mm 3.55mm 10.00mil]
)
