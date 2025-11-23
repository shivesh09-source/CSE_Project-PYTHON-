def pow_mod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def miller_rabin_test(d, n, a):
    x = pow_mod(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def is_prime_miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        a_list = [2, 3, 5, 7, 11]
        a = a_list[_ % len(a_list)]
        if a > n - 2:
            a = 2
        if not miller_rabin_test(d, n, a):
            return False
    return True

num = int(input("Enter the number to check if it is prime: "))
rounds = int(input("Enter the number of rounds for the test: "))

if is_prime_miller_rabin(num, rounds):
    print(f"{num} is probably prime.")
else:
    print(f"{num} is composite.")
