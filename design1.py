#!/usr/bin/env python3
n=int(input('Enter the number of rows:'))
while n>=0:
    x='*'*n
    print(x)
    n-=1  #第一行打印n个*，之后每一次循环n都减1，每一行就少打一个*
