def polygonal_number(s, n):
    """
    Returns the nth s-gonal number where s is the number of sides.
    Formula: ((s - 2) * n^2 - (s - 4) * n) // 2
    """
    return ((s - 2) * n * n - (s - 4) * n) // 2

s = int(input("Enter the number of sides of the polygon (s): "))
n = int(input("Enter which term number (n) you want: "))

result = polygonal_number(s, n)
print(f"The {n}-th {s}-gonal number is: {result}")
