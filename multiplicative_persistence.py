def multiplicative_persistence(n):
    steps = 0
    while n >= 10:  
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

num = int(input("Enter a positive integer: "))
result = multiplicative_persistence(num)
print(f"The multiplicative persistence of {num} is {result}")
