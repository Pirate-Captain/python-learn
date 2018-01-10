#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: Person
# @Date    : 2018-01-10 10:52
# @Author  : zhuyl

"""
test UpperAttribute
"""

from com.zyl.yuanlai.module.upperatrribute import UpperAttribute


class Person(object, metaclass=UpperAttribute):
    bar = 'bip'


person = Person()
print(hasattr(person, "BAR"))
