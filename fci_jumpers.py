import footgen

#Minitek unshrouded HDR
# unshrouded smt headers on a 0.05" pitch
#dimensions from datasheet
#http://portal.fciconnect.com/Comergent//fci/drawing/20021121.pdf
basename = "20021121-X0X0{0}XXLF"
# import numpy for full ranges
# dimN = arange ( 0,65,1.27)
# and use a dict {} with the pos as the key for the dimensions
DIMX = [3.81, 5.08, 6.35]
DIMY = [2.54, 3.81, 5.08]
DIMZ = [1.27, 2.54, 3.81]
pos = range(6,12,2)
for i in range(len(pos)):
    f = footgen.Footgen(basename.format(str(pos[i]).zfill(2)))
    if pos == 100:
        f = footgen.Footgen(basename.format(str(A0)))
    f.generator.clearance = 0.33
    f.generator.mask_clearance = 0.250
    f.pins = pos[i]
    f.pitch = 1.27
    f.padheight = 0.76 # mm
    f.padwidth = 2.40 # mm
    f.width = 6.30 - 2 * f.padwidth
    f.soh()
    f.finish()
