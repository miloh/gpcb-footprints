#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

# Implements board headers for Molex micro fit 3 connects.
# Micro Fit 3 is a 3mm pitch 5A max crimping wire-2-board and wire-2-wire
# connect system with a LCP (liquid crystal polymer) housing.
# Originally designed for 'glow-wire' heating applications, this connect  
# has found extended life and use in the reprap and desktop 3DP world.
# Following values are from Molex datasheet  http://www.molex.com/pdm_docs/sd/436500215_sd.pdf
# the product key for the part is simple:  
# 43650-XXYY
# XX = # of circuits 
# YY = finish and style     
# style options:  pth | smt, right angle | straight, tabbed | notabs, polarizing??
# Molex offers single row headers for these components with 3 (and more) finishes:
# 2.54nm bright Tin contacts/ 1.27nm Tin plated tails
# 0.38nm Gold contacts/ 2.54nm Tin plated tails over 1.27nm Nickel
# 0.76nm Gold contacts/ 1.27nm Tin plated tail over 1.27nm Nickel
# 2.54nm matte Tin contacts/ 1.27nm Tin plated tails
# mates with MicroFit receptacle series 43645

import footgen

# following values are from datasheet
MMF_basename = "Molex-43650-{0}{1}"
MMF_pins = range(2,13)
MMF_style = {'':range(0:8),'smt horizontal tabbed':[9,10,11],'smt horizontal':[12,13,14],'pth vertical tabbed':[15,16,17],'smt vertical tabbed':[21,22,23],'smt vertical notabs':[24,25,26]}
MMF_finish = {'tin 2.54nm':0, 'gold, 38nm':1, 'gold, 76nm':2}
MMF_dimA = [9.65,12.65,15.65,18.65,21.65,24.65,27.65,30.65,33.65,36.65,39.65] 
MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
MMF_dimC = [14.20,17.20,20.20,23.20,26.20,29.20,32.20,35.20,38.20,41.20,44.20]
for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt horizontal'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 3.00
    f.width = 4.37
    f.height = MMF_dimC[i]
    f.padheight = 1.27
    f.padwidth = 2.54
    f.box_corners((f.height+2)/2,f.width/2,-(f.height+2)/2,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+1.0,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-1.0,-(f.width+f.padwidth))
    f.silk_diamond(0,0,.5,.2)
    #signal pads
    f.rowofpads([0,-2.15-2.54/2],"left",1,f.pins)
    # header case gnds at the back
    f.add_pad("MNT",-f.height/2 + 3.43/2, 0  ,3.43,1.65) 
    f.add_pad("MNT",f.height/2  - 3.43/2, 0  ,3.43,1.65) 
    f.finish()

for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt vertical notabs'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 3.00
    f.width = 2.15+2.54
    f.height = MMF_dimC[i]
    f.padheight = 1.27
    f.padwidth = 2.54
    f.box_corners((f.height+2)/2,f.width/2,-(f.height+2)/2,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+1.0,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-1.0,-(f.width+f.padwidth))
    f.silk_diamond(0,0,.5,.2)
    #signal pads
    f.rowofpads([0,-2.15-f.padwidth/2],"left",1,f.pins)
    # header case gnds at the back
    f.add_pad("MNT",-f.height/2 + 3.43/2, 0  ,3.43,1.65) 
    f.add_pad("MNT",f.height/2  - 3.43/2, 0  ,3.43,1.65) 
    f.finish()

for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt vertical tabbed'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 3.00
    f.width = 2.15+2.54
    f.height = MMF_dimC[i]
    f.padheight = 1.27
    f.padwidth = 2.54
    f.box_corners((f.height+2)/2,f.width/2,-(f.height+2)/2,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+1.0,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-1.0,-(f.width+f.padwidth))
    f.silk_diamond(0,0,.5,.2)
    #signal pads
    f.rowofpads([0,-2.15-f.padwidth/2],"left",1,f.pins)
    # header case gnds at the back
    f.add_pad("MNT",-f.height/2 + 3.43/2, 0  ,3.43,1.65) 
    f.add_pad("MNT",f.height/2  - 3.43/2, 0  ,3.43,1.65) 
    f.finish()

for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt horizontal tabbed'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 3.00
    f.width = 2.15+2.54
    f.height = MMF_dimC[i]
    f.padheight = 1.27
    f.padwidth = 2.54
    f.box_corners((f.height+2)/2,f.width/2,-(f.height+2)/2,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+1.0,-(f.width+f.padwidth))
    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-1.0,-(f.width+f.padwidth))
    f.silk_diamond(0,0,.5,.2)
    #signal pads
    f.rowofpads([0,-2.15-f.padwidth/2],"left",1,f.pins)
    # header case gnds at the back
    f.add_pad("MNT",-f.height/2 + 3.43/2, 0  ,3.43,1.65) 
    f.add_pad("MNT",f.height/2  - 3.43/2, 0  ,3.43,1.65) 
    f.finish()
#for i in range(len(MMF_pins)):
#    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['pth vertical'][MMF_finish['tin 2.54nm']]).zfill(2)))
#    f.pins = MMF_pins[i] 
#    f.generator.clearance = 0.3048
#    f.generator.mask_clearance = 0.1524
#    f.pitch = 3.00
#    f.width = 2.15+2.54
#    f.height = MMF_dimC[i]
#    f.padheight = 1.27
#    f.padwidth = 2.54
#    f.box_corners((f.height+2)/2,f.width/2,-(f.height+2)/2,-(f.width+f.padwidth))
#    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch+1.0,-(f.width+f.padwidth))
#    f.silk_line(-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch,-(f.width+f.padwidth/2),-(f.pitch*(f.pins-1))/2+(f.pins-1)*f.pitch-1.0,-(f.width+f.padwidth))
#    f.silk_diamond(0,0,.5,.2)
#    #signal pads
#    f.rowofpads([0,-2.15-f.padwidth/2],"left",1,f.pins)
#    # header case gnds at the back
#    f.add_pad("MNT",-f.height/2 + 3.43/2, 0  ,3.43,1.65) 
#    f.add_pad("MNT",f.height/2  - 3.43/2, 0  ,3.43,1.65) 
#    f.finish()
