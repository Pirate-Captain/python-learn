#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: class_define_init
# @Date    : 2018-01-04 15:25
# @Author  : zhuyl

"""
1. 类的定义

类的定义是对显示事务的抽象过程和能力，类是一个对象/实例的模板，也是一个特殊的对象/实例（因为Pythobn中一切皆对象，所以类本身也是一个对象）
"""


class Person(object):
    nationality = "China"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hi, I am %s, from %s, I am %s now" % (self.name, self.nationality, self.age))


tom = Person("Tom", 20)
tom.hello()
