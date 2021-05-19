#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
#STARTED: February 2 2021

"""
Given the array candies and the integer extraCandies,
where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies
among the kids such that he or she can have the greatest number of
candies among them. Notice that multiple kids can have the greatest
number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.

"""

def kidsWithCandies(candies, extraCandies):
    maxCandies = len(candies)

    result = []
    greatestNum = 0

    for candy in candies:
        if candy + extraCandies >= maxCandies and candy + extraCandies <= greatestNum:
        elif candy + extraCandies >= maxCandies:
            result.append(True)
            greatestNum = candy + extraCandies
        else:
            result.append(False)

    return result

    

#print(kidsWithCandies([2,3,5,1,3], 3))
#print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12,1,12], 10)) #should be [true,false,true]

#new_list = [expression(i) for i in old_list if filter(i)]
#new_range = [i * i for i in range(5) if i % 2 == 0] #0, 1, 2, 3, 4
#print(new_range) #0, 4, 16
