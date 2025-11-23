import time
start=time.perf_counter()

def digital_root(n):
    while n > 10:
        n = sum(int(digit) for digit in str(n))
    return n
end=time.perf_counter()
execution=end-start
print("time required=",(execution))
x= int(input("enter digit="))
print (digital_root(x) )

