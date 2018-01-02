#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字节类型的数据用带b前缀的单引号或双引号表示
x = b'mdfdfa'
print(x)

print("ABC".encode('utf-8'))

print('如果有来生，愿做一棵树，站成永恒，没有悲欢的姿势。一半在土里安详，一半在风中飞扬；一半倾洒阴凉，一半沐浴阳光。非常沉默，非常骄傲。'.encode('UTF-8'))

print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord("A"))
print(chr(125))
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('中国'))
print(len('中国'.encode('utf-8')))


# 占位符，在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hello %s' % 'world')