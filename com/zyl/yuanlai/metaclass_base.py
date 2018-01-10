#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: metaclass_base
# @Date    : 2018-01-10 10:33
# @Author  : zhuyl

"""
metaclass

除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。

当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：

    当前准备创建的类的对象；

    类的名字；

    类继承的父类集合；

    类的方法集合。

"""


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaClass(type):
    def __new__(cls, name, base, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        print(cls)
        return super(ListMetaClass, cls).__new__(cls, name, base, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


l = MyList()
l.add(1)
print(l)
