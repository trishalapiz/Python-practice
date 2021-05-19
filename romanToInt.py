def romanToInt(s):
    romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
    total = 0

    r
        
    for i in range(1, len(s)-1): #start, stop, step
        print(romanDict[s[i]], romanDict[s[i+1]])
        if romanDict[s[i]] > romanDict[s[i+1]]:
            total += romanDict[s[i]]
        elif romanDict[s[i]] < romanDict[s[i+1]]:
            total += abs(romanDict[s[i]] - romanDict[s[i+1]])
        print("TOTAL IS", total)
                
    return total

print(romanToInt("MCMXCIV"))
