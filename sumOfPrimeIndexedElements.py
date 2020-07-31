#sum of prime-index elements
def prime(n):
    if n <= 0:
        return False
    elif n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def sum_list(arr):
    total = 0
    for number in arr:
        total += number
    return total

a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

primeNumbered = [] #should have [3, 4, 6, 8, 12, 14] and then sum these up

for i in range(len(a_list)):
    if prime(i) == True:
        primeNumbered.append(a_list[i])
print(primeNumbered)
#print(sum_list(primeNumbered))
print(sum(primeNumbered))

