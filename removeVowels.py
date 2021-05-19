#remove vowels from string

def removeVowels(s):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    """
    the_string = list(s)
    print("the_string as a list is {}".format(the_string))
    string_length = len(the_string) #9

    for i in range(string_length):
        print(i, the_string[i])
        if the_string[i] in vowels:
            the_string.pop(i)

    return "".join(the_string)
    """
    new_string = ""

    for i in range(len(s)): #solution is O(n) time bc of loop
        if s[i] not in vowels:
            new_string += s[i]
    return new_string
    

def main():

    removed_string = removeVowels("Hollywood")
    print(removed_string)

    #nums = [1,1,1,3,3,4,3,2,4,2]

    """
    length = len(nums)
    print(length)
    distinct = set(nums)
    check = dict.fromkeys(distinct,0)
    print(check)
        
    for n in nums:
        check[n] += 1

    print(check)
    """

main()
