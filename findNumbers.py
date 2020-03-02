"""
FIND NUMBER WITH EVEN NUMBER OF DIGITS
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

DON'T DELETE
nums = [555,901,482,1771]
#newNums = [str(x) for x in nums]
evens = [int(x) for x in nums if len(str(x)) % 2 == 0]
#evens = [int(e) for e in newNums if len(e) % 2 == 0]
print(nums)
#print(newNums)
print(evens)
"""

def findNumbers(nums):
    #runtime 44ms faster than 36.52% of submissions
    #memory 12MB less than 100% online submissions
    return len([int(x) for x in nums if len(str(x)) % 2 == 0])

print(findNumbers([12,345,2,6,7896]))
print(findNumbers([555,901,482,1771]))

