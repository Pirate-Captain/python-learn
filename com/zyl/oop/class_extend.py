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

"""
继承层级关系中子类的实例对象对属性的查找顺序问题
新式类 与 经典类

Python 2.2引入了新式类，与它对应的是经典类，这里我们仅仅是解释下他们的概念，为讲解下面的内容做铺垫，不会深入讨论的它们的之间的区别。
这里我们主要说明一下几个点就可以了：

    Python 2.x中，默认是经典类，只有显示继承了object的才是新式类；
    Python 3.x中，默认就是新式类，经典类已经被废弃；
    新式类的子类也是新式类

深度优先 与 广度优先

深度优先 可以理解为 纵向优先，广度优先 可以理解为 水平方法优先。我们知道，类与类之间是有层级关系的，父类与子类是纵向的层级关系，同一个父类的多个
直接子类是水平方向的同级关系。
   A
B     c
   D
上图中 A是父类、B和C是继承A的子类，D是同时继承B和C的子类。此时D的一个实例对象去查找一个父类中的属性或方法的查找顺序就有两种可能，但是这两种查
找顺序中第一个查找的父类必然都是B：

    B-->A-->C：这就是深度优先，因为优先查找的是与B上一层级的、纵向的A
    B-->C-->A：这就是广度优先，因为优先查找的是与B同一层极的、水平方向的C
    
前面我们已经说过了 在Python 3.x中无论是否显示指定继承object，所有的类都是新式类，那么我们根据上面的两个实例的输出结果可以得出这样的结论：
在多继承的情况下，经典类查找父类属性或方法的顺序是深度优先，新式类查找父类属性的顺序是广度优先。

"""


class A(object):
    def fun1(self):
        print("a fun1")

    def fun2(self):
        print("a fun2")

    def fun3(self):
        print("a fun3")


class B(A):
    def fun2(self):
        print("b fun2")


class C(A):
    def fun2(self):
        print("c fun2")

    def fun3(self):
        print("c fun3")


class D(B, C):
    pass


d = D()
d.fun1()
d.fun2()
d.fun3()
