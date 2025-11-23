def count_divisors(n):
    if n <= 0:
        return 0 
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1  
            else:
                count += 2  
        i += 1
    return count

number = int(input("enter a number:"))
print(f"Number of positive divisors of {number} is: {count_divisors(number)}")