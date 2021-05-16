# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    '''This will allocate s two times'''
    s=s[::-1]
    print(s)

    '''For Inplace use reverse'''
    s.reverse()

reverseString(["h","e","l","l","o"])