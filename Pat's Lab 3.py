"""
PATS LAB 3
"""

number = 3498
print("The number:", number, end=" ") 

total = 0 #where we sum the digits the first time
new_total = 0 #where we sum the digits the second time

""" HOW U SUM THE DIGITS OF 3498 """
#get 8
total += (number%10) #number%10 =  3498%10 = 8, so total = 8
number = number // 10 #3498 // 10 = 349

#get 9
total += (number%10) # 349 % 10 = 9, so total becomes 17 (8+9)
number = number // 10 #349 // 10 = 34

#get 4
total += (number%10)
number = number // 10

#get 3
total += number

#total = 24
#number = 3

string_total = str(total)

#check if the length of the number is less than 2
if len(string_total) < 2: 
    string_total = string_total + "0" #concatenate 0 so you have a 2 digit number

    total = int(string_total) #turn it back to a number

    new_total += (total%10) #24 % 10 = 4
    total = total // 10 #24 // 10 = 2

    new_total += (total%10) #2 % 10 = 2
else: #if length is 2 or more
    new_total += (total%10) #24 % 10 = 4
    total = total // 10 #24 // 10 = 2

    new_total += (total%10) #2 % 10 = 2


print("The digital root:", new_total)



