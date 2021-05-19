#https://leetcode.com/problems/add-binary/

"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

def addBinary(a,b):
    first_bin = str(bin(a))
    sec_bin = str(bin(b))

    print("first bin be {}".format(first_bin))
    print("second bin be {}".format(sec_bin))

def main():

    #print(addBinary(2,3))

    addBinary(2,3)

main()
