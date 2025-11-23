def collatz_length(n):
    steps = 0
    while n != 1 :
        if n%2 == 0 :
            n=n//2
        else:
            n = 3*n+1
        steps += 1
    return steps

num = int( input("enter a positive integer to find its collatz sequence length:"))

length = collatz_length(num)
print ( f" it takes {length} steps for {num} to reach 1 in the collatz sequence. ")
