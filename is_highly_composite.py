def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count

def is_highly_composite(n):
    target_divisors = count_divisors(n)
    for i in range(1, n):
        if count_divisors(i) >= target_divisors:
            return False
    return True

num = int(input("Enter a positive integer: "))
if is_highly_composite(num):
    print(f"{num} is a highly composite number.")
else:
    print(f"{num} is not a highly composite number.")
