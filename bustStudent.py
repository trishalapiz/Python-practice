#https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
"""
INITIAL CODE IN GREEN:
Runtime - 52ms
Memory - 12.8 MB
"""
def busyStudent(startTime, endTime, queryTime):
    count = 0
    """
    RUNTIME - 52ms (too slow)
    Memory - 12.8MB
    if len(startTime) > 1:
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count += 1
    else:
        if queryTime >= startTime[0] and queryTime <= endTime[0]:
            count += 1
    return count
    """

    for i in range(len(startTime)): #O(n) time
        if startTime[i] <= queryTime <= endTime[i]:
            count += 1
    return count

print(busyStudent([1, 2, 3], [3, 2, 7], 4)) # 1 student
print(busyStudent([4], [4], 4)) # 1 student
print(busyStudent([4], [4], 5)) # 0 students
print(busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7)) # 0 students
print(busyStudent([9, 8, 7, 6, 5, 4, 3, 2, 1], [19, 10, 10, 10, 10, 10, 10, 10, 10], 5)) # 5 students
