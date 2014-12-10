import footgen

f = footgen.Footgen("test-pad")
f.generator.clearance = 0.33
f.generator.mask_clearance = 0.080
f.pitch = 2 # mm
f.padheight = 1.27 # mm
f.padwidth = 0.5 # mm

f.add_pad("shirley",0,1,1.27,0.5)
f.add_pad("you",0,2,1.27,0.5)
f.add_pad("are",0,3,1.27,0.5)
f.add_pad("joking",0,4,1.27,0.5)
f.finish()
