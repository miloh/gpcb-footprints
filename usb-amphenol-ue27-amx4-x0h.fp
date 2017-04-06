# Ampehnol USB type A receptacle 
# UE27-AMX4-X0H is a right angle smt/pth part 
# 4 smt-signal and 2 pth-mount(boardlock) usb adapter
#
## Element[element_flags, desc., pcb-name, value, mark_x, mark_y,  text_x,text_y, text_direction, text_scale, text_flags]
Element["" "UE27-AMX4-X0H" "USB" "" 0 0 5mm -6.0mm 0 100 ""]
(
# Pin        [ rX  rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
# 'boardlock' mounting holes
 Pin[ -6.57mm 0mm  3.90mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
 Pin[  6.57mm 0mm  3.90mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
# Pad        [ x1 y1 x2 y2 thickness clear mask "name" "pad_number" sflags]
# signal pads 
 Pad[ -3.5mm -4.46mm -3.5mm  -2.70mm  1.12mm 0.153mm 2.171mm "" "1" "square"]
 Pad[ -1.0mm -4.46mm -1.0mm  -2.70mm  1.12mm 0.153mm 2.171mm "" "2" "square"]
 Pad[  1.0mm -4.46mm  1.0mm  -2.70mm  1.12mm 0.153mm 2.171mm "" "3" "square"]
 Pad[  3.5mm -4.46mm  3.5mm  -2.70mm  1.12mm 0.153mm 1.171mm "" "4" "square"]
# ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
# body outline is roughly 14.50 x 13.85  
    ElementLine[-7.25mm  -3.72mm -4.65mm  -3.72mm  600]
    ElementLine[ 7.25mm  -3.72mm  4.65mm  -3.72mm  600]
    ElementLine[-7.25mm  10.28mm -7.25mm   2.30mm  600]
    ElementLine[-7.25mm  -2.30mm -7.25mm  -3.72mm  600]
    ElementLine[ 7.25mm  10.28mm  7.25mm   2.30mm  600]
    ElementLine[ 7.25mm  -2.30mm  7.25mm  -3.72mm  600]
)
