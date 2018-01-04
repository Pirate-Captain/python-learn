#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: class_method
# @Date    : 2018-01-04 17:27
# @Author  : zhuyl

import uuid

"""
类中封装的是数据和操作数据的方法。数据就是属性，且上面已经介绍过了属性分为：
公有属性/类变量、成员属性/实例变量 和 私有属性。现在我们来说说类中的方法，类中的方法分为以下几种：

    成员方法： 上面定义的都是成员方法，通常情况下，它们与成员属性相似，是通过类的实例对象去访问；成员方法的第一个参数必须是当前实例对象，
             通常写为self；实际上，我们也可以通过类名来调用成员方法，只是此时我们需要手动的传递一个该类的实例对象给成员方法的self参数，
             这样用明显不是一种优雅的方法，因此基本不会这样使用。

    私有方法： 以双下划线开头的成员方法就是私有方法，与私有属性类似，只能在实例对象内部访问，且不能被子类继承；私有方法的第一个参数也必须是当
             前实例对象本身，通常写为self；

    类方法： 以@classmethod来装饰的成员方法就叫做类方法，它要求第一个参数必须是当前类。与公有属性/静态属性 相似，除了可通过实例对象进行访问，
            还可以直接通过类名去访问，且第一个参数表示的是当前类，通常写为cls；另外需要说明的是，类方法只能访问公有属性，不能访问成员属性，
            因此第一个参数传递的是代表当前类的cls，而不是表示实例对象的self。

    静态方法： 以@staticmethod来装饰的成员方法就叫做静态方法，静态方法通常都是通过类名去访问，且严格意义上来讲，静态方法已经与这个类没有
             任何关联了，因为静态方法不要求必须传递实例对象或类参数，这种情况下它不能访问类中的任何属性和方法。

    属性方法： 这个比较有意思，是指可以像访问成员属性那样去访问这个方法；它的第一个参数也必须是当前实例对象，且该方法必须要有返回值。

"""


class Person(object):
    nationality = "China"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = str(uuid.uuid1())

    def say_hello(self):
        print("%s is saying hello" % self.name)

    @classmethod
    def fun1(cls):
        print(cls.nationality)

    @staticmethod
    def fun2(a, b):
        print(a + b)

    @property
    def id(self):
        return self.__id


person = Person("李四", 40)
person.say_hello()
person.fun1()
person.fun2(10, 20)
Person.say_hello(person)
Person.fun1()
Person.fun2(10, 20)
print(person.id)
