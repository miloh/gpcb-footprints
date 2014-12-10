import footgen

f = footgen.Footgen("testpad")
f.generator.clearance = 0.33
f.generator.mask_clearance = 0.080
#f.pins = 10
f.pitch = 10# mm
f.padheight = 1.27 # mm
f.padwidth = 0.5 # mm
print f.generator.drill
print f.pins
print "update values from initialized"
f.generator.drill = 3
f.pins = 5
f.rowofpads([0,0],"left",1,f.pins)
#f.add_pad("shirley",0,1,1.27,0.5)
#f.add_pad("you",0,2,1.27,0.5)
#f.add_pad("are",0,3,1.27,0.5)
#f.add_pad("joking",0,4,1.27,0.5)
f.finish()
