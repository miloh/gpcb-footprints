# Ampehnol USB type A receptacle 
# UE27-ACX4 is a right angle 4 pth signal and 2 pth mount(boardlock) usb adapter
#
## Element[element_flags, desc., pcb-name, value, mark_x, mark_y,  text_x,text_y, text_direction, text_scale, text_flags]
Element["" "U227-ACX4" "USB" "" 0 0 5mm -6.0mm 0 100 ""]
(
# Pin        [ rX  rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
# 'boardlock' mounting holes
 Pin[ -6.57mm 0mm  3.30mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
 Pin[  6.57mm 0mm  3.30mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
# signal holes
 Pin[ -3.50mm -2.71mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "1" ""]
 Pin[ -1.00mm -2.71mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "2" ""]
 Pin[  1.00mm -2.71mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "3" ""]
 Pin[  3.50mm -2.71mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "4" ""]
# ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
# body outline is roughly 14.50 x 13.85  
    ElementLine[-7.25mm  -3.57mm  7.25mm  -3.57mm  600]
    ElementLine[-7.25mm  10.28mm -7.25mm   1.70mm  600]
    ElementLine[-7.25mm  -1.70mm -7.25mm  -3.57mm  600]
    ElementLine[ 7.25mm  10.28mm  7.25mm   1.70mm  600]
    ElementLine[ 7.25mm  -1.70mm  7.25mm  -3.57mm  600]
)
