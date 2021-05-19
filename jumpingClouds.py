#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

SAMPLE INPUT
7
[0 0 1 0 0 1 0]
 0 1 2 3 4 5 6  <-- index
 
SAMPLE OUTPUT
4

"""
def jumpingOnClouds(c): #c is a list of 0s and 1s
    #RETURN MINIMUM NUMBER OF JUMPS REQUIRED
    index = 0
    count = 0
    length = len(c)
    while index < length-1:
        if index == length-2: #if at the end
            index += 1
        else:
            if c[index + 2] != 0: #if can't take 2 steps, can surely take 1
                index += 1
            else:
                index += 2

        count += 1
            
    

