"""
INTEGER TO ROMAN
https://leetcode.com/problems/integer-to-roman/

Input: 3
Output: "III"

Input: 4
Output: "IV"

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def intToRoman(s):
    """
    :type num: int
    :rtype: str
    """

    """
    PRINTING DICT KEYS
    for key in romans:
        print(key)

    PRINTING KEYS AND ITS VALUE
    for key, value in romans.items():
        print(key, value)

        k, v
        I 1
        V 5
        X 10
        L 50
        C 100
        D 500
        M 1000
    -------------------------------------
    for num in range(len(str(s))):
        if num > 0 and s[num]:
            pass
        else:
            string += s[num]
    """
    #s is the integer // eg 1994
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    string = ""

    for i in range(len(str(s))): #length of 1994 is 4 so i = 0, 1, 2, 3
        if i == 0:
            pass
        else:
            pass
    
    pass

intToRoman(1994) #MCMXCIV

romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for key, value in romans.items():
    print(key, value)


