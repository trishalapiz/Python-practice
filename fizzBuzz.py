"""
FIZZ BUZZ
https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

def fizzBuzz(n):
    """HAVING num += 1 IN EVERY BRANCH"""
    #Runtime: 36 ms, faster than 34.37% of Python online submissions for Fizz Buzz
    #Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Fizz Buzz
    # ^^^^ EVERYTIME THERE IS A LIST INPUT AND LIST OUTPUT REQUIRED USE LIST COMPREHENSIONS!!!!

    """num += 1 AFTER the branches"""
    #Runtime: 32 ms, faster than 67.06% of Python online submissions for Fizz Buzz.
    #Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Fizz Buzz.

    num = 1

    fizzbuzz = []
    
    while num <= n:
        if num % 3 == 0 and num % 5 == 0: #if multiple of 3 AND 5
            fizzbuzz.append("FizzBuzz")
            #num += 1
        elif num % 3 == 0: #if multiple of 3
            fizzbuzz.append("Fizz")
            #num += 1
        elif num % 5 == 0: #if multiple of 5
            fizzbuzz.append("Buzz")
            #num += 1
        else:
            fizzbuzz.append(str(num))
            #num += 1

        num += 1
    
    return fizzbuzz

print(fizzBuzz(15))
