#https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums): #runtime = 28ms, memory = 12.8 MB
    count = 0

    #FOR LOOP WAY
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                count+= 1
    return count

print(numIdenticalPairs([1, 2, 3, 1, 1, 3])) #[1, 1], [1, 1], [1, 3] and [3, 3]
print(numIdenticalPairs([1, 1, 1, 1]))
print(numIdenticalPairs([1, 2, 3]))
