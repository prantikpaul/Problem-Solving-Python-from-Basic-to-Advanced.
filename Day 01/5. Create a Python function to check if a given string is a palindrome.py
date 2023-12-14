#5. Create a Python function to check if a given string is a palindrome.py

enter_str = input('Enter a string :')


reverse_str=enter_str[::-1]

if enter_str == reverse_str :
    print('Yes this string is a palindrome')
else :
    print('No this string is not a palindrome')


