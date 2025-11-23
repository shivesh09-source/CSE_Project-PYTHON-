def sum_of_divisors(num):
    if num <= 1:
        return 0
    total = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    return total

def are_amicable(a, b):
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if are_amicable(n1, n2):
    print(f"{n1} and {n2} are amicable numbers.")
else:
    print(f"{n1} and {n2} are not amicable numbers.")
