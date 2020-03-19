#!/usr/bin/env python3
i=1
print('-'*50)  #字符串乘以整数n代表返回该字符串重复n次
while i<11:
    n=1
    while n<=10:
        print('{:5d}'.format(i*n),end='')
        n+=1  #当n等于11时，跳出里循环
    print()   #什么都不打印代表换行，即默认执行字符\n
    i+=1      #此时i=2，进入下一循环（外循环）后重新赋值n=1
print('-'*50)
