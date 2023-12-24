#Implement a program that swaps the values of two variables

def swap(a,b) :
    a = a + b
    b = a - b 
    a = a - b 

    return a , b 




var = int(input('Enter value for Variable 1 :'))
var2 = int(input('Enter value for Variable 2 :'))
print(swap(var,var2))
