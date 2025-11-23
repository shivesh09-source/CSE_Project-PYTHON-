def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_power(n):
    if n < 2:
        return False
    
    for k in range(2, int(n.bit_length()) + 1):
        p = round(n ** (1.0 / k))
        if p ** k == n and is_prime(p):
            return True
    if is_prime(n):
        return True
    return False
n = int(input("Enter a number: "))
if is_prime_power(n):
    print(f"{n} is a prime power number.")
else:
    print(f"{n} is NOT a prime power number.")
