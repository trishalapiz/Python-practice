"""
GOAT LATIN
https://leetcode.com/problems/goat-latin/

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

* If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
  For example, the word 'apple' becomes 'applema'.
 
* If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
  For example, the word "goat" becomes "oatgma".
 
* Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
  For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
  Return the final sentence representing the conversion from S to Goat Latin.

EXAMPLE

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

CONSTRAINTS
* S contains only uppercase, lowercase and spaces. Exactly one space between each word.
* 1 <= S.length <= 150.

"""

def goatLatin(S): #S is sentence
    #Runtime: 20 ms, faster than 47.77% of Python online submissions for Goat Latin
    #Memory Usage: 11.8 MB, less than 20.00% of Python online submissions for Goat Latin
    """
    :type S: str
    :rtype: str
    """
    vowels = 'AEIOUaeiou'
    words_list = S.split() #going through each word
    count = 1

    goat_latin = []
    
    for word in words_list:
        if word[0] in vowels: #if the first letter of word is a vowel
            extra_a = count * 'a'
            word = word + "ma" + extra_a 
            goat_latin.append(word)
            count += 1
        else: #if consonant
            extra_a = count * 'a'
            word = word[1:] + word[0] + "ma" + extra_a
            goat_latin.append(word)
            count += 1
            
    return " ".join(goat_latin)

print(goatLatin("I speak Goat Latin"))
print(goatLatin("The quick brown fox jumped over the lazy dog"))
