#8. Given a list of integers, find the sum of all positive numbers.py

num_to_add = int(input('How many numbers u wanna check ? '))
num=[]
for i in range(num_to_add):
    Get_num=int(input('Enter numbers , if negetive then must include "-" : '))
    num.append(Get_num)
print(num)

sum=0
for i in num:
    if i > 0 :
        sum+=i

print(f'The sum of all positive num is : {sum}')
