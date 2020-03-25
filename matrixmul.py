#!/usr/bin/env python3
n=int(input('Enter the value of n:'))  #n是矩阵的阶数
print('Enter value for the Matrix A')
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()]) #中括号里是列表推导式
    #input()获得用户输入的含空格字符串，split()分割含空字符串成多个数字字符串
    print(a)  #1 2 3  a=[[1,2,3]]  2 3 4  a=[[1,2,3],[2,3,4]]
print('Enter value for the Matrix B')
b=[]
for i in range(n):
    b.append([int(x) for x in input().split()])
    print(b)
c=[]
for i in range(n):
    c.append([a[i][j]*b[i][j] for j in range(n)])#A矩阵的第1行要乘上B矩阵的某列
    print(c)
print('After matrix multiplication')
print('-'*7*n)
for x in c:  #准备打印C矩阵
    for y in x:
        print(str(y).rjust(5),end='') #打印标准的方形C矩阵
        #sty()将数字y改成字符串格式，xx.rjust(5)在每个字符串y之间跳过5个空格
        #结尾处用end=''取消默认换行
    print()  #结尾处什么都不打印则默认换行
print('-'*7*n)
