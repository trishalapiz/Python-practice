"""
DAY OF THE WEEK
https://leetcode.com/problems/day-of-the-week/

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

EXAMPLES

Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

CONSTRAINT
* year is between 1971 and 2100
"""

def dayOfTheWeek(day, month, year):
    """
    :type day: int
    :type month: int
    :type year: int
    :rtype: str
    """
