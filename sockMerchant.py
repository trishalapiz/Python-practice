#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""
Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

INPUT FORMAT

The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

9
10 20 20 10 10 30 50 10 20
"""

def main():
    n = int(input()) #9

    ar = list(map(int, input().rstrip().split())) #[10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n, ar))

def sockMerchant(n, ar): ##### means print statements used to test and see current values
    count = 0

    ### THE FOLLOWING ALGORITHM HAS A COMPLEXITY OF n^2 ###
    for i in range(n): #i = 0
        if ar[i] == 0:
            continue
        for j in range(i+1,n): #j = 1
            if ar[i] == ar[j]: #if 10 == 20
                count += 1
                ar[i] = 0
                ar[j] = 0
                break

    return count

main()
