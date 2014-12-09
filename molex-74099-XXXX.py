#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

import footgen


# Molex SDA-74099 family of SMT 0.1" pitch pcb headers
# implements SMT vertical (top) entry type only!!! 
# following values are from datasheet "740990604_sd.pdf
# all units mm

molex_74099_basename = "Molex-74099-06{0}"
molex_74099_pins = [3,4,5,6,7,8,9,10,11,12,22] # more pins in the complete sheet 
molex_74099_dimA = [8.13,10.67,13.21,15.75,18.29,20.83,23.37,25.91,28.45,30.99,56.39] 
molex_74099_dimB = [5.08,7.62,10.16,12.70,15.24,17.78,20.32,22.86,25.40,27.94,53.34]
molex_74099_dimC = [0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.18]
contact_finish = {'tin 2.54nm':0, 'gold, 0.38um':20, 'gold, 0.76mm':40}
#tin = [molex_74099_pins]
#38um_gold = [molex_74099_pins+20]
#76um_gold = [molex_74099_pins+40]
for i in range(len(molex_74099_pins)):
    f = footgen.Footgen(molex_74099_basename.format(str(molex_74099_pins[i]).zfill(2))) 
    f.pins = molex_74099_pins[i] 
    f.height = molex_74099_dimA[i]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.1524
    f.pitch = 2.54
    f.width = 6.60
    rowlen = molex_74099_dimB[i]
    inner_width = 5.08
    notch_width = 1.52
    f.padheight = 1.27
    f.padwidth = 3.18 
    f.silk_line(f.height/2,inner_width/2,rowlen/2,inner_width/2)
    f.silk_line(-f.height/2,inner_width/2,-f.height/2+0.5,inner_width/2)
    f.silk_line(f.height/2,inner_width/2,f.height/2,-inner_width/2)
    f.silk_line(f.height/2,-inner_width/2,f.height/2-0.5,-inner_width/2 )
    if not f.pins % 2:
        f.silk_line(-rowlen/2,-inner_width/2-notch_width,-rowlen/2+0.5,-inner_width/2-notch_width )
        f.silk_line(-rowlen/2,-inner_width/2,-rowlen/2,-inner_width/2-notch_width)
        f.silk_line(-f.height/2,-inner_width/2,-rowlen/2,-inner_width/2 )
    if f.pins % 2:
        f.silk_line(-f.height/2,-inner_width/2,-f.height/2+0.5,-inner_width/2 )
    f.silk_line(-f.height/2,-inner_width/2,-f.height/2,inner_width/2)
    x = rowlen * 0.5
    y_offset = 1.02
# this smt part's contact pads use staggared spacing 
# generate arrays of odds and evens for the contact rows
    for i in range(1,f.pins+1):
        if  i % 2:
            f.add_pad(str(i),x,-y_offset-f.padwidth/2,f.padheight,f.padwidth)
        if not i % 2:
            f.add_pad(str(i),x,+y_offset+f.padwidth/2,f.padheight,f.padwidth)
        x = x - f.pitch
    f.silk_diamond(rowlen*0.5,-(y_offset*2.5+f.padwidth),0.2,0.10) # pad one indicator
    f.finish()
