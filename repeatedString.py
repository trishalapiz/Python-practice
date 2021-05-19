"""
REPEATED STRING

https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


Lilah has a string 's' of lowercase English letters that she repeated infinitely many times.

Give an integer 'n', FIND and PRINT the number of letter a's in the first 'n' letters of Lilah's infinite string.




For example, if the string 's' = 'abcac' and 'n' = 10,
the substring we consider is 'abcacabcac', the first 10 characters of her infinite string.

Complete the repeatedString function in the editor below.
It should return an integer representing the number of occurrences of a in the prefix of length 'n'
in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider

Input Format

The first line contains a single string, s.
The second line contains an integer, n.

-----------------------------------------------------------------------------------------------------------------------
SAMPLE INPUT 0

aba
10

SAMPLE OUTPUT 0

7

EXPLANATION 0

The first n=10 letters of the infinite string are abaabaabaa.
Because there are 7 a's, we print 7 on a new line.
-----------------------------------------------------------------------------------------------------------------------
SAMPLE INPUT 1

a
1000000000000

SAMPLE OUTPUT 1

1000000000000

EXPLANATION 1

Because all of the first n=1000000000000 letters of the infinite string are a, we print 1000000000000 on a new line.
-----------------------------------------------------------------------------------------------------------------------

s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

===> It counts the number of "a" in a full string, and in the last, potentially partial string, and calculates the total amount of "a" based on that.
===> "a" count of full string * number of string repeats + "a" count of last string.

print("s.count(\"a\") is", s.count("a")) --- 'a' count of full string
print("n // len(s) is", (n // len(s))) -- string repeats
print("s[:n % len(s)].count(\"a\")", s[:n % len(s)].count("a")) -- extra letter/partial string
"""

def repeatedString(s, n): #s = string AND n = num
    # s = 'aba'
    # n = 10
    # so string needs to be 'abaabaabaa' [aba aba aba a]

    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

    
repeatedString('aba', 10) #7
repeatedString('abcac', 10) #4

#EXAMPLE
#print("abcacabcac".count("a")) #4
#print(10//3) #3
#print(10%3) #1

