#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import functools

"""
1. 什么是装饰器？

装饰器，是一种“语法糖”，其本质上就是个函数。
2. 装饰器的作用

它是一个装饰其他函数的函数，用来为其他函数添加一些额外的功能。
3. 装饰器原则

装饰器对被装饰的函数应该是完全透明的，即

    不能修改被装饰的函数的源代码
    不能修改被装饰的函数的调用方式

4. 什么样的函数才是装饰器？

高阶函数 + 嵌套函数 => 装饰器

这里的高阶函数需要同时满足以下两个条件：

    接收函数名作为参数 -- 可以实现在不修改被装饰函数源代码的情况下为其添加新的功能
    返回内部嵌套函数的函数名 -- 可以实现不用修改函数的调用方式

注意要解决 内部wrapper函数名的问题：functools.wrapper
"""


# 装饰器不带参数的情况
def print_run_time(f):
    def wrapper(*args, **kw):
        time_start = time.time()
        result = f(*args, **kw)
        time_end = time.time()
        print("%s run time %s" % (f.__name__, (time_end - time_start)))
        return result

    return wrapper


@print_run_time
def fun1(message):
    print(message)
    time_start = time.time()
    time.sleep(2)
    time_end = time.time()
    print("func1 耗时：", (time_end - time_start))


@print_run_time
def fun2(message):
    print(message)
    time_start = time.time()
    time.sleep(1)
    time_end = time.time()
    print("fun2 耗时：", (time_end - time_start))


fun1("hello")
print("fun1.__name__:%s" % fun1.__name__)
fun2("world")
print("fun2.__name__:%s" % fun2.__name__)


# 装饰器也带有参数的情况
def print_run_time2(timeout=2):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            time_start = time.time()
            result = f(*args, **kw)
            time_end = time.time()
            run_time = time_end - time_start
            print("%s run time %s" % (f.__name__, run_time))
            if run_time > timeout:
                print("PROBLEM".rjust(30, ">"))
            return result

        return wrapper

    return decorator


@print_run_time2(timeout=1)
def fun3(message):
    print(message)
    time_start = time.time()
    time.sleep(2)
    time_end = time.time()
    print("func1 耗时：", (time_end - time_start))


@print_run_time2(timeout=1)
def fun4(message):
    print(message)
    time_start = time.time()
    time.sleep(1)
    time_end = time.time()
    print("fun2 耗时：", (time_end - time_start))


fun3("hello")
print("fun3.__name__:%s" % fun3.__name__)
fun4("world")
print("fun4.__name__:%s" % fun4.__name__)
