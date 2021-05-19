#based on a COMPSCI105 assignment -> number converter
#trying to make it non-recursive

def converter(n, b): #n = number to be converted, b = mode to convert
    final_number = []

    if b == 2:
        while n > 0:
            final_number.append(n % b)
            n = n // 10
    elif b == 8:
        while n > 0:
            final_number.append(n % b)
            n = n // b


def main():

    binary = converter(34, 2)
    octal = converter(10, 8)
    hexadecimal = converter(23, 16)

main()

if increment > 0:
                remainder = str(number % base)
                a_list.append(remainder)
                a_string = "".join(a_list)
            else:
                remainder = str(number % base)
                a_list.append(remainder)
                a_string = "".join(a_list)
