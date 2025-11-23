def partition_function(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]

n = int(input("Enter a positive integer to find its partition number p(n): "))

result = partition_function(n)

print(f"The number of distinct partitions of {n} is: {result}")
