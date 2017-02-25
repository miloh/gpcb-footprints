Element["" "#5-40 close fit mount, clear mask & poly" "#5-40" "#5-40" 0  0 5000 7500 0 80 ""]
(
# 5-40 is a 0.125" imperial screw less apt to get confused with M3 than 4-40
# use 136mil close fit, 140.5mil free fit
# double clearance, possilby insulated from planes poly floods
    Pin [0.0000 0.0000 0mil 136.0mil  136.0mil  136.0mil "1" "1" "hole"]
# no clearance, possibly conduction to planes/poly/floods
    #Pin [0.0000 0.0000 0mil 0mil  136.0mil  136.0mil "1" "1" "hole"]
# no clearance, expanded mask.  likely conduction to planes/poly/floods
    #Pin [0.0000 0.0000 0mil 0mil  272.0mil  136.0mil "1" "1" "hole"]

    ElementArc [0mm 0mm 136.0mil  136.0mil -90 -90 8mil]
    ElementArc [0mm 0mm 136.0mil  136.0mil   0  90 8mil]

        )

