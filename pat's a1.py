"""
import random
consonants = "bcdfghjklmnprstvwz"
vowels = "aeiouaeiouaeiouaei"

consonant_letter = random.choice(consonants)
consonant_letter1 = random.choice(consonants)
consonant_letter2 = random.choice(consonants)

#vowel_letter = random.choice(vowels)
vowel_letter = vowels[random.randrange(0, len(vowels))]
vowel_letter1 = random.choice(vowels)
vowel_letter2 = random.choice(vowels)

#output = consonant_letter + vowel_letter + consonant_letter1 + vowel_letter1 + consonant_letter2 + vowel_letter2
output = vowel_letter + consonant_letter + vowel_letter1 + consonant_letter1 + vowel_letter2 + consonant_letter2

final_output = output.center(15)

num_spaces = 4
number_of_stars = 4 * num_spaces
stars = "*" * number_of_stars
initial_spaces = " " * num_spaces

print(stars)
print(stars)
print(final_output, sep = "")
print(stars)
print(stars)
"""

import math

#area = pi * r1 * r2
#perimeter of ellipse = 2 * pi * sqrt((r1^2 + r2^2) / 2)

fencing_per_metre = 75
grass_per_square_metre = 20
major_radius = 10 
minor_radius = 5

num_spaces = 25
number_of_stars = 2 * num_spaces
stars = "*" * number_of_stars
initial_spaces = " " * num_spaces

area = (math.pi * (minor_radius * major_radius)) * 2 #area
perimeter = 2 * math.pi * math.sqrt(((math.pow(major_radius,2) + (math.pow(minor_radius,2))) / 2))

cost_grass = area * grass_per_square_metre

cost_fencing = perimeter * fencing_per_metre

total_cost = cost_grass + cost_fencing

print(stars)
print("Cost of laying grass (", round(area), " square metres): $", cost_grass, sep= "")
print("Cost of fencing (50 metres): $", cost_fencing, sep= "")
print("Total cost: $", total_cost, sep= "")
print(stars)
