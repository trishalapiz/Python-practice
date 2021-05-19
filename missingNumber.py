#https://leetcode.com/problems/missing-number/

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

EXAMPLE ONE
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

EXAMPLE TWO
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

EXAMPLE THREE
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

EXAMPLE FOUR
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

"""

def missingNumber(nums): #return int
    """THIS SOLUTION IS TOO SLOW, RUNTIME 2052ms, FASTER THAN 11.29% submissions"""
    length = len(nums) + 1
    lost_num = 0 #always a missing number

    for i in range(length):  
        if i not in nums:
            lost_num = i
            return lost_num
        else:
            continue

def main():

    nums = [9,6,4,2,3,5,7,0,1] #length = 9 so 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    #8 is the missing number

    output = missingNumber(nums)

    print(output)
    
    

main()
