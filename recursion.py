def decimal_to_octal(number):
    octal=''
    while number>0:
        octal=str(number%8) + octal
        number=number//8
    return octal

def recursion(number):
    if number<8:
        return str(number)
    else:
        return recursion(number//8) + str(n%8)

n=int(input("input decimal number:" ))
print(decimal_to_octal(n))



