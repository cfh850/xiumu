#!/usr/bin/env python3
# days=int(input('Enter days:'))
# months=days//30
# days=days%30
# print('Months={}Days={}'.format(months,days))
days=int(input('Enter days:'))
print('Months={}Days={}'.format(*divmod(days,30)))
# divmod(,)返回2个值，一个是前者除后者的整数部分，一个是剩下的余数部分
# divmod()前的*用来拆封divmod()函数返回的元组
