#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
在Python中有两种定义函数的方式：

    通过def关键字定义的函数：这是最常用的方式，前面已经介绍过
    通过lambda关键字定义的匿名函数：这是本次要说的主角
"""

"""
匿名函数的定义
语法：

lambda argument1, argument2, ... argumentN :expression using argments

冒号左边是函数的参数，冒号右边是一个整合参数并计算返回值的表达式。

匿名函数的特性：

    函数体只能包含一个表达式
    不能有return语句（表达式的值就是它的返回值）
    参数个数不限，可以有0个、1个或多个

"""


def add(x, y):
    return x + y


print((lambda x, y: x + y)(10, 20))
