def is_perfect_power(n):
    if n <= 1:
        return True  # 1 = 1^b for any b > 1
    b = 2
    while b * b <= n:
        a = 1
        while a ** b < n:
            a += 1
        if a ** b == n:
            return True
        b += 1
    return False

num = int(input("Enter a number to check if it is a perfect power: "))

if is_perfect_power(num):
    print(f"{num} is a perfect power number.")
else:
    print(f"{num} is NOT a perfect power number.")
