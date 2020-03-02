"""
NUMBER OF STEPS TO REDUCE A NUMBER TO ZERO
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.

Input: num = 123
Output: 12
"""

def numberOfSteps(num): #20ms faster than 36.17% submissions (bad)
    """
    :type num: int
    :rtype: int
    """

    count = 0 #steps

    while num > 0:
        if num % 2 == 0: #even
            num = num // 2
            count += 1
        else:
            num = num - 1
            count += 1

    return count

print(numberOfSteps(14)) #6
print(numberOfSteps(8)) #4
print(numberOfSteps(123)) #12

print()

def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))
    
