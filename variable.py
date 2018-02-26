#!/usr/bin/env python3
#-*- coding: utf-8 -*-
print('变量名必须是大小写英文,数字,和_的组合，且不能用数字开头')
a = 123
print(a)
a = 'adv'
print(a)
print('常量：用全部大写的变量名表示常量，例如：PI = 3.14159265359')
print('9/3 = ',9/3)
print('地板除(//)：只保留整数部分,例如：7//4 = ',7//4)
print('''\nPython 字符串是以Unicode编码的,所以说,Python的字符串支持多语言
ord()函数获取字符的整数表示,chr()把编码转换为对应的字符''')
print('ord(\'A\') = ', ord('A'),'; chr(20013) =',chr(20013))
print('len()用于计算str的字符数,例如:len(\'新年快乐\') = ', len('新年快乐'))
print('%2d-%02d' %(3,1))
name='yyq'
age=25
print('Python 输出格式化的字符串，类似：name is xxx,age is xxx')
print('%运算符就是用来格式化字符串的,%s表示字符串替换,%d表示整数替换,%f表示浮点数替换,%x表示十六进制替换')
print('my name is %s,age is %d' %(name,age))
print('\n当有时候需要%表示字符的时候,百分号,用%%来表示一个百分号')
print('rate is : %d %%'%7)
