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
    for i in range(len(nums)): #[2,5,5,11]
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



