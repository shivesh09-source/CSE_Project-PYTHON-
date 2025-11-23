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
        return None  # Inverse does not exist
    else:
        return x % m  # Ensure the result is positive

a = int(input("Enter a: "))
m = int(input("Enter m: "))

inverse = mod_inverse(a, m)
if inverse is None:
    print(f"No modular inverse exists for {a} mod {m}")
else:
    print(f"The modular inverse of {a} mod {m} is {inverse}")
