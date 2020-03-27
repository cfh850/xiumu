#!/usr/bin/env python3
s=input('Please enter a string:')
z=s[::-1]  # 对字符串每隔-1个字符进行取值，即把字符串倒过来写
if s==z:
    print('The string is a palindrome')
else:
    print('The string is not apalindrome')
