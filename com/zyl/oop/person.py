#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: person
# @Date    : 2018-01-08 14:24
# @Author  : zhuyl

class Person(object):
    """这是一个person类"""
    nationality = "China"

    def __init__(self, name):
        self.name = name

    def fun1(self):
        pass

    def __fun1(self):
        pass

    @classmethod
    def fun2(cls):
        pass

    @staticmethod
    def fun3():
        pass

