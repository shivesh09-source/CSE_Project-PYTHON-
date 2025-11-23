def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = 2          
    y = 2
    c = 1         
    d = 1
    def f(x):
        return (x * x + c) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        if d == n:
            c += 1  
            x, y = 2, 2
    return d

n = int(input("Enter an integer to factorize: "))
factor = pollard_rho(n)
print("A non-trivial factor of", n, "is", factor)
