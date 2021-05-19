"""
inspiration = playing bowling on Jan 9 2021 and not knowing how scoring works


HOW SCORING WORKS
https://en.wikipedia.org/wiki/Ten-pin_bowling#Traditional_scoring

say we're on frame N:

==> if we get a STRIKE, the next 2 balls (pretty much ur turn in the next frame N+1 --> IF NOT a strike)
are ADDED to the strike --> and the score of the 2 balls in frame N+1 are added to the score
from frame N

    EXAMPLE

    frame 1 you get a strike, Frame 2 you knock down 3 pins then 6 pins, 3 and 6 are added to the strike
    (10) making Frame 1 = 19, and because you didn't get a spare nor a strike in Frame 2, Frame
    2's score is 3+6 which gets added to Frame 1's score (19) making it 19 + 9 = 28


==> if you knock down a couple pins THEN GET A SPARE, the next ball (first turn in frame N+1)
is added to the pins+spare, which becomes the score for Frame N

    if in Frame N+1 there is neither a spare or strike, the number of pins knocked down in
    frame N+1 is added to the total score

    EXAMPLE

    frame 1 you knock down 7 then get a spare (knocked down the remaining 3), upon your first
    turn in frame 2, the first turn is added to the number of pins knocked down in frame 1
    making it 7 + 3 from frame 1 AND + 4 from frame 2 making Frame 1 = 14

    then if Frame 2 is 4 pins then 2 pins, the score for Frame 2 becomes 14 + (4 + 2) = 20

"""

import random


def bowlingGame():

    

    pass


pins = 10

knocked_over = random.randrange(0,11) #you can either hit no pins, some pins or all the pins



