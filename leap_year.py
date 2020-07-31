"""
https://www.hackerrank.com/challenges/write-a-function/problem

In the Gregorian calendar, three conditions are used to identify leap years:

- The year can be evenly divided by 4, is a leap year, unless:
- The year can be evenly divided by 100, it is NOT a leap year, unless:
- The year is also evenly divisible by 400. Then it is a leap year.
"""
def is_leap(year): #1990
    leap = False
    
    # Write your logic here
    if year % 4 == 0: #if evenly divided by 4
        print("divisible by 4")
        if year % 100 == 0: #must also be divisble by 400
            print("divisible by 100")
            if year % 400 == 0:
                print("divisible by 400")
                leap = True
                return leap
            else:
                return leap
    elif year % 100 == 0: #must also be divisble by 400
        print("divisible by 100")
        if year % 400 == 0:
            print("divisible by 400")
            leap = True
            return leap
        else:
            return leap
    else:
        return leap

year = int(input())
print(is_leap(year))

"""
if a year is divisible by 4 = leap year

if year is divisible by 4, and divisible by 400 WHEN DIVISIBLE by 100 = leap year
