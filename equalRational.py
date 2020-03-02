"""
EQUAL RATIONAL NUMBERS
https://leetcode.com/problems/equal-rational-numbers/

Input: S = "0.(52)", T = "0.5(25)"
Output: true
Explanation:
Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.

Input: S = "0.9(9)", T = "1."
Output: true
Explanation: 
"0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".

Note:

* Each part consists only of digits.
* The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
* 1 <= <IntegerPart>.length <= 4
* 0 <= <NonRepeatingPart>.length <= 4
* 1 <= <RepeatingPart>.length <= 4
"""

def isRational(S, T):
    pass
