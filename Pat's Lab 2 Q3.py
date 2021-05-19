"""
PAT'S LAB 2 Q3
"""

""" EXAMPLE OUTPUT

***********************
** n____y is p_____t **
***********************
Nobody is perfect
"""

phrase = "hello world python".lower() #convert to lowercase

#find the spaces
first_space = phrase.find(' ') 
second_space = phrase.rfind(' ')

#separate the words
word1 = phrase[:first_space] #nobody LEN = 6
word2 = phrase[first_space+1:second_space] #is
word3 = phrase[second_space+1:] #perfect

#format
outer_stars = (len(phrase) + 6) * "*"

underscore = "_"
two_stars = 2 * "*" #the stars at the sides of the new phrase
second_line = two_stars + " " #initialise the output of the second line
a_list = [word1, word2, word3] #converted to a list so it's easier to go through each word and check its length

#if the length of the word is greater than 2, add '_' in between first/last letters
#otherwise, leave word as is

for word in a_list:
    if len(word) > 2:
        if a_list.index(word) != (len(a_list)-1): 
            num_underscore = '_' * (len(word)-2)
            second_line = second_line + word[0] + num_underscore + word[-1] + ' '
        else: #last word
            num_underscore = '_' * (len(word)-2)
            second_line = second_line + word[0] + num_underscore + word[-1] + ' ' + two_stars
    else: #if len(word) 0, 1, 2
        if a_list.index(word) != (len(a_list)-1):  
            second_line = second_line + word + ' '
        else: #last word
            second_line = second_line + word + ' ' + two_stars
print(outer_stars) # ***********************
print(second_line) # ** n____y is p_____t **
print(outer_stars) # ***********************
