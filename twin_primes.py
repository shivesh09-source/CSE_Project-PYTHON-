def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes(limit):
    twins = []
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            twins.append((num, num + 2))
    return twins

def get_valid_integer(prompt):
    user_input = input(prompt)
    while not (user_input.isdigit() and int(user_input) > 1):
        print("Invalid input. Please enter an integer greater than 1.")
        user_input = input(prompt)
    return int(user_input)

limit = get_valid_integer("Enter an integer greater than 1 as the limit: ")
pairs = twin_primes(limit)
print(f"Twin prime pairs up to {limit}:")
for pair in pairs:
    print(pair)