#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: del_method
# @Date    : 2018-01-08 14:58
# @Author  : zhuyl

list1 = list(range(1, 20))

del list1[5:10]
print(list1)

dic1 = {"key1": 11, "key2": 22, "key3": 33}
del dic1["key1"]
print(dic1)

# set1 = {11, 22, 33, 44, 11}
# del set1[0:2]
# print(set1)
