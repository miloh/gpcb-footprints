#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

# Implements board headers for Molex micro fit 3 connects.
# Micro Fit 3 is a 3mm pitch 5A max crimping wire-2-board and wire-2-wire
# connect system with a LCP (liquid crystal polymer) housing.
# Originally designed for 'glow-wire' heating applications, this connect  
# has found extended life and use in the reprap and desktop 3DP world.
# Following values are from the variety of Molex datasheets at 
# http://www.molex.com/molex/products/listview.jsp?query=43650&offset=0&npp=20&sType=s&fs=&channel=Products&autoNav=1&path=cHome%23%23-1%23%23-1~~ncPCBHEADERS%23%230%23%2381&Itemlist=
#
# The product key for the part is simple:  43650-XXYY
# 43650 is the family of pcb board headers (a project will also require receptacles, and the two types of crimps or terminals for the connector/receptacle pair)
# XX = # of circuits 
# YY = finish and style combined  
# style options:  [pth | smt, right angle | straight, snap-in plastic peg PCB lock | PCB press-fit metal retention clip | pcb polarizing peg | solder tab] 
#
# Molex offers single row headers for these components with 3 (and more) finishes:
# 2.54nm bright Tin contacts/ 1.27nm Tin plated tails
# 0.38nm Gold contacts/ 2.54nm Tin plated tails over 1.27nm Nickel
# 0.76nm Gold contacts/ 1.27nm Tin plated tail over 1.27nm Nickel
# 2.54nm matte Tin contacts/ 1.27nm Tin plated tails
# This product line connects with MicroFit receptacle series 43645
# Note XX0[6-8] are obsolete and discontinued by Molex, all parts used 'snap-in platic pegs

import footgen

