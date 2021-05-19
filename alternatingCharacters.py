#https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def alternatingChars(s):
    count = 0
    string_list = list(s)

    while count < len(string_list):
        print(string_list)
        if len(string_list) == 1:
            return string_list
        elif string_list[count] == string_list[count+1]:
            string_list.remove(string_list[count+1])
        count += 1
    return string_list
    

def main():

    print(alternatingChars("AAAA")) #should return 'A'
    #print(alternatingChars("ABABAABBAB")) #should return 'ABABABAB'

main()
