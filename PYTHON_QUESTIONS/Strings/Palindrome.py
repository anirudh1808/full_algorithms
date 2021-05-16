# Code -- https://practice.geeksforgeeks.org/problems/palindrome-string0817/1

def isPalidrome(s):
    if s==s[::-1]:
        print('Palindrome')
    else :
        print('Not Palindrome')

isPalidrome('madam')
isPalidrome('madama')