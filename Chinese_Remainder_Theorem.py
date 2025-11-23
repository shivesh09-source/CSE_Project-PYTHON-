def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    else:
        return x % m

def crt(remainders, moduli):
    product = 1
    for m in moduli:
        product *= m

    result = 0
    for r, m in zip(remainders, moduli):
        p = product // m
        inv = mod_inverse(p, m)
        if inv is None:
            return None  # Inverse does not exist; CRT not solvable
        result += r * inv * p

    return result % product

n = int(input("Enter the number of congruences: "))
remainders = []
moduli = []
for i in range(n):
    r = int(input(f"Enter remainder r{i+1}: "))
    m = int(input(f"Enter modulus m{i+1}: "))
    remainders.append(r)
    moduli.append(m)

solution = crt(remainders, moduli)
if solution is None:
    print("No solution exists because modular inverse does not exist for some term.")
else:
    print(f"The solution x that satisfies all congruences is: {solution}")
