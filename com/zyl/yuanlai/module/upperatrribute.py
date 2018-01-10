#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: UpperAttribute
# @Date    : 2018-01-10 10:44
# @Author  : zhuyl


"""
将属性转换为大写
"""


class UpperAttribute(type):
    def __new__(cls, cname, bases, attrs):
        upper_attrs = dict((name.upper(), value) for name, value in attrs.items() if not name.startswith("__"))
        print(cls)
        return super(UpperAttribute, cls).__new__(cls, cname, bases, upper_attrs)
