def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None  # Order not defined if a and n not coprime
    k = 1
    val = a % n
    while val != 1:
        val = (val * a) % n
        k += 1
    return k

a = int(input("Enter the value of a (integer): "))
n = int(input("Enter the modulus n (integer): "))

order = order_mod(a, n)
if order is None:
    print(f"Order not defined for {a} mod {n} as they are not coprime.")
else:
    print(f"The order of {a} modulo {n} is {order}.")
