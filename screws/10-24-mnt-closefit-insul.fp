Element["" "#10-24 close fit mount, clear mask & poly" "#10-24" "#10-24" 0  0 5000 7500 0 80 ""]
(
# 10-24 is a 0.19" imperial screw with coarse threading compared to 10-32
# per a clearance chart, use 0.1960 for close fit and 0.2010 for free fit

    # insulated clearance from poly + mask to hole edge
     Pin [0.0000 0.0000 0mil 196.0mil  196.0mil  196.0mil "1" "1" "hole"]
     # no clearance from poly
    #Pin [0.0000 0.0000 0mil 0mil  196.0mil  196.0mil "1" "1" "hole"]
    # conductor no clearance from poly + mask clears
    #Pin [0.0000 0.0000 0mil 0mil  392.0mil  196.0mil "1" "1" "hole"]
     
     ElementArc [0mm 0mm 196.0mil 196.0mil -90 -90 8mil]
     ElementArc [0mm 0mm 196.0mil 196.0mil   0  90 8mil]
        )
