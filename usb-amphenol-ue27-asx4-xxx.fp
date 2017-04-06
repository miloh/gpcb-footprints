# Ampehnol USB type A receptacle 
# UE27-ASX4-XXX is a right angle pth 8 stacked pth-signal and 4 pth-mount(boardlock) usb adapter
#
## Element[element_flags, desc., pcb-name, value, mark_x, mark_y,  text_x,text_y, text_direction, text_scale, text_flags]
Element["" "U227-ASX4-XXx" "USB" "" 0 0 5mm -6.6mm 0 100 ""]
(
# Pin        [ rX  rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
# 'boardlock' mounting holes
 Pin[ -6.57mm  -2.97mm  3.30mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
 Pin[  6.57mm  -2.97mm  3.30mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
# rear shell mounts
 Pin[ -6.57mm   2.71mm  3.30mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
 Pin[  6.57mm   2.71mm  3.30mm  0.153mm  2.30mm 2.30mm "mnt" "0" ""]
# signal holes
 Pin[ -3.50mm   0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "1" ""]
 Pin[ -1.00mm   0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "2" ""]
 Pin[  1.00mm   0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "3" ""]
 Pin[  3.50mm   0.00mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "4" ""]
#
 Pin[ -3.50mm -2.62mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "1" ""]
 Pin[ -1.00mm -2.62mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "2" ""]
 Pin[  1.00mm -2.62mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "3" ""]
 Pin[  3.50mm -2.62mm  1.42mm 0.153mm 0.92mm 0.92mm "mnt" "4" ""]
# ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
# body outline is roughly 14.50 x 17.00  
    ElementLine[-5.00mm  -4.01mm  5.00mm  -4.01mm  600]
    ElementLine[-7.25mm   1.01mm -7.25mm  -1.27mm  600]
    ElementLine[-7.25mm  12.99mm -7.25mm   4.41mm  600]
    ElementLine[ 7.25mm   1.01mm  7.25mm  -1.27mm  600]
    ElementLine[ 7.25mm  12.99mm  7.25mm   4.41mm  600]
)
