class Solution(object):
    def twoSum(self, nums, target):
        cache = {}
        for i in xrange(len(nums)):
            if target - nums[i] in cache and cache[target - nums[i]] != i:
                return [cache[target - nums[i]], i]
            cache[nums[i]] = i

#a = [1, 2, 3, 4]
#print(enumerate(a)) #can't just print enumerate()
#print(list(enumerate(a)))

def twoSum(nums, target):
        residual = {}
        for i, n in enumerate(nums): #when i = 0 then n = 1, i = 1 then n = 2....
            #i, n ----- n are the elements in nums
            #0, 1
            #1, 2
            #2, 3
            #3, 4
            print(residual)
            if n in residual:
                return [i, residual[n]]
            else:
                residual[target - n] = i

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

print(twoSum([1, 2, 3, 4], 6))
