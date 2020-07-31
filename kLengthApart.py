#https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

def kLengthApart(nums, k): #nums = [1,0,0,0,1,0,0,1]
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    count = 0
    counting_list = []
    for n in nums:
        if n == 0:
            count += 1
        elif n == 1:
            counting_list.append(count)

    print(counting_list)

kLengthApart([1,0,0,0,1,0,0,1], 2)
