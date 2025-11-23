# CSE_Project-PYTHON-
Mathematical Functions in Python
# 🐍 Python Number Theory & Cryptography Functions

## 📝 Overview

This repository hosts a comprehensive collection of **34 Python functions** that implement various concepts from **Number Theory, Discrete Mathematics, and Cryptography**.

The project aims to demonstrate the application of course concepts through practical, modular, and well-tested code. Each function addresses a specific mathematical or algorithmic problem, ranging from basic number properties to advanced cryptographic primitives.

## ✨ Features

This project includes 34 distinct functions categorized by topic:

### Basic Number Properties (Questions 1-12)

1.  `factorial(n)`: Calculates the factorial of a non-negative integer $n$ ($n!$).
2.  `is_palindrome(n)`: Checks if a number reads the same forwards and backwards.
3.  `mean_of_digits(n)`: Returns the average of all digits in a number.
4.  `digital_root(n)`: Repeatedly sums the digits of a number until a single digit is obtained.
5.  `is_abundant(n)`: Returns `True` if the sum of proper divisors of $n$ is greater than $n$.
6.  `is_deficient(n)`: Returns `True` if the sum of proper divisors of $n$ is less than $n$.
7.  `is_harshad(n)`: Checks if a number is divisible by the sum of its digits (Harshad/Niven number).
8.  `is_automorphic(n)`: Checks if a number's square ends with the number itself.
9.  `is_pronic(n)`: Checks if a number is the product of two consecutive integers (Pronic/Heteromecic number).
10. `prime_factors(n)`: Returns the list of prime factors of a number.
11. `count_distinct_prime_factors(n)`: Returns how many unique prime factors a number has.
12. `is_semiprime(n)`: Checks if a number is the product of two (not necessarily distinct) prime numbers.

### Modular Arithmetic & Number Theory (Questions 13-21, 25-32)

13. `phi(n)`: Returns the count of numbers $\le n$ that are coprime to $n$ (Euler's Totient Function).
14. `modular_inverse(a, m)`: Calculates the modular multiplicative inverse of $a \pmod m$.
15. `solve_crt(congruences)`: Solves a system of linear congruences (Chinese Remainder Theorem).
16. `is_primitive_root(g, n)`: Checks if $g$ is a primitive root modulo $n$.
17. `legendre_symbol(a, p)`: Computes the Legendre symbol $(a/p)$.
18. `solve_dlog(g, h, p)`: Finds the discrete logarithm $x$ such that $g^x \equiv h \pmod p$.
19. `pollard_p_minus_1(n, B)`: Integer factorization using Pollard's $p-1$ algorithm.
20. `continued_fraction(x, max_terms)`: Returns the continued fraction representation of a real number $x$.
21. `sum_digits_base_b(n, b)`: Computes the sum of the digits of $n$ in base $b$.
25. `mod_exp(base, exponent, modulus)`: Efficiently calculates $(\text{base}^{\text{exponent}}) \pmod{\text{modulus}}$.
26. `lucas_sequence(n)`: Generates the first $n$ Lucas numbers.
27. `is_perfect_power(n)`: Checks if a number can be expressed as $a^b$ where $a>0$ and $b>1$.
28. `collatz_length(n)`: Returns the number of steps for $n$ to reach 1 in the Collatz conjecture.
29. `polygonal_numbers(n, s)`: Returns the $n$-th $s$-gonal number.
30. `is_carmichael(n)`: Checks if a composite number $n$ satisfies $a^{n-1} \equiv 1 \pmod n$ for all $a$ coprime to $n$ (Carmichael Number Check).
31. `is_prime_miller_rabin(n, k)`: Probabilistic Miller-Rabin primality test with $k$ rounds.
32. `pollard_rho(n)`: Integer factorization using Pollard's rho algorithm.

### Cryptography & Advanced Functions (Questions 22-24, 33-34)

22. `rsa_encrypt/decrypt`: Functions for RSA Encryption and Decryption.
23. `elgamal_encrypt/decrypt`: Functions for ElGamal Encryption and Decryption.
24. `rabin_encrypt/decrypt`: Functions for the Rabin Cryptosystem.
33. `zeta_approx(s, terms)`: Approximates the Riemann Zeta function $\zeta(s)$.
34. `simple_hash(data)`: A simple hash function that returns a small integer hash value.

## 🛠️ Technologies/Tools Used

* **Language:** Python 3.x
* **Version Control:** Git
* **Hosting:** GitHub (assumed)

## 💻 Steps to Install & Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone [Your-GitHub-Repository-URL]
    cd [Your-Project-Name]
    ```

2.  **Ensure Python is Installed:**
    This project requires **Python 3.x**. You can check your version:
    ```bash
    python --version
    # or
    python3 --version
    ```

3.  **Run the Main Script (Example):**
    Assuming all functions are saved in a file named `math_functions.py`:
    ```bash
    python math_functions.py
    ```
    *Note: A primary script (e.g., `main.py`) should import and demonstrate the usage of the core functions.*

## ✅ Instructions for Testing

Unit tests ensure the correctness of all 34 functions.

1.  **Install a Test Runner:**
    It is recommended to use `pytest` for running tests:
    ```bash
    pip install pytest
    ```

2.  **Run the Tests:**
    Assuming a `test_functions.py` file contains the test cases, run them from the project root directory:
    ```bash
    pytest
    ```
