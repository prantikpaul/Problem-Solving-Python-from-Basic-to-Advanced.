#1. Given a list of numbers, find the sum and average 

pp = input('Enter list of numbers,add space between them : ')

rr=pp.split()

l=[]

for i in rr :
    l.append(int(i))

sum_of_num=sum(l)

print(f'sum of numbers are : {sum_of_num}')

avg_of_num = sum_of_num / len(l)
print(f'avg of numbers are : {avg_of_num}')

