def repeatedString(s, n): #s = 'abcac', n = number of characters to look at in the string
    #return s[:n].count('a')

    counter = 0
    count = 0
    length = len(s)
    while counter < n:
        if s[counter % length] == 'a':
            count += 1
        counter += 1
    return count

def main():
    s = 'aba'
    n = 10
    result = repeatedString(s,n)
    print(result)

main()
