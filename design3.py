#!/usr/bin/env python3
n=int(input('Enter the number of rows:'))
i=0
while n>=0:
    x=' '*i  #设法控制空格数，使每行的空格数加1
    y='*'*n
    print(x+y)
    n-=1
    i+=1
