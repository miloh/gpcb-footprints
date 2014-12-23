#!/usr/bin/python
# R. Miloh Alexander
# Use: unrestricted with attribution

# Implements pcb mount camera sockets from molex 
# standard mobile imaging architecture (SMIA) compliant
# camera sockets 
# these sockets typically come in on-board and through-board designs
# http://www.molex.com/molex/products/family?key=camera_sockets&channel=products&chanName=family&pageTitle=Introduction

import footgen

basename = "Molex-SMIA"
pins = 
style = {}
MMF_finish = {}
# Dimensions will change for the following part groups -- 
for i in range(len(pins)):
    f = footgen.Footgen()
    f.pins = pins[i] 
    f.generator.diameter = 
    f.generator.drill = 
    f.generator.options_list = ["circle"]
    f.generator.clearance = 0.3048
    f.generator.mask_clearance = 0.080
    f.pitch = 
    f.width = 
    f.height = 
    f.padheight = 
    f.padwidth = 
    f.finish()
