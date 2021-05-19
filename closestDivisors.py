"""
https://leetcode.com/problems/closest-divisors/

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

-------------------------------------

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

"""

def closestDivisors(num):
    first = num + 1
    second = num + 2

    divisors_one = findFactors(first)
    divisors_two = findFactors(second)

    print(divisors_one, divisors_two)

    

    

    

    


#print(closestDivisors(8))

def findFactors(n):
    factors = []

    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)

    return factors

"""
print(findFactors(10))
print(findFactors(9))
print(findFactors(8))
"""
closestDivisors(8)
