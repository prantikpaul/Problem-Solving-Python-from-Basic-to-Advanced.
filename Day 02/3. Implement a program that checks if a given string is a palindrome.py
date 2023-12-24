#Implement a program that checks if a given string is a palindrome

def palindrome (s):
    
    reverse_str=s[::-1]

    if s == reverse_str :
       return print('Yes this string is a palindrome')
    else :
        return print('No this string is not a palindrome')

pp= input('Enter an string ')

palindrome(pp)