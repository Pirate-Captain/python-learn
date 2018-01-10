#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: with_express
# @Date    : 2018-01-10 14:58
# @Author  : zhuyl

"""
自定义上下文管理器

开发人员可以自定义支持上下文管理协议的类。自定义的上下文管理器要实现上下文管理协议所需要的 __enter__() 和 __exit__() 两个方法：

    context_manager.__enter__() ：进入上下文管理器的运行时上下文，在语句体执行前调用。with 语句将该方法的返回值赋值给 as 子句中的 target，
    如果指定了 as 子句的话
    context_manager.__exit__(exc_type, exc_value, exc_traceback) ：退出与上下文管理器相关的运行时上下文，返回一个布尔值表示是否对发生
    的异常进行处理。参数表示引起退出操作的异常，如果退出时没有发生异常，则3个参数都为None。如果发生异常，返回

    True 表示不处理异常，否则会在退出该方法后重新抛出异常以由 with 语句之外的代码逻辑进行处理。如果该方法内部产生异常，则会取代由 statement-body
    中语句产生的异常。要处理异常时，不要显示重新抛出异常，即不能重新抛出通过参数传递进来的异常，只需要将返回值设置为 False 就可以了。之后，上下文管理
    代码会检测是否 __exit__() 失败来处理异常
"""


class TestWith(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("%s Access enter" % self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("%s exit ok" % self.name)
        else:
            print("%s exit error" % self.name)
            # return True


testWith = TestWith("zhangsan")
with TestWith("张三"):
    pass
with TestWith("李四"):
    raise AttributeError("error")
