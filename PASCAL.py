#https://leetcode.com/problems/pascals-triangle/

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Input: 5
Output: (In Pascal's triangle, each number is the sum of the two numbers directly above it.)
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def generate(numRows):
    triangle = []
    #[[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

    """
    for row in triangle:
        if len(row) == 1:
            row[0] = 1
        elif len(row) == 2:
            row = [1,1]
        elif len(row) > 2:
            for i in range(len(row)):
    """

    for i in range(numRows): #i = 0, 1, 2, 3, 4
        row = [ None for _ in range(i+1) ]
        row[0], row[-1] = 1, 1

        for j in range(1, len(row)-1): #len of row 3 = 4 so j = 1, 2
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)                

    return triangle
            
                
    
    

def main():
    print(generate(5))

main()
