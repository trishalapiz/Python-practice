"""
SUBTRACT THE PRODUCT AND SUM THE DIGITS OF AN INTEGER
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

** Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

CONSTRAINT:
1 <= n <= 10^5
"""

def subtractProductAndSum(n): #runtime 12ms
    """
    :type n: int
    :rtype: int
    """
    if n >= 1 or n <= 10^5:
        #list comprehension = [expression for variable in range if condition]
        nums = [int(x) for x in str(n)] 
        
        #get product of digits
        product = 1

        for i in nums:
            product *= i

        print("product:", product)

        #get sum of digits
        digit_sum = sum(nums)
        print("sum is {}".format(digit_sum))

        return product - digit_sum

print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))
