#!/usr/bin/env python3
n=int(input('Enter the number of students:'))
#输入学生的总数n
data={} #集合内的元素是不重复的，经过基础语言的编写使其可以进行数学上
        #集合的交并运算，大括号是集合的标志，{}与set()都可以创建集合
        #集合内不同的字符串之间也是用逗号分割的
        #当set()中没有逗号，只有一个单词字符串时，则把该单词字符串的
        #每一个字母都用逗号分开当成新的字符串
        #set()用来创建空集，{}用来创建空字典
        #字典是无序键对的集合{'kusha':'Fedora',}顿号前的是键，后面的是值
        #顿号前后都是字符串，键对之间用逗号隔开
        #键是为了方便检索的，键就相当于列表[]中字符串的索引0,1,2,3
        #结合列表符[],利用键可以检索键对应的值，也可以创建新的键值对
        #检索：data['kusha']  'Fedora'  创建：data['kusha']='Fedora'
        #data  {'kusha':'Fedora'}
        #键是不可变的，所以列表[]不能当做键
        #dict((('kusha','Fedora'),))  dict可从形似词典的双小括号的元组
        #中创造词典
        #xx.items()可以将词典中的键值对以两个对应的变量导出，就像0 kusha一样
        #重置默认值xx.setdefault('0',[]).append('Fedora')给字典中的键值添加列表数据
        #xx  {'0':['Fedora']} 原键存在则覆盖，不存在则创建
        #枚举函数enunerate()，括号内可以是列表、集合、元组等任何序列类型
        #enumerate()将使序列中以逗号隔开的字符串对应其默认索引值列成两列
        #zip()可以使两个序列按照相同的索引值列成两列
        #for x,y in zip(['a','b','c'],['1','2','3'])  print(x,y)
Subjects=('Physics','Math','History')
#创建以逗号分割字符串的元组，元组里的元素/字符串是不可变的
#只要有逗号，带小括号或者不带括号都是元组的标志
#type(123)是整数，type(123,)是元组
for i in range(1,n+1):
    name=input('Enter the name of students{}:'.format(i))
    #输入第i+1个学生的姓名，并赋给变量name
    marks=[] #创建空列表marks,列表是可以用逗号分割的，但它的标志是要有[]
    #列表[]不同于集合，它其中的元素/字符串是可变的，也可重复
    #可用xx.append()在列表[]中添加新的字符串，并默认用逗号隔开
    #a=[1,2]  a.append(3)  a  [1,2,3]
    for x in Subjects: #输入每一个学科的分数，并用xx.append()添加进空列表marks里面
        marks.append(int(input('Enter marks of {}:'.format(x))))
    data[name]=marks  #创建姓名与分数对应的键值对 'wo':[100,90,80]
    print(data)
    #{'wo': [100, 90, 80]}
    print(x)
for x,y in data.items():
    print(x, y)
    total=sum(y)
    print('{}\'s total marks {}'.format(x,total))
    if total<120:
        print(x,'failed :(')
    else:
        print(x,'passed :)')
