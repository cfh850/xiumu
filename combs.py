#!/usr/bin/env python3
combs=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
# combs
# (1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 【列表推导式由中括号里的变量表达式后跟for和if组成，】
# 【for后是单个变量需要满足的条件，if后是多个变量之间需要满足的条件，】
# 【不满足if条件的变量组将不会代入变量表达式中】
# 等价于
combs=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(combs)
# combs
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

a=[1,2,3]
z=[x+1 for x in [x**2 for x in a]]
# z
# [2, 5, 10]
print(z)
