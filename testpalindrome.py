#!/usr/bin/env python3
def palindrome(s):#关键字def用来定义函数xx()，括号里放的是参数:def 函数名(参数):
    return s==s[::-1] #return后面是判断句，若为真则返回True，否则返回False
    # return返回后面判断语句的真假值给调用的函数，即新定义的模块函数palindrome()
if __name__=='__main__':  #判断前面调用的函数模块是不是直接被执行的模块，是的
    # 话_name__的值是__main__，不是的话则返回模块的真实名称
    # 判断前面的代码中是否调用了其它函数模块，调用了就返回调用模块的真实名称
    # 否则返回__main
    # 这里函数palindrome()是在这个模块里被定义的，也就是直接被执行的，返回__main__
    # 因为'__main__'=='__main__'，满足了if的条件，所以下面缩进后的语句得以执行
    s=input('Enter a string:')
    if palindrome(s):  #使用前面定义的函数palindrome()对s进行作用，字符串s将
        print('Yay a palindrome')  #倒写
    else:#因为调用的函数palindrome()为True,所以执行缩进句,打印‘哇，一个回文‘
        print('Oh no,not a palindrome')
