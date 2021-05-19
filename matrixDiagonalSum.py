#https://leetcode.com/problems/matrix-diagonal-sum/

"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the primary
diagonal.

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""

def diagonalSum(mat):
    length = len(mat) #4
    counter = 0
    primary_sum = 0
    sec_sum = 0

    track = set()

    #CAN ONLY COUNT ELEMENT ONCE!
    #NEED TO KEEP TRACK IF IT'S BEEN COUNTED FOR

    #THIS SOLUTION WORKS IF ABLE TO COUNT ELEMENTS MORE THAN ONCE
    for i in range(length): #length = 4
        #i = 0,1,2,3
        track.add(mat[i][i])
        primary_sum += mat[i][i]

    print(primary_sum)
    print(track)

    while counter < length:
        num_to_check = mat[counter][length-1-counter]
        print(num_to_check)

        if num_to_check not in track:
            sec_sum += num_to_check
            track.add(num_to_check)
        counter += 1
            
    return primary_sum + sec_sum


def main():
    """
    mat = [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]]
    """
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    """
    primary diagonal: mat[0][0] + mat[1][1] + mat[2][2] + mat[3][3]
    secondary diagonal: mat[0][3] + mat[1][2] + mat[2][1] + mat[3][0]
    """
    result = diagonalSum(mat)

    print(result)

main()
