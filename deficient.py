def is_deficient (n) :
    div_sum = 0
    for i in range (1,n):
        if n%i == 0:
            div_sum += i
    return div_sum<n
number = int ( input ("enter a number : "))    
if is_deficient (number)    :
    print(" Deficient ")
else:
    print ("Not deficient ")