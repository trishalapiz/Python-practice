#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly n steps.
For every step he took, he noted if it was an uphill, U, or a downhill, D step.
Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude.

We define the following terms:

* A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
* A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

$$$$$$ Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through. $$$$$$

For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path

INPUT FORMAT

- The first line contains an integer n, the number of steps in Gary's hike.
- The second line contains a single string s, of n characters that describe his path.

OUTPUT FORMAT

- Print a single integer that denotes the number of valleys Gary walked through during his hike.

Sample Input

8
UDDDUDUU

Sample Output

1

Explanation

If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:

_/\      _
   \    /
    \/\/
-UDDDUDUU-   [using * to denote a valley]
   ******
He enters and leaves one valley.

ANOTHER CASE
12
_          /\_
 \  /\    /
  \/  \/\/
-DDUUDDUDUUUD-
 ****^^^^^^ so first valley is *, second valley is ^

He enters and leaves two valleys.

"""

def countingValleys(n, s): #n = number of steps , s = string depicting path
    #WE WANT TO COUNT THE NUMBER OF TIMES LEVEL 0 HAS BEEN REACHED?
    count = 0 #number of valleys
    level = 0

    for letter in s:
        if letter == 'U':
            level += 1
        else:
            level -= 1

        if level == 0 and letter == 'U':
            count += 1
    return count

print(countingValleys(8, 'UDDDUDUU')) #1
print(countingValleys(12, 'DDUUDDUDUUUD')) #2
