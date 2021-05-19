#https://leetcode.com/problems/running-sum-of-1d-array/
def runningSum(nums):
    #sums = [nums[i] + nums[i+1] if i > 0 else nums[i] for i in range(len(nums)-2)]
    #return sums

   
    sums = [nums[0]]
    for i in range(1, len(nums)):
        sums.append(sums[i-1] + nums[i])
    return sums
   

    #Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.


print(runningSum([1, 2, 3, 4, 5])) #[1, 3, 6, 10, 15]

#runtime = 32ms (slow because for loop)
n
