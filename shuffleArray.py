#https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    x = nums[:n]
    y = nums[n:]
    l = 0
    r = 0

    print("x is {}".format(x))
    print("y is {}".format(y))
    
    for i in range(len(nums)):
        print("when {}:".format(i))
        #if even
        if i % 2 == 0:
            nums[i] = x[l]
            l += 1
            print("l after it's incremented: {}".format(l))
        else: #if odd
            nums[i] = y[r]
            r += 1
            print("r after it's incremented: {}".format(r))
    return nums

def main():

    print(shuffle([2,3,5,4,1,7], 3))

main()
