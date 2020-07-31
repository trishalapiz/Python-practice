#https://leetcode.com/problems/reverse-integer/
def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        #convert to a string, and reverse sort string
        hold = str(abs(x))
        print("hold is", hold)
        ans = int(hold[::-1])
        print("ans is", ans)

            #check special case, overflow or negative value
        if ans > 2**31 -1:
            return 0
        if x < 0:
            ans *= -1
        return ans

print(reverse(123)) #321
print(reverse(-123)) #-321
print(reverse(120)) #21

print()

def reverseBits(n): #n is an int
    n = str(n)
    #n = int(n[::-1], 2)
    return n[::-1]

print("reverseBits('00000010100101000001111010011100') = ", end=" ")
print(reverseBits(00000010100101000001111010011100)) #00111001011110000010100101000000

#print(int('00000010100101000001111010011100', 2))
