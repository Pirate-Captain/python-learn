#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: class_special_property_method
# @Date    : 2018-01-08 14:14
# @Author  : zhuyl

from com.zyl.oop.person import Person

"""
1. 类的特殊成员属性
属性名称 	说明
__doc__ 	类的描述信息
__module__ 	表示当前操作的对象对应的类的定义所在的模块名
__class__ 	表示当前操作的对象对应的类名
__dict__ 	一个字典，保存类的所有的成员（包括属性和方法）或实例对象中的所有成员属性

实例对象.__dict__ 和 类.__dict__ 的值是不同的：实例对象.__dict__的值中只包含成员属性和私有属性，类.__dict__的值中包含公有属性/类属性和所有类型的方法；
__module__和__class__的值可用于反射来实例化一个类的对象
"""

person = Person("张三")
print(person.__doc__)
print(person.__module__)
print(person.__class__)
print(Person.__dict__)
print(person.__dict__)

"""
2. 类的特殊成员方法
方法名称 	说明
__init__ 	类构造方法，通过类创建对象时会自动触发执行该方法
__del__ 	析构方法，当对象在内存中被释放，会自动触发执行该方法。比如实例对象的作用域退出时，或者执行 del 实例对象操作时。
__str__ 	如果一个类中定义了__str__方法，那么在打印对象时默认输出该方法的返回值，否则会打印出该实例对象的内存地址。
__xxxitem__ 是指__getitem__、__setitem__、__delitem这3个方法，它们用于索引操作，比如对字典的操作，分别表示 获取、设置、删除某个条目。
            数据。可以通过这些方法来定义一个类对字典进行封装，从而可以对字典中key的操作进行控制，尤其是删除操作。
__new__ 	该方法会在__init__方法之前被执行，该方法会创建被返回一个新的实例对象，然后传递给__init__。另外需要说明的是，这不是一个成员方法，
            而是一个静态方法。
__call__ 	源码中的注释是"Call self as a function." 意思是把自己（实例对象）作为一个函数去调用，而函数的调用方式是函数名()。也就是说，
            当我们执行实例对象()或者 类名()()这样的操作时会触发执行该方法。
__iter__    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的
            for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
__getattr__ 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错: AttributeError: 'xxx' object has no attribute 'cccc'
            写一个__getattr__()方法，动态返回一个属性
"""


class Person1(object):
    def __call__(self, *args, **kwargs):
        print(self.name, "__call__")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, "__init__")

    def __del__(self):
        print(self.name, "__del__")

    def __str__(self):
        print(self.name, "__str__")
        return "%s: %s" % (self.name, self.age)


p = Person1("张三", 40)
print(p)
p()

"""
定义一个类似字典的类



    可见，如果一个类实现了__setitem__，__getitem、__delitem 这几个方法，就可以执行一些类似字典一样的操作，比如上面用到的：

        my_dict['KEY'] 会自动调用my_dict实例对象的__getitem__方法；
        my_dict['KEY'] = VALUE 会自动调用my_dict实例对象的__setitem__方法；
        del my_dict['KEY'] 会自动调用my_dict实例独享的__delitem__方法；
        而我们定义这样一个类的目的在于，我们可以更好对字典操作进行控制，比如上面的例子中我们不允许删除key以'wh'开头的条目。


"""


class MyDict(object):
    def __init__(self, init=None):
        self.__dict = init if init is not None else {}

    def __setitem__(self, key, value):
        print("__set__", key)
        self.__dict[key] = value

    def __getitem__(self, item):
        print("__get__", item)
        return self.__dict.get(item, None)

    def __delitem__(self, key):
        print("__del__", key)
        if key is not None and key.startswith("wh"):
            print("you can't delete key")
            return None
        return self.__dict.pop(key, None)


my_dict = MyDict(init={"what": "打豆豆", "who": "企鹅团", "time": "吃饱睡好之后"})
print(my_dict["what"], my_dict["who"], my_dict["time"])

my_dict["num"] = "10次"
print(my_dict["what"], my_dict["who"], my_dict["time"], my_dict["num"])
del my_dict["num"]
print(my_dict["num"])
del my_dict["what"]
print(my_dict["what"])

"""
__iter__    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的
            for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
"""


class IterClass(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a


for n in IterClass():
    print(n)

"""
__getattr__ 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错: AttributeError: 'xxx' object has no attribute 'cccc'
            写一个__getattr__()方法，动态返回一个属性
"""


class GetAttr(object):
    def __init__(self):
        self.name = "Mike"

    def __getattr__(self, item):
        if item == "age":
            return 20
        raise AttributeError("'GetAttr' object has no attribute %s" % item)


ga1 = GetAttr()
print(ga1.name)
print(ga1.age)


# print(ga1.score)


class Chain(object):
    def __init__(self, path):
        self.path = path

    def __getattr__(self, item):
        return Chain("%s/%s" % (self.path, item))

    def __str__(self):
        return self.path

    __repr__ = __str__


print(Chain("").status.user.timeline.list)
