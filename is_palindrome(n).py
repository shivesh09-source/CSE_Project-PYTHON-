def is_palindrome(n):
    return str(n) == str(n)[::-1]  
try:
    ui= int(input("enter a number: "))
    if is_palindrome(ui):
        print(f"{ui} is pallindrome")
    else :
        print(f"{ui} is not a  pallindrome")
except ValueError:
    print("invalid input. please enter an integer ")
