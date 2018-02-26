#!/usr/bin/env python3
print(100+200+300)
#input使用
name = input('please enter your name: ')
print('hello',name)
#转义字符的使用
print('I\'m \"OK\"!')
#当需要转义\的时候，用\\
print('\\\n\\')
#还可以使用r''表示‘’内部的字符串默认不转义
print(r'\\\n\\')
#用'''...'''可以多行输入，效果同\n
print('''like
what
you''')
print('Boolen的使用:')
print('5 > 3',5 > 3)
print('5 < 3',5 < 3)
print('and ,or ,not的使用：')
print('True and True :',True and True)
print('True and False :',True and False)
print('3 > 2 or 4 > 7 :',3 > 2 or 4 > 7)
