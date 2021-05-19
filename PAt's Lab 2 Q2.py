"""
CAN ONLY USE

* abs()
* upper()
* lower()
* find()
* rfind()
* strip()
* min()
* max()
* abs()
* len()
"""
#PIZTRI is the output if num = 3
#APIZTRIS is the output if num = 4
import random
fullname = input("Enter first and last names (separated by space): ") #user types in name

randomNum = random.randrange(2,5) #want either 2, 3 or 4

space = fullname.find(' ') #.find() finds index of first occurence of the thing being searched for
firstName = fullname[:space].upper() #TRISHA
lastName = fullname[space+1:].upper() #LAPIZ

newName = lastName[len(lastName)-randomNum:] + firstName[:randomNum]
#based on the random number N, we take the last N characters of the surname, and first N characters
#of the first name
print(newName, "random number was", randomNum) #the 'random number was' is used for debugging



