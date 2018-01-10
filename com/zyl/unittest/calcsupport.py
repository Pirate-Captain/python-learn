#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: calcsupport
# @Date    : 2018-01-10 14:31
# @Author  : zhuyl

"""
简单的计算
"""


class CalcSupport(object):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def div(self):
        return self.param1 / self.param2

    def minus(self):
        return self.param1 - self.param2
