#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: property
# @Date    : 2018-01-04 16:22
# @Author  : zhuyl

import uuid

"""
公有属性/类属性

直接定义在class下的属性就是公有属性/类属性，比如下面那个Person类中的nationality属性。“公有”的意思是这个属性是这个类的所有实例对象共同所有的，
因此默认情况下这个属性值值保留一份，而不会为该类的每个实例都保存一份。

结论：

- 公有属性/静态属性 可以直接通过类直接访问，也可以直接通过实例进行访问；
- 通过类的某个实例对公有属性进行修改，实际上对为该实例添加了一个与类的公有属性名称相同的成员属性，对真正的公有属性是没有影响的，因此它不会影响其他
  实例获取的该公有属性的值；
- 通过类对公有属性进行修改，必然是会改变公有属性原有的值，他对该类所有的实例是都有影响的（已添加过与公有属性名称相同的成员属性的实例，将不受影响）。
"""


class Person(object):
    nationality = "China"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = str(uuid.uuid1())

    def hello(self):
        print("I am %s, from %s, I am %s now, id is %s" % (self.name, self.nationality, self.age, self.__id))


tom = Person("Tom", 20)
jack = Person("Jack", 30)
mike = Person("Mike", 25)

print(Person.nationality, tom.nationality, jack.nationality, mike.nationality)
tom.nationality = "USA"
print(Person.nationality, tom.nationality, jack.nationality, mike.nationality)
Person.nationality = "INDIA"
print(Person.nationality, tom.nationality, jack.nationality, mike.nationality)

"""
成员属性/实例属性

成员属性，又称成员变量 或 实例属性，也就是说这些属性是 该类的每个实例对象单独持有的属性。成员属性需要在类的__init__方法中进行声明，
比如上面的Person类中定义的name属性就是一个成员属性。

结论：

- 成员属性可以直接通过实例对象来访问和更改；
- 成员属性是每个实例对象独有的，某个实例对象的成员属性被更改不会影响其他实例对象的相同属性的值；
- 成员属性的值不能通过类来访问和修改；
"""

print(tom.name)

"""
私有属性

私有属性和成员属性一样，是在__init__方法中进行声明，但是属性名需要以双下划线__开头，比如上面定义的Person中的__id属性。私有属性是一种特殊的成
员属性，它只允许在实例对象的内部（成员方法或私有方法中）访问，而不允许在实例对象的外部通过实例对象或类来直接访问，也不能被子类继承。

结论：

- 私有变量不能通过类直接访问；
- 私有变量也不能通过实例对象直接访问；
- 私有变量可以通过成员方法进行访问。

那么要访问私有变量怎么办呢？ 有两种办法：
办法1：通过一个专门的成员方法返回该私有变量的值
办法2：通过 实例对象._类名__私有变量名 的方式来访问
"""
print(tom.hello())
print(tom._Person__id)

"""
总结

    公有属性、成员属性 和 私有属性 的受保护等级是依次递增的；
    私有属性 和 成员属性 是存放在已实例化的对象中的，每个对象都会保存一份；
    公有属性是保存在类中的，只保存一份；
    哪些属性应该是公有属性的，哪些属性应该是私有属性 需要根据具体业务需求来确定。

"""
