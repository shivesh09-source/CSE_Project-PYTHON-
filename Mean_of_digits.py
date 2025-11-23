import time 
start_time = time.perf_counter()
def mean_of_digits(n):
    total = 0   
    count = 0  
    
    n = abs(n)  
    
    while n > 0:
        digit = n % 10      
        total += digit      
        count += 1         
        n = n // 10        
    
    if count == 0:         
        return 0
    return total / count    
end_time= time.perf_counter()
execution_time= end_time - start_time
print(f"execution time=",(execution_time),"seconds")
print(f"mean of digits in number", mean_of_digits(642))   