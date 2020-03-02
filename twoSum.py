"""
TWO SUM https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

----------------------------------------------
:type nums: List[int]
:type target: int
:rtype: List[int]
"""

"""
def twoSum(nums, target):
    some = {}
    for i, o in enumerate(nums):
        some[i] = o
    return some
"""
nums = [2, 4, 3, 9]
def twoSum(nums, target):
        wanted = {}
        for i in range(len(nums)): #i = 0, 1, 2, 3
            n = nums[i] #n is the value
            if n in wanted: 
                return [wanted[n], i] #wanted[n] == i
            else:
                wanted[target-n] = i
            print(wanted)
        return []

print(twoSum(nums, 10))


