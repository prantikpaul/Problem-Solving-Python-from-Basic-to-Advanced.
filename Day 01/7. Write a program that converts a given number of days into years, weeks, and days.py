#7. Write a program that converts a given number of days into years, weeks, and days.py

day = int(input('Please Enter Nums of days to covert :'))

to_get_num_of_year=int(day/365) #this will get how many yrs
to_get_num_of_days_left=day%365  # this will get how days left after yrs

to_get_num_of_month=int(to_get_num_of_days_left/30) #this will get how many months
to_get_num_of_days_left=to_get_num_of_days_left%30 # this will get how days left after months

to_get_num_of_week=int(to_get_num_of_days_left/7) #this will get how many weeks
to_get_num_of_days_left=to_get_num_of_days_left%7 # this will get how days left after week


print(f'According to your given numbers of days there will be {to_get_num_of_year} years ,{to_get_num_of_month} months ,{to_get_num_of_week} weeks and {to_get_num_of_days_left} days ')

