#!/usr/bin/env python3
import math
def longest_side(a,b):
    '''
    Function to find the length of the longest side of a right triangle.
    :arg a:Side a of the triangle
    :arg b:Side b of the triangle
    :return: Length of the longest side c as float
    '''  # 函数中的文本内容要用一对3引号(''' ''')夹起来，
         # 代表其内部只是文本不会被执行
    return math.sqrt(a*a+b*b)
if __name__=='__main__':
    print(longest_side.__doc__) #函数名.__doc__是指代函数中的文本内容
    print(longest_side(4,5))
