import time 
start_time=time.perf_counter()
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 2:
        factors.append(n)
    return factors
end_time=time.perf_counter()
execution_time= end_time -start_time
print (f"time required=",(execution_time))
print(f"prime number",prime_factors(9))