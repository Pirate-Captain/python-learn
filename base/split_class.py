#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: split_class
# @Date    : 2018-01-08 11:10
# @Author  : zhuyl

import uuid

"""
拆分python对象内部信息
"""

"""
dir
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
"""

print(dir("hello"))


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = str(uuid.uuid1())

    def get_id(self):
        return self.__id

    @staticmethod
    def fun1(x, y):
        print(x + y)

    @classmethod
    def fun2(cls):
        print(cls.__id)

    @property
    def id(self):
        return self.__id


print(dir(Person("张三", 30)))

"""
len
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法
"""
print("ABC".__len__())
print(len("ABC"))


class P1(object):
    def __len__(self):
        return self.__sizeof__()


p = P1()
print(len(p))
print(p.__len__())
p.name = "zhangsan"
print(len(p))

"""
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
"""


class P2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = str(uuid.uuid1())

    def get_name(self):
        return self.name

    def get_id(self):
        return self.__id


p2 = P2("张三", 30)
print(hasattr(p2, "name"))
print(hasattr(p2, "age"))
print(hasattr(p2, "__id"))
print(getattr(p2, "name"))
print(getattr(p2, "__id", "None"))
setattr(p2, "name", "李四")
print(getattr(p2, "name"))

get_name_bak = getattr(p2, "get_name")
print(get_name_bak)
