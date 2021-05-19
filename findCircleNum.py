#https://leetcode.com/problems/friend-circles/

"""
There are N students in a class.
Some of them are friends, while some are not.
Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C,
    then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct
    or indirect friends.

Given a N*N matrix M representing the friend relationship between students
    in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with
    each other, otherwise not.
And you have to output the total number of friend circles among all
    the students.

EXAMPLE
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1

Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
"""

def findCircleNum(M):

    return len(M)

print(findCircleNum([[1,1,0],[1,1,1],[0,1,1]])) # 1 -- len(M) returns 3 because 3 rows of lists
