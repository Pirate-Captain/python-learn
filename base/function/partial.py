#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools

"""
偏函数
functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
"""

print(int("12345", base=8))


def int10(value):
    return int(value, base=10)


print(int10("123456"))

print(functools.partial(int, base=10)("123456"))
