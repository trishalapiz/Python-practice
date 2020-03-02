"""
https://leetcode.com/problems/roman-to-integer/

ROMAN TO INTEGER

Input: "IX"
Output: 9

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

---------------------------------------------------------------------------------------
https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php

rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    print("Number is", s)
    for i in range(len(s)):
        print("When i is {}:".format(i))
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]: #if the number after is bigger than the number before
            print("{} += {} - 2 * {} ({})".format(int_val, rom_val[s[i]], rom_val[s[i-1]], s[i]))
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            print("{} += {} ({})".format(int_val, rom_val[s[i]], s[i]))
            int_val += rom_val[s[i]]
        print()
    return int_val
"""

def romanToInt(s): #LVIII
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    #if symbol[previous] < symbol[next] then previous-next
    #for symbol in s:
        #total += romans[symbol]
    #return total
    
    for symbol in range(len(s)-1): #len = 5 // so symbol = 0, 1, 2, 3
        if symbol > 0 and romans[s[symbol]] > romans[s[symbol-1]]:
            total += (romans[s[symbol]] - romans[s[symbol-1]])
        else:
            total += romans[s[symbol]]
    return total
    
    
    
        


#print(romanToInt("LVIII")) #58
#print(romanToInt("IX")) #9
print(romanToInt("MCMXCIV")) #1994
