#6. Calculate the compound interest for a given principal amount, interest rate, and time period.py

p =int(input('Enter your principal amount :'))
while p is None:
    p =int(input('Enter your principal amount :'))
r =int(input('Enter your interest rate :'))
n =int(input('Enter your number of times that interest is compounded per year :'))
t =int(input('Enter your time period :'))

r = r / 100 # converting to % for interest 
a = p * (1+(r/n))**(n*t)

print(a)
