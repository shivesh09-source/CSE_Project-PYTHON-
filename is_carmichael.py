def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pow_mod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

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

def is_carmichael(n):
    if n < 2 or is_prime(n):
        return False
    for a in range(2, n):
        if gcd(a, n) == 1:
            if pow_mod(a, n - 1, n) != 1:
                return False
    return True

num = int(input("Enter a number to check if it is a Carmichael number: "))

if is_carmichael(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is NOT a Carmichael number.")
