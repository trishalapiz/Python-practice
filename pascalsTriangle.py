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
    #NEED TO MAKE A MULTIDIMENSIONAL ARRAY
    counter = 1

    triangle = []

    while counter <= numRows:
        print("counter: {}".format(counter))
        if not triangle: #if empty?
            triangle.append([1])
            counter += 1
            print("triangle is {}".format(triangle))
        else:
            if len(triangle) == 1:
                triangle.append([1,1])
                counter += 1
                print("triangle is {}".format(triangle))
            else:
                newRow = generateList(triangle[counter-1], counter)
                triangle.append(newRow)
                counter += 1
                #triangle[counter-1]
                print("triangle is {}".format(triangle))
  
            
    return triangle

def generateList(prev_list, counter): #[1,1]
    print("in generateList(), counter is {}".format(counter))
    length = len(prev_list)
    new_list = []

    for i in range(counter-1, -1, -1): #start, end, step
        print("i is {}".format(i))
        if not new_list or counter == 1:
            new_list.append(1)
        elif counter == 2:
            to_add = prev_list[0] + prev_length[-1]
            new_list.append(to_add)
        else:
            to_add = prev_list[length] + prev_length[length-1]
            new_list.append(to_add)
        

    return new_list

    

def main():
    print(generate(5))

main()
