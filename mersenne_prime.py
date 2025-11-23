def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False  # p must be prime
    mersenne_num = 2**p - 1
    return is_prime(mersenne_num)

def get_valid_integer(prompt):
    user_input = input(prompt)
    while not (user_input.isdigit() and int(user_input) > 0):
        print("Invalid input. Please enter a positive integer.")
        user_input = input(prompt)
    return int(user_input)

p = get_valid_integer("Enter a prime number p to check if 2^p - 1 is a Mersenne prime: ")
if is_mersenne_prime(p):
    print(f"2^{p} - 1 is a Mersenne prime.")
else:
    print(f"2^{p} - 1 is NOT a Mersenne prime.")