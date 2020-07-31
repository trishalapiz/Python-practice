"""
https://www.hackerrank.com/challenges/python-print/problem?h_r=next-challenge&h_v=zen

The included code stub will read an integer 'n' from STDIN.

Without using any string methods, try to print the following:

123.....n

Note that "....." represents the consecutive values in between.

Example:

n = 5

Print the string 12345.
"""


n = int(input())

for i in range(1, n+1):
    print(i, end="")

