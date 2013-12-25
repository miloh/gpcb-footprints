Element[ "" "molex_705430036" "" "" 10 10 0 0 3 100""]
(
#[0, 0]
#[-50.0, 50.0]

#Pin [rX rY]
Pin [ 0mil -50.0mil 71mil 10mil 66mil 46mil  "1" "1" "square" ]
Pin [ 0mil 50.0mil 71mil 10mil 66mil 46mil  "2" "2" "" ]

#ElementLine[ rX1 rY1 rX2 rY2  silk thicknessmil]
ElementLine[ -42.0mil -98.0mil 42.0mil -98.0mil 6mil]
ElementLine[ 42.0mil -98.0mil 42.0mil -2.0mil 6mil]
ElementLine[ 42.0mil -2.0mil -42.0mil -2.0mil 6mil]
ElementLine[ -42.0mil -2.0mil -42.0mil -98.0mil 6mil]
ElementLine[ -42.0mil 2.0mil 42.0mil 2.0mil 6mil]
ElementLine[ 42.0mil 2.0mil 42.0mil 98.0mil 6mil]
ElementLine[ 42.0mil 98.0mil -42.0mil 98.0mil 6mil]
ElementLine[ -42.0mil 98.0mil -42.0mil 2.0mil 6mil]

## cross shape defines outline of straight angle 2ckt SL connect
## Dimension "A" from 705430036_sd.pdf  0.100" for 2 CKT
#ElementLine [-5.00mil -50.00mil -5.00mil 50.00mil 6.00mil]
## Dimension "B" from 705430036_sd.pdf  0.210" for 2 CKT
#ElementLine [5.00mil -105.00mil 5.00mil 105.00mil 6.00mil]
# Add in typ. wall thickness of 40mils on either side of "B"
#ElementLine [0.00mil -145.00mil 0.00mil 145.00mil 6.00mil]

# outline of part using the above guidlines
ElementLine [-130.00mil -145.00mil 100.00mil -145.00mil 6.00mil]
ElementLine [100.00mil -145.00mil 100.00mil 145.00mil 6.00mil]
ElementLine [100.00mil 145.00mil -130.00mil 145.00mil 6.00mil]
ElementLine [-130.00mil 145.00mil -130.00mil -145.00mil 6.00mil]

#ElementLine [-55.00mil 0.00mil 55.00mil 0.00mil 6.00mil]

)
