"""
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within the list
(including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.

EXAMPLE
Input: ["bella","label","roller"]
Output: ["e","l","l"]

CONSTRAINTS
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

from collections import Counter

def commonChars(A): #["bella","label","roller"]
    common_dict = Counter(A[0])
    for word in A:
        common_dict &= Counter(word)
    return list(common_dict.elements())

    """
    common_dict = {}
    final_list = []

    #THIS CAN BE DONE IN 1 LINE USING COUNTER() which turns it into a dict!
    for word in A:
        a_dict = {}
        for letter in word:
            if letter not in a_dict:
                a_dict[letter] = 1
            else:
                a_dict[letter] += 1
            common_dict[word] = a_dict
        final_list.append(max(a_dict.values()))
    
    print("common_dict:", common_dict)
    print("a_dict:", a_dict)
    print("final_list", final_list)
    """

    """
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    dict3 = Counter(str3)
    common_dict = dict1 & dict2 & dict3

    print("dict1:",dict1)
    print("dict2:",dict2)
    print("dict3:",dict3)
    print("common_dict:", common_dict)
    #print(list(common_dict.elements()))
    """
#print(commonChars(["bella","label","roller"]))
print(commonChars(["bella","label","roller"]))
#commonChars("bella","label", "roller") #if not a list
