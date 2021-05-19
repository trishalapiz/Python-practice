#https://leetcode.com/problems/plus-one/
"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

def plusOne(digits):
    digits = digits[::-1] #REVERSED
    the_digits = []
    #print("digits is {}".format(digits))
    incremented = str(digits.pop(0) + 1) #.pop(0) returns first element removed
    #print("incremented is {}".format(incremented))
    if len(incremented) > 1:
        #incremented.split() #10 becomes ["1", "0"]
        incremented = list(incremented)
        #print("incremented is {}".format(incremented))
        the_digits = [int(x) for x in incremented] #[0, 1]
        #print("the digits are {}".format(the_digits))
        for i in the_digits:
            digits.insert(0, i)
    else:
        digits.insert(0, int(incremented))
        
        
        
    #each element in the array contains a single digit.
    return digits[::-1]

def main():

    num1 = [1,2,3]
    num2 = [1,2,3,4,5,6,7,8,9]
    print("from [1,2,3] to {}".format(plusOne(num1)))
    print("from [1,2,3,4,5,6,7,8,9] to {}".format(plusOne(num2)))

main()
