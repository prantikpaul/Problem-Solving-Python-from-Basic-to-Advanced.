#4. Given a list of numbers, find the maximum and minimum values.

num=int(input('How many numbers u want to add ?'))

list=[]

for i in range(num):
    take_input=int(input('Input your numbers : '))
    list.append(take_input)
print(f'Your list of numbers are {list}')

print('In your giving list the maximum num is ',max(list))
print('In your giving list the minimum num is ',min(list))
    

# by using max and min function we can find max num or min num 

#