"""BASIC CALCULATOR APP"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2): #include dividing numbers not divisible = float
    if num1 % num2 == 0:
        return num1 // num2
    else:
        return num1 / num2

def main():

    while True:
        try:
            first_num = int(input("Enter a number "))
            second_num = int(input("Enter another number "))
            
            option = int(input("Enter a number between 1 and 4 (inclusive). Enter 5 to quit. "))
            if option < 1 or option > 5:
                print("Please try again. Number must be either 1, 2, 3, 4. ")
            elif option == 1:
                print("{} + {} = {}".format(first_num, second_num, add(first_num, second_num)))
            elif option == 2:
                print("{} - {} = {}".format(first_num, second_num, subtract(first_num, second_num)))
            elif option == 3:
                print("{} x {} = {}".format(first_num, second_num, multiply(first_num, second_num)))
            elif option == 4:
                print("{} / {} = {}".format(first_num, second_num, divide(first_num, second_num)))
            elif option == 5:
                break
        except ValueError:
            print("Looks like you didn't read the instruction...")
main()
    
