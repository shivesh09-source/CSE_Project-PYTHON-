def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result

def is_quadratic_residue(a, p):
    if a == 0:
        return True  # 0 is always a quadratic residue mod p
    legendre = mod_exp(a, (p - 1) // 2, p)
    return legendre == 1

a = int(input("Enter a (integer): "))
p = int(input("Enter p (prime modulus): "))

if is_quadratic_residue(a, p):
    print(f"{a} is a quadratic residue modulo {p}.")
else:
    print(f"{a} is NOT a quadratic residue modulo {p}.")
