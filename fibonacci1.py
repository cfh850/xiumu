#!/usr/bin/env python3
a=0
b=1
while b<100:
    # print(b)
    # (a,b)=(b,a+b)
    print(b,end=' ')  # ,end=''是为了指出这次打印以什么形式结尾，
                      # 若不写,end''则默认以换行符\n结尾
    a,b=b,a+b      # a=0 1 1 2 3
                   # b=1 1 2 3 5
print()  #指全部打印完以空缺结尾，如果没有这一句则默认以%结尾
