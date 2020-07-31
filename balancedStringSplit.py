"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

EXAMPLE
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL",
             each substring contains same number of 'L' and 'R'.

"""
def balancedStringSplit(s):
    check = {'R': 0, 'L': 0}
    count = 0
    for word in s:
        check[word] += 1
        if check['R'] == check['L']:
            count += 1
            check['R'] = 0 #reset
            check['L'] = 0 #reset
    return count

print(balancedStringSplit("RLRRLLRLRL"))
