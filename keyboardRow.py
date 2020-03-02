"""
KEYBOARD ROW
https://leetcode.com/problems/keyboard-row/

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

EXAMPLES
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

CONSTRAINTS
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

def findWords(words): #words is a list
    """
    :type words: List[str]
    :rtype: List[str]
    """
    #words = ["Hello", "Alaska", "Dad", "Peace"]
    keyboard = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
    same_row = []

    for word in words:
        for letter in word:
            #if all letters are in the same row, append to same_row
            pass
        pass
    pass
