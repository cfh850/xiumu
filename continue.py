#!/usr/bin/env python3
while True:
    n=int(input('Please enter an Integer:'))
    if n<0:
        continue  # continue会返回到while循环内的开始处执行
    elif n==0:
        break     # break会跳出while的循环
    print('Square is',n**2)
print('Goodbye')