# following values are from datasheet
MMF_basename = "Molex-43650-{0}{1}"
MMF_pins = range(2,13)
MMF_style = {'pth, horizontal, snap-in plastic peg PCB lock':[0,1,2,37],'pth, horizontal, PCB press-fit metal retention clip':[3,4,5,59],'smt, horizontal, PCB press-fit metal rentention clip':[9,10,11],'smt, horizontal, solder tab':[12,13,14],'pth, vertical, pcb polarizing peg':[15,16,17],'pth, vertical, PCB press-fit metal retention clip':[18,19,20],'smt, vertical, PCB press-fit metal retention clips':[21,22,23],'smt, vertical, solder tab':[24,25,26]}
MMF_finish = {'tin 2.54nm':0, 'gold, 0.38um':1, 'gold, 0.76mm':2}
# Dimensions will change for the following part groups -- 
MMF_dimA = [9.65,12.65,15.65,18.64,21.64,24.64,27.64,30.63,33.66,36.65,39.65] 
MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
MMF_dimC = [None,None,4.70,7.70,10.70,13.70,16.70,19.70,22.70,25.70,28.70]
for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['pth, horizontal, snap-in plastic peg PCB lock'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.diameter = 2.14
    f.generator.drill = 1.02
    f.generator.options_list = ["circle"]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.153
    f.pitch = 3.00
    f.width = 4.32
    f.height = MMF_dimA[i]
    f.padheight = 1.27
    f.padwidth = 2.54
    #f.box_corners(MMF_dimA[i]/2,-f.width-f.generator.drill,-MMF_dimA[i]/2,4.6)
    f.silk_line(-f.height/2,-f.width,-f.height/2+2.41/2,-f.width)
    f.silk_line(-f.height/2,-f.width+f.generator.drill,-f.height/2,-f.width)
    f.silk_line(f.height/2,-f.width,f.height/2-2.41/2,-f.width)
    f.silk_line(f.height/2,-f.width+f.generator.drill,f.height/2,-f.width)
    f.silk_line(-f.height/2, 4.6, f.height/2, 4.6)
    f.silk_line(-f.height/2, 4.6, -f.height/2, 4.6-f.generator.drill)
    f.silk_line(f.height/2, 4.6, f.height/2, 4.6-f.generator.drill)
    f.silk_diamond(MMF_dimB[i]/2,4.6,0.50,0.20) # pin one marking, at entry 
    #signal pins
    f.rowofpads([0,-f.width],"left",1,f.pins)
    # conditional adds correct no. of snap-in plastic peg mounting holes, per datasheet 
    if MMF_dimC[i] is not None:
      f.add_mount(pin="SNAP-IN" ,x= MMF_dimC[i]/2, y= 0, size= 3.00,pad=3.00)
      f.add_mount(pin="SNAP-IN" ,x= -MMF_dimC[i]/2, y= 0, size= 3.00,pad=3.00)
    if MMF_dimC[i] is None:
      f.add_mount(pin="snap-in",x= 0, y= 0, size= 3.00,pad=3.00)
    f.finish()
MMF_dimA = [9.65,12.65,15.65,18.64,21.64,24.64,27.64,30.63,33.66,36.65,39.65] 
MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
MMF_dimC = [7.30,10.30,13.30,16.30,19.30,22.30,25.30,28.30,31.30,34.30,37.30]
for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['pth, horizontal, PCB press-fit metal retention clip'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.diameter = 2.14
    f.generator.drill = 1.02
    f.generator.options_list = ["circle"]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.153
    f.pitch = 3.00
    f.width = 4.32
    f.height = MMF_dimA[i]
    f.padheight = 1.27
    f.padwidth = 2.54
    f.silk_line(-f.height/2,-f.width,-f.height/2+2.41/2,-f.width)
    f.silk_line(-f.height/2,-f.width+f.generator.drill,-f.height/2,-f.width)
    f.silk_line(f.height/2,-f.width,f.height/2-2.41/2,-f.width)
    f.silk_line(f.height/2,-f.width+f.generator.drill,f.height/2,-f.width)
    f.silk_line(-f.height/2, 4.6, f.height/2, 4.6)
    f.silk_line(-f.height/2, 4.6, -f.height/2, 4.6-f.generator.drill)
    f.silk_line(f.height/2, 4.6, f.height/2, 4.6-f.generator.drill)
    f.silk_diamond(MMF_dimB[i]/2,4.6,.5,.2) # pin one marking,  
    #signal pads
    f.rowofpads([0,-f.width],"left",1,f.pins)
    # Press fit metal retention clips 
    f.add_mount(pin="CLIP" ,x= MMF_dimC[i]/2, y= 0, size= 2.41, pad=2.41)
    f.add_mount(pin="CLIP" ,x= -MMF_dimC[i]/2, y= 0, size= 2.41, pad=2.41)
    f.finish()
MMF_dimA = [9.65,12.65,15.65,18.64,21.64,24.64,27.64,30.63,33.66,36.65,39.65] 
MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
MMF_dimC = [7.30,10.30,13.30,16.30,19.30,22.30,25.30,28.30,31.30,34.30,37.30]
for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt, horizontal, PCB press-fit metal rentention clip'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.153
    f.pitch = 3.00
    f.width = 6.93 
    f.height = MMF_dimA[i]
    f.padheight = 1.27
    f.padwidth = 2.92
    f.silk_line(-f.height/2,-f.width+f.padwidth/2,-f.height/2+2.41/2,-f.width+f.padwidth/2)
    f.silk_line(-f.height/2,-f.width+f.padwidth/2,-f.height/2,-f.width+f.padwidth)
    f.silk_line(f.height/2,-f.width+f.padwidth/2,f.height/2-2.41/2,-f.width+f.padwidth/2)
    f.silk_line(f.height/2,-f.width+f.padwidth/2,f.height/2,-f.width+f.padwidth)
    f.silk_line(-f.height/2, 4.6, f.height/2, 4.6)
    f.silk_line(-f.height/2, 4.6, -f.height/2, 4.6-f.padwidth/2)
    f.silk_line(f.height/2, 4.6, f.height/2, 4.6-f.padwidth/2)
    f.silk_line(f.height/2, 4.6, f.height/2, 4.6-f.padheight)
    f.silk_diamond(MMF_dimB[i]/2,4.6,.5,.2) # pin one marking,  
    #signal pads
    f.rowofpads([0,-f.width+f.padwidth/2],"left",1,f.pins) # note geda pcb's footprint locater diamond is centered w/r/t whole footprint 
    # metal retention clips
    f.add_mount(pin="CLIP" ,x=  MMF_dimC[i]/2, y= 0, size= 2.41, pad=2.41)
    f.add_mount(pin="CLIP" ,x= -MMF_dimC[i]/2, y= 0, size= 2.41, pad=2.41)
    f.finish()
MMF_dimA = [9.65,12.65,15.65,18.65,21.65,24.65,27.65,30.65,33.65,36.65,39.65] 
MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
MMF_dimC = [14.20,17.20,20.20,23.20,26.20,29.20,32.20,35.20,38.20,41.20,44.20]
for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt, horizontal, solder tab'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.153
    f.pitch = 3.00
    f.width = 6.93 
    f.height = MMF_dimA[i]
    f.padheight = 1.27
    f.padwidth = 2.92
    f.silk_line(-f.height/2,-f.width+f.padwidth/2,-f.height/2+2.41/2,-f.width+f.padwidth/2)
    f.silk_line(-f.height/2,-f.width+f.padwidth/2,-f.height/2,-f.width+f.padwidth)
    f.silk_line(f.height/2,-f.width+f.padwidth/2,f.height/2-2.41/2,-f.width+f.padwidth/2)
    f.silk_line(f.height/2,-f.width+f.padwidth/2,f.height/2,-f.width+f.padwidth)
    f.silk_line(-f.height/2, 4.6, f.height/2, 4.6)
    f.silk_line(-f.height/2, 4.6, -f.height/2, 4.6-f.padwidth/2)
    f.silk_line(f.height/2, 4.6, f.height/2, 4.6-f.padwidth/2)
    f.silk_line(f.height/2, 4.6, f.height/2, 4.6-f.padheight)
    f.silk_diamond(MMF_dimB[i]/2,4.6,.5,.2) # pin one marking,  
    #signal pads
    f.rowofpads([0,-f.width+f.padwidth/2],"left",1,f.pins) # note geda pcb's footprint locater diamond is centered w/r/t whole footprint 
    # solder tail gnds on the side 
    f.add_pad("MNT",-MMF_dimC[i]/2 + 3.43/2, 0, 3.43, 1.65) 
    f.add_pad("MNT",MMF_dimC[i]/2  - 3.43/2, 0, 3.43, 1.65) 
    f.finish()
# 15,16,17 missing
MMF_dimA = [9.65,12.65,15.65,18.64,21.64,24.64,27.64,30.63,33.66,36.65,39.65] 
MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
MMF_dimC = [7.30,10.30,13.30,16.30,19.30,22.30,25.30,28.30,31.30,34.30,37.30]
for i in range(len(MMF_pins)):
    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['pth, vertical, PCB press-fit metal retention clip'][MMF_finish['tin 2.54nm']]).zfill(2)))
    f.pins = MMF_pins[i] 
    f.generator.diameter = 1.81
    f.generator.drill = 1.02
    f.generator.options_list = ["circle"]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.153
    f.pitch = 3.00
    f.width = 4.37 
    f.height = MMF_dimA[i]
    f.silk_line(-f.height/2,-1.9,f.height/2,-1.9)
    f.silk_line(-f.height/2,-1.9,-f.height/2,-1.9/2)
    f.silk_line(f.height/2,-1.9,f.height/2,-1.9/2)
    f.silk_line(-f.height/2, 2.47,  f.height/2, 2.47) 
    f.silk_line(-f.height/2, 2.47, -f.height/2, 2.41/2)
    f.silk_line( f.height/2, 2.47,  f.height/2, 2.41/2)
    f.silk_diamond(MMF_dimB[i]/2,2.47,.5,.2) # pin one marking,  
    #signal pads
    f.rowofpads([0,0],"left",1,f.pins)
    # Press fit metal retention clips 
    f.add_mount(pin="CLIP" ,x= -MMF_dimC[i]/2, y= 0, size= 2.41, pad=2.41)
    f.add_mount(pin="CLIP" ,x= +MMF_dimC[i]/2, y= 0, size= 2.41, pad=2.41)
    f.finish()
