# Ampehnol USB type A receptacle 
# UE27-ACX4 is a straight down pth 4 pth-signal and 2 pth-mount(boardlock) usb adapter
#
## Element[element_flags, desc., pcb-name, value, mark_x, mark_y,  text_x,text_y, text_direction, text_scale, text_flags]
Element["" "UE27-AEX4-X0X" "USB" "" 0 0 5mm -6.0mm 0 100 ""]
(
# Pin        [ rX  rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
# 'boardlock' mounting holes
 Pin[ -6.57mm 2.71mm  3.90mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
 Pin[  6.57mm 2.71mm  3.90mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
# signal holes
 Pin[ -3.50mm  0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "1" ""]
 Pin[ -1.00mm  0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "2" ""]
 Pin[  1.00mm  0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "3" ""]
 Pin[  3.50mm  0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "4" ""]
# ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
    ElementLine[-7.25mm  -3.45mm  7.25mm  -3.45mm  600]
    ElementLine[-4.00mm   3.45mm  4.00mm   3.45mm  600]
    ElementLine[-7.25mm   0.45mm -7.25mm  -3.45mm  600]
    ElementLine[ 7.25mm   0.45mm  7.25mm  -3.45mm  600]
)
