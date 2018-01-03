#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
嵌套函数

嵌套函数是指在函数内部定义一个函数，这些函数都遵循各自的作用域和生命周期规则。
"""


def outer():
    level = 1
    print("outer", level)

    def inner():
        print("inner", level)

    inner()


outer()


def outer1():
    level = 1
    print("outer", level)

    def inner():
        level = 2
        print("inner", level)

    inner()

    print("outer-new", level)


outer1()

"""
 闭包

首先要说明一个问题：函数名其实也是一个变量，我们通过def定义一个函数时，实际上就是在定义一个变量，函数名就是变量名称，函数体就是该变量的值。
我们知道，变量是可以赋值给其他变量的，因此函数也是可以被当做返回值返回的，并且可以赋值给其他变量。

闭包的定义

  如果在一个内部函数中，引用了外部非全局作用域中的变量，那么这个内部函数就被认为是闭包(closure)。
  
  Ptyhon支持一种特性叫做函数闭包（function closres），它的工作原理是：在非全局（global）作用域（函数）中定义inner函数时，这个inner函数会
  记录下外层函数的namespaces（外层函数作用域的locals，其中包括外层函数局部作用域中的所有变量），可以称作：定义时状态，inner函数可以通过
  __closure__（早期版本中为func_closure）这个属性来获得inner函数外层嵌套函数的namespaces。其实我们可以通过打印一个函数的__closesure__
  属性值是否为None来判断闭包是否发生。
"""
