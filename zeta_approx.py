def zeta_approx(s, terms):
    total = 0.0
    for n in range(1, terms + 1):

        term = n ** (-s)
        total += term
    return total

s = float(input("Enter the value of s (real number > 1): "))
terms = int(input("Enter the number of terms to use in the approximation: "))

approx_value = zeta_approx(s, terms)

print(f"Approximation of zeta({s}) using {terms} terms is: {approx_value}")
