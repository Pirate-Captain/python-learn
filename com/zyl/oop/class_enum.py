#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: enum
# @Date    : 2018-01-09 16:24
# @Author  : zhuyl

from enum import Enum, unique

"""
枚举类
"""
Month = Enum('Month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

for name, member in Month.__members__.items():
    print(name, "==>", ',', member, member.value)


@unique
class WeekDay(Enum):
    SunDay = 0
    MonDay = 1
    TuesDay = 2
    WednesDay = 3
    ThirsDay = 4
    FriDay = 5
    SaturDay = 6


print(WeekDay.SunDay)
print(WeekDay["MonDay"])
print(WeekDay.SunDay.value)
print(WeekDay(1))
