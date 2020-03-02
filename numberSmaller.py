"""
How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
* For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
* For nums[1]=1 does not exist any smaller number than it.
* For nums[2]=2 there exist one smaller number than it (1). 
* For nums[3]=2 there exist one smaller number than it (1). 
* For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

"""
def smallerNumbersThanCurrent(nums): #396ms faster than 33.33% submissions, 11.9MB less than 100% submissions
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    new_list = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        new_list.append(count)

    return new_list

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7]))

"""
Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""

def countSmaller(nums):

    new_list = []
    print(nums)
    #when on 1st number, compare with numbers after it (sub list)
    for i in range(len(nums)): #i = 0, 1, 2, 3
        count = 0
        sublist = nums[i+1:]
        print(sublist)
        if len(sublist) > 1:
            for j in sublist:
                if sublist[j] < nums[i]:
                    count += 1
            new_list.append(count)


    return new_list

print(countSmaller([5, 2, 6, 1])) #[2, 1, 1, 0]

