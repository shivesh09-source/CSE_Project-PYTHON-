def is_harshad(n):
    sum_digits = sum(int(digit) for digit in str(n))
    return n % sum_digits == 0

number = int(input("enter a number "))
if is_harshad(number):
    print (f"{number} is a harshad number ")
else :
    print (f"{number} is not a harshad number")