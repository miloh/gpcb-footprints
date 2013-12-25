
Element["" "Molex_705534038" "" "" 10.00mil 10.00mil 0.0000 0.0000 3 100 ""]
(
	Pin[0.0000 -150.00mil 71.00mil 10.00mil 66.00mil 43.00mil "1" "1" "square"]
	Pin[0.0000 -50.00mil 71.00mil 10.00mil 66.00mil 43.00mil "2" "2" ""]
	Pin[0.0000 50.00mil 71.00mil 10.00mil 66.00mil 43.00mil "3" "3" ""]
	Pin[0.0000 150.00mil 71.00mil 10.00mil 66.00mil 43.00mil "4" "4" ""]

	ElementLine [-42.00mil -192.00mil 42.00mil -192.00mil 6.00mil]
	ElementLine [42.00mil -192.00mil 42.00mil -108.00mil 6.00mil]
	ElementLine [42.00mil -108.00mil -42.00mil -108.00mil 6.00mil]
	ElementLine [-42.00mil -108.00mil -42.00mil -192.00mil 6.00mil]
	ElementLine [-42.00mil -92.00mil 42.00mil -92.00mil 6.00mil]
	ElementLine [42.00mil -92.00mil 42.00mil -8.00mil 6.00mil]
	ElementLine [42.00mil -8.00mil -42.00mil -8.00mil 6.00mil]
	ElementLine [-42.00mil -8.00mil -42.00mil -92.00mil 6.00mil]
	ElementLine [-42.00mil 8.00mil 42.00mil 8.00mil 6.00mil]
	ElementLine [42.00mil 8.00mil 42.00mil 92.00mil 6.00mil]
	ElementLine [42.00mil 92.00mil -42.00mil 92.00mil 6.00mil]
	ElementLine [-42.00mil 92.00mil -42.00mil 8.00mil 6.00mil]
	ElementLine [-42.00mil 108.00mil 42.00mil 108.00mil 6.00mil]
	ElementLine [42.00mil 108.00mil 42.00mil 192.00mil 6.00mil]
	ElementLine [42.00mil 192.00mil -42.00mil 192.00mil 6.00mil]
	ElementLine [-42.00mil 192.00mil -42.00mil 108.00mil 6.00mil]

## cross shape defines outline of straight angle 2ckt SL connect
## Dimension "A" from 705430036_sd.pdf  0.300" for 4 CKT
#ElementLine [-5.00mil -150.00mil -5.00mil 150.00mil 6.00mil]
## Dimension "B" from 705430036_sd.pdf  0.420" for 4 CKT
#ElementLine [5.00mil -210.00mil 5.00mil 210.00mil 6.00mil]
# Add in typ. wall thickness of 40mils on either side of "B"
#ElementLine [0.00mil -250.00mil 0.00mil 250.00mil 6.00mil]

# outline of part using the above guidlines
ElementLine [-100.00mil -250.00mil 100.00mil -250.00mil 6.00mil]
ElementLine [100.00mil -250.00mil 100.00mil 250.00mil 6.00mil]
ElementLine [100.00mil 250.00mil -100.00mil 250.00mil 6.00mil]

ElementLine [-100.00mil 250.00mil -100.00mil 150.00mil 6.00mil]
ElementLine [-100.00mil 150.00mil -130.00mil 150.00mil 6.00mil]

ElementLine [-130.00mil 150.00mil -130.00mil -150.00mil 6.00mil]

ElementLine [-130.00mil -150.00mil -100.00mil -150.00mil 6.00mil]
ElementLine [-100.00mil -150.00mil -100.00mil -250.00mil 6.00mil]



#ElementLine [-55.00mil 0.00mil 55.00mil 0.00mil 6.00mil]

# outlines for 4 pin straight SL series connector
#ElementLine [-512.00mil -250.00mil 42.00mil -250.00mil 6.00mil]
	#ElementLine [-130.00mil -210.00mil 105.00mil -210.00mil 6.00mil]
#	ElementLine [42.00mil -250.00mil 42.00mil 250.00mil 6.00mil]
#	ElementLine [42.00mil 250.00mil -512.00mil 250.00mil 6.00mil]
#	ElementLine [-130.00mil 210.00mil 100.00mil 210.00mil 6.00mil]
#ElementLine [-512.00mil 250.00mil -512.00mil -250.00mil 6.00mil]

	)
