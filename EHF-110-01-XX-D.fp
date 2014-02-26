Element["" "20 pin (2x13) header for Samtec Tigereye EHF/SHF"  "20 pin EHF" "val" 0 0 150mil -200mil 3 100 ""]

# Element [ SFlags "Desc" "Name" "Value" MX MY TX TY TDir Scale TSFlags]

(

# Pin [rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
	Pin[ 50mil 450mil  44mil 5mil 44mil 28mil "1" "1" "square"]
	Pin[ 0mil  450mil  44mil 5mil 44mil 28mil   "2" "2" ""]
	Pin[ 50mil 400mil  44mil 5mil 44mil 28mil   "3" "3" ""]
	Pin[ 0mil  400mil  44mil 5mil 44mil 28mil   "4" "4" ""]
	Pin[ 50mil 350mil  44mil 5mil 44mil 28mil   "5" "5" ""]
	Pin[ 0mil  350mil  44mil 5mil 44mil 28mil   "6" "6" ""]
	Pin[ 50mil 300mil  44mil 5mil 44mil 28mil   "7" "7" ""]
	Pin[ 0mil  300mil  44mil 5mil 44mil 28mil   "8" "8" ""]
	Pin[ 50mil 250mil  44mil 5mil 44mil 28mil   "9" "9" ""]
	Pin[ 0mil  250mil  44mil 5mil 44mil 28mil   "10" "10" ""]
	Pin[ 50mil 200mil  44mil 5mil 44mil 28mil   "11" "11" ""]
	Pin[ 0mil  200mil  44mil 5mil 44mil 28mil   "12" "12" ""]
	Pin[ 50mil 150mil  44mil 5mil 44mil 28mil   "13" "13" ""]
	Pin[ 0mil  150mil  44mil 5mil 44mil 28mil   "14" "14" ""]
	Pin[ 50mil 100mil  44mil 5mil 44mil 28mil   "15" "15" ""]
	Pin[ 0mil  100mil  44mil 5mil 44mil 28mil   "16" "16" ""]
	Pin[ 50mil 50mil  44mil 5mil 44mil 28mil   "17" "17" ""]
	Pin[ 0mil  50mil  44mil 5mil 44mil 28mil   "18" "18" ""]
	Pin[ 50mil 0mil  44mil 5mil 44mil 28mil   "19" "19" ""]
	Pin[ 0mil  0mil  44mil 5mil 44mil 28mil   "20" "20" ""]
	
# reference centerline commented out
	#ElementLine [ -106.50mil 225mil 156.5mil 225mil 5mil]
	
# silk outline for latch orienting tab
	ElementLine [ 123mil 125mil 156.5mil 125mil 5mil]
	ElementLine [ 123mil 125mil 123mil 325mil 5mil]
	ElementLine [ 123mil 325mil 156.5mil 325mil 5mil]

# full part outline (latch unextended)
	ElementLine [ -106.5mil -310mil 89.5mil -310mil 5mil]
# hint line for assembly orientation
	ElementLine [89.5mil -310mil 156.5mil -243mil 5mil] 
	ElementLine [ 156.5mil -243mil 156.5mil 125mil 5mil]
        ElementLine [ 156.5mil 325mil 156.5mil 693mil 5mil]
# hint line for assembly orientation
	ElementLine [156.5mil 693mil 89.5mil 760mil 5mil] 
	ElementLine [89.5mil 760mil -106.5mil 760mil 5mil]

	ElementLine [ -106.5mil 760mil -106.5mil 660mil 5mil]
	ElementLine [ -106.5mil 660mil -86.5mil 660mil 5mil]
	ElementLine [ -86.5mil 660mil -86.5mil -210mil 5mil]
	ElementLine [ -86.5mil -210mil -106.5mil -210mil 5mil]
	ElementLine [ -106.5mil -210mil -106.5mil -310mil 5mil]

# outlines for pin block  
	ElementLine [ -50mil -50mil 100mil -50mil 5mil]
	ElementLine [ 100mil -50mil 100mil 500mil 5mil]  
	ElementLine [ 100mil 500mil -50mil 500mil 5mil]
	ElementLine [ -50mil 500mil -50mil -50mil 5mil]
)
