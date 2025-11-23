def count_distinct_prime_factors(n):
    factors = set()
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.add(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
        if divisor * divisor > n and n > 1:
            factors.add(n)
            break
    return len(factors)

a =int(input(" enter a number : "))
result = count_distinct_prime_factors(a)
print(f"Number of distinct prime factors of {a}: {result}")
