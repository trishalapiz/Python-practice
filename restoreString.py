#https://leetcode.com/problems/shuffle-string/

"""
def restoreString(s, indices):
    print(s)
    shuffle = [None for x in range(len(indices))]
    print(shuffle)
    for i in indices:
        print("i is", i)
        #print("shuffle.insert(i = {}, s[i] = {})".format(i, s[i]))
        #shuffle.insert(i, s[i])
        shuffle[i] = s[i]
        print(shuffle)
restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
#print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
"""
"""
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
"""

#FINAL!!!
"""
def restoreString(s, indices):
    shuffle = [None for x in range(len(indices))]
    for i in range(len(indices)):
        shuffle[indices[i]] = s[i]
    print("".join(shuffle))
"""
"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""
def restoreString(s, indices):
    shuffle = [None for x in range(len(indices))]
    """
    for i in s: #codeleet
        print("i is", i)
        #print("shuffle.insert(i = {}, s[i] = {})".format(i, indices[i]))
        shuffle[i] = s[indices[i]]
    return shuffle
    """
    for i in range(len(indices)):
        shuffle[indices[i]] = s[i]
    print("".join(shuffle))
        
restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
