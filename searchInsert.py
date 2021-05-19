#https://leetcode.com/problems/search-insert-position/

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.


EXAMPLE
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0
"""

def searchInsert(nums, target):

    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)


print(searchInsert([1,3,5,6], 5)) #2
print(searchInsert([1,3,5,6], 2)) #1
print(searchInsert([1,3,5,6], 7)) #4
print(searchInsert([1,3,5,6], 0)) #0
