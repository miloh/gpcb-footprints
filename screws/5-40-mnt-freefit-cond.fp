Element["" "#5-40 free fit mount, clear mask & poly" "#5-40" "#5-40" 0  0 5000 7500 0 80 ""]
(
#
# 5-40 is a 0.125" imperial screw less apt to get confused with M3 than 4-40
# use 136mil close fit, 140.5mil free fit
#

# insulated clearance from poly + mask to hole edge
     #Pin [0.0000 0.0000 0mil 140.5mil  140.5mil  140.5mil "1" "1" "hole"]
# no clearance from poly
    #Pin [0.0000 0.0000 0mil 0mil  140.5mil  136.0mil "1" "1" "hole"]
# conductor no clearance from poly + mask clears
    Pin [0.0000 0.0000 0mil 0mil  272.0mil  136.0mil "1" "1" "hole"]
     
     ElementArc [0mm 0mm 136.0mil 136.0mil -90 -90 8mil]
     ElementArc [0mm 0mm 136.0mil 136.0mil   0  90 8mil]

        )
