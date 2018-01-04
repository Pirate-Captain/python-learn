#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: class_extend
# @Date    : 2018-01-04 17:03
# @Author  : zhuyl

"""
1. 继承的相关概念

继成 和 组合 是类的两个最主要的关系，而 继承 关系的类之间是有层级的。被继承的类被称为 父类、基类 或 超类 ；继承的类被称为 子类 或 派生类。
2. 继承的作用

继承 是一个从一般到特殊的过程， 子类可以继承现有类的所有功能，而不需要重新实现代码。简单来说就是 继承提高了代码重用性和扩展性。
3. 继承的分类

Python中类的继承按照父类中的方法是否已实现可分为两种：

    实现继承 ：指直接继承父类的属性和已定义并实现的的方法；
    接口继承 ：仅继承父类类的属性和方法名称，子类必须自行实现方法的具体功能代码。

如果是根据要继承的父类的个数来分，有可以分为：

    单继承： 只继承1个父类
    多继承： 继承多个父类
    通常，我们都是用 单继承 ，很少用到 多继承。

4. 类继承实例
子类需要在自己的__init__方法中的第一行位置调用父类的构造方法，下面给出了两种方法：
super(子类名, self).__init__(父类构造参数)，如super.(Teacher, self).__init__(name, age)
父类名.__init__(self, 父类构造参数)，如Person.__init__(self, name, age)，这是老式的用法。
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("%s is walking" % self.name)

    def talk(self):
        print("%s is talking" % self.name)


class Teacher(Person):
    def __init__(self, name, age, level, salary):
        super(Teacher, self).__init__(name, age)
        self.level = level
        self.salary = salary

    def teach(self):
        print("%s is teaching" % self.name)


class Student(Person):
    def __init__(self, name, age, class_):
        Person.__init__(self, name, age)
        self.class_ = class_

    def study(self):
        print("%s is study" % self.name)


teacher = Teacher("张老师", 40, 1, 5000)
student = Student("王小明", 10, "数学")

teacher.walk()
teacher.talk()
teacher.teach()

student.walk()
student.talk()
student.study()