#21,22,23 missing 
#24,25,26 missing
#for i in range(len(MMF_pins)):
#    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt, vertical, solder tab'][MMF_finish['tin 2.54nm']]).zfill(2)))
#    f.pins = MMF_pins[i] 
#    f.generator.clearance = 0.3048
#    f.generator.mask_clearance = 0.1524
#    f.pitch = 3.00
#    f.width = 2.15+2.54
#    f.height = MMF_dimC[i]
#    f.padheight = 1.27
#    f.padwidth = 2.54
#    f.box_corners(MMF_dimA[i]/2,-f.width,-MMF_dimA[i]/2,1.65/2)
#    f.silk_diamond(MMF_dimB[i]/2,f.width+f.padwidth/2,.5,.2) # pin one marking,  
#    #signal pads
#    f.rowofpads([0,-f.width+f.padwidth/2],"left",1,f.pins)
#    # header case gnds at the back
#    f.add_pad("MNT",-f.height/2 + 3.43/2, 0, 3.43, 1.65) 
#    f.add_pad("MNT",f.height/2  - 3.43/2, 0, 3.43, 1.65) 
#    f.finish()
#
#MMF_dimA = [9.65,12.65,15.65,18.65,21.65,24.65,27.65,30.65,33.65,36.65,39.65] 
#MMF_dimB = [ 3.00,6.00,9.00,12.00,15.00,18.00,21.00,24.00,27.00,30.00,33.00]
#MMF_dimC = [7.30,10.30,13.30,19.30,22.30,25.30,28.30,31.30,34.30,37.30]
#for i in range(len(MMF_pins)):
#    f = footgen.Footgen(MMF_basename.format(str(MMF_pins[i]).zfill(2),str(MMF_style['smt, vertical, PCB press-fit  metal retention clips'][MMF_finish['tin 2.54nm']]).zfill(2)))
#    f.pins = MMF_pins[i] 
#    f.generator.clearance = 0.3048
#    f.generator.mask_clearance = 0.1524
#    f.pitch = 3.00
#    f.width = 2.15+2.54
#    f.height = MMF_dimC[i]
#    f.padheight = 1.27
#    f.padwidth = 2.54
#    f.box_corners(MMF_dimA[i]/2,-f.width,-MMF_dimA[i]/2,1.65/2)
#    f.silk_diamond(MMF_dimB[i]/2,f.width+f.padwidth/2,.5,.2) # pin one marking,  
#    #signal pads
#    f.rowofpads([0,-f.width+f.padwidth/2],"left",1,f.pins)
#    f.add_mount(pin="retention clip" ,x= f.height/2, y= 0, size= 2.41,pad=2.41)
#    f.add_mount(pin="retention clip" ,x= -f.height/2, y= 0, size= 2.41,pad=2.41)
#    f.finish()
#
