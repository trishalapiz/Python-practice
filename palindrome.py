"""
PALINDROME

https://leetcode.com/problems/palindrome-number/

Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

THINGS TESTED HERE:
- floor division
- modulus
- lists (reverse, slicing)
- type conversions
"""
def isPalindrome(x): #READ THE SAME BACKWARDS as forward

    #even length palindrome examples
    #00, 11, 2002, 321123

    #odd length palindrome examples
    #101, 54145, 0192910

    ## Could you solve it without converting the integer to a string? ##

    ##---------------------------STRING METHOD--------------------------##
    """
    x = str(x)
    backward = ""

    for letter in range(len(x)-1, -1, -1): #len(x) = 3 so len(x)-1 = 2
        backward = backward + x[letter]
    print("X is {} and backward is {}".format(x, backward))
    if x == backward:
        return True
    else:
        return False
    """

    ##---------------------------INTEGER METHOD--------------------------##
    temp = x
    new = 0

    #eg x = 121, x // 10 = 12, WHILST x % 10 = 1
    # '//' for all digits but last one
    # '%' for last digit

    while x > 0:
        new = new * 10 + x % 10 #getting the outer digit
        x = x // 10

    return temp == new
    

    

print(isPalindrome(10)) #False
print(isPalindrome(121)) #True
print(isPalindrome(-121)) #False

