#!/usr/bin/env python3
a=9
def change():
    global a
    print(a)
    a=100
print('Before the function call', a)
print('inside change function',end=' ')  #打印完字符串不结尾，接连执行下一行
                                         #的change()函数，后者将再次打印a的值
                                         #等于9，并重新赋值a=100
                                         #所以再下一行打印a时，a=100
change()
print('After the function call', a)
