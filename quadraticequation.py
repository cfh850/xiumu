#!/usr/bin/env python3
import math
a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
c=int(input('Enter value of c:'))
d=b*b-4*a*c
if d<0:
    print('ROOTS are imaginary')
else:
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    # math.sqrt自math函数模块中引用了sqrt求平方根函数
    print('Root1=',root1)
    print('Root2=',root2)

# x*x+2x+1=0,a=1,b=2,c=1,root1=-1,root2=-1
# x*x+x+1=0,a=1,b=1,c=1,d=-3,roots=imaginary
# x*x+4x+3=0,a=1,b=4,c=3,d=16-4*3=4,root1=-1,root2=-3
