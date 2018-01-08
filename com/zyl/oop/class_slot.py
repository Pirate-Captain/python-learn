#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: class_slot
# @Date    : 2018-01-08 11:40
# @Author  : zhuyl

from types import MethodType

"""
动态绑定属性以及方法
"""


class Person(object):
    pass


p = Person()
p.name = "张三"
p.age = 30

print(p.name)


def get_name(self):
    return self.name


p.get_name = MethodType(get_name, p)
print(p.get_name())

"""
但是，给一个实例绑定的方法，对另一个实例是不起作用的
为了给所有实例都绑定方法，可以给class绑定方法
"""


def get_age(self):
    return self.age


Person.get_age = get_age
print(p.get_age())

"""
__slots__
如果我们想要限制实例的属性，只允许添加指定的属性，则可以使用__slots__
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
"""


class Student(object):
    __slots__ = ("name", "age")
    pass


s1 = Student()
s1.age = "20"
s1.name = "张三"
# s1.sex = "MALE"
print(s1.age)
print(s1.name)


class SeniorStudent(Student):
    __slots__ = ("sex")
    pass


ss = SeniorStudent()
ss.name = "李四"
ss.age = 20
ss.sex = "MALE"
# ss.class_info = "English"
print(ss.sex)
