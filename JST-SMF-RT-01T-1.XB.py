#!/usr/bin/python
import footgen

f = footgen.Footgen("RT-01T-1.0B")
f.pitch = 1.08
f.pins = 1
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.080
f.generator.diameter = 1.1
f.silkbox(1.5, circle = 2.0, nosides=True)
f.finish

f = footgen.Footgen("RT-01T-1.3B")
f.pitch = 1.38
f.pins = 1
f.generator.clearance = 0.3048
f.generator.mask_clearance = 0.080
f.generator.diameter = 1.4
f.silkbox(1.5, circle = 2.0, nosides=True)
f.generator._add_pin(0,0,"","")
f.finish

f = footgen.Footgen("RT-01T-1.08")
f.pitch = 2.54
f.drill = 1.0
f.diameter = 1.6
f.pins = 1
f.width = 2.54
f.dih()
f.finish()
