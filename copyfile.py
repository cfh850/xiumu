#!/usr/bin/env python3
import sys
print(sys.argv)  # sys.argv是指shell界面输入的命令行参数
                 # sys.argv(当前系统文件中的命令行参数)
if len(sys.argv)<3:  # len()统计括号内有几个由空格隔开的字符串/单词
    print('Wrong parameter')
    print('./copyfile.py file1 file2')
    sys.exit(1)  # 退出系统文件模块
f1=open(sys.argv[1]) # sys.argv[0]是命令行参数中的第一个字符串,
                     # 这里便是命令自身的名字(./copyfile.py)
                     # sys.argv[1]是命令行参数中的第二个字符串，即file1
                     # sys.argv[2]是命令行参数中的第三个字符串，即file2
s=f1.read()          # 打开file1，临时缓存在f1上，
                     # 读取f1的内容，并将其内容以字符串的格式赋值给变量s
f1.close()           # 关闭临时缓存f1
f2=open(sys.argv[2],'w')
f2.write(s)          # 向临时缓存f2中重新写入变量s所指代的字符串
f2.close()
