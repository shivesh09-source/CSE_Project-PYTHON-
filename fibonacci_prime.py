def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(x):
    s = int(x**0.5)
    return s*s == x

def is_fibonacci(num):
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

def is_fibonacci_prime(n):
    return is_fibonacci(n) and is_prime(n)

n = int(input("Enter an integer to check if it is a Fibonacci prime: "))

if is_fibonacci_prime(n):
    print(f"{n} is both a Fibonacci number and prime.")
else:
    print(f"{n} is NOT a Fibonacci prime.")
