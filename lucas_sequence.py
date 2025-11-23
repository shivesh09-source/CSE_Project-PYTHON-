def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    lucas_nums = [2, 1]
    for i in range(2, n):
        next_val = lucas_nums[i-1] + lucas_nums[i-2]
        lucas_nums.append(next_val)
    return lucas_nums

n = int(input("Enter the number of Lucas numbers to generate: "))

sequence = lucas_sequence(n)
print(f"The first {n} Lucas numbers are: {sequence}")
