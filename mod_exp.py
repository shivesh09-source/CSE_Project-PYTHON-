def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus  
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
modulus = int(input("Enter modulus: "))

result = mod_exp(base, exponent, modulus)
print(f"Result of ({base}^{exponent}) % {modulus} = {result}")
