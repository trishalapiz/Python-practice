#reversenumber
#can only use modulus and floor division

import math

#IF NOT LIMITED TO % AND //
number = 345
reverseString = ""
# 345 => 543
for i in range(len(str(number))-1, -1, -1): #meaning starting at 2 (number[2] is 5), -1 because we want to end at 0 (number[0] = 3) and going backwards (therefore -1)
    reverseString += str(number)[i]
print("Doing it using for loops:", number, "=> {}".format(reverseString))


#LIMITED TO % AND //

#137 % 10 = 7
#137 // 10 = 13

n = 137 #ORIGINAL
a_string = ""

a_string = a_string + str(n % 10) #137 % 10 = 7, so a_string = 7
m = n // 10 #137 // 10 = 13
a_string = a_string + str(m % 10) #13 % 10 = 3, so a_string = 73
m = m // 10 #13 // 10 = 1
a_string = a_string + str(m % 10) #1 % 10 = 1, so a_string = 731
print("Doing 3x a_string concatenation, // and % 2 times:", n, "=>", a_string)



