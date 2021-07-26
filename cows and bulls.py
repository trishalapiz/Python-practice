#cows and bulls
#https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

#ValueError - right type but wrong value
#IndexError - index out of range
#TypeError - mismatch of types eg strings != integers

#INDEXING!!!!!!!!!
#LOOOOOOOPPPPPPPPPSSSSSSS

""""
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the CORRECT place, they have a “cow”.
For every digit the user guessed correctly in the WRONG place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...

"""
import random

def try_guess(num, other_num):
    cows = 0
    bulls = 0
    guesses = 0

    num = str(num)
    other_num = str(other_num)
    
    for i in range(4):
        if num[i] == other_num[i]: #if number at same position are the same = COW
            cows += 1
            guesses += 1
            print("{} cows, {} bulls, {} guesses".format(cows, bulls, guesses))
        else:
            if num[i] in other_num: #if number at input is in random number but incorrect position = BULL
                bulls += 1
                guesses += 1
                print("{} cows, {} bulls, {} guesses".format(cows, bulls, guesses))
            else:
                guesses += 1
                print("{} cows, {} bulls, {} guesses".format(cows, bulls, guesses))

    if cows == 4:
        print("Congrats, you have guessed the correct number with {} guesses!".format(guesses))
    elif bulls <= 4 and bulls > 0:
        print("Nice try, you got the right number in the wrong places and it took you {} guesses.".format(guesses))
        print("The number was {}".format(other_num))
    else:
        print("Nice try, better luck next time!")
        print("The number was {}".format(other_num))

def main():
    """
    while True:
        try:
            number = int(input("Enter a 4-digit number: "))
            if len(number) <= 3 and len(number) >= 5:
                raise ValueError("You can only enter 4 digit numbers.")
        except TypeError:
            print("You can only enter letters, please try again.")
            number = int(input("Enter a number: "))
        except ValueError as x:
            print("Please try again. {}".format(x))
        else:
            try_guess(number)
    """
    random_number = str(random.randrange(10000)) #generate a random number
    while True: #MAKING SURE NUMBER DOESN'T START WITH 0 AND IS 4 DIGITS
        if len(random_number) <= 3 or len(random_number) >= 5 or random_number[0] == '0':
            random_number = str(random.randrange(10000))
        else:
            break
    random_number = int(random_number)

    """----------------------------------------------------------------------------------------------------------------------------------------"""
    
    number = input("Enter a 4-digit number: ")
    while True: #MAKING SURE NUMBER DOESN'T START WITH 0 AND IS 4 DIGITS
        if len(number) <= 3 or len(number) >= 5:
            number = input("Number must be 4 digits: ")
        elif number[0] == '0':
            number = input("Number cannot start with 0: ")
        else:
            break
    number = int(number)
    try_guess(number, random_number)
    
main()



    
        

