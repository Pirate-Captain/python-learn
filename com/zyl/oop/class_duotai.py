#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: class_duotai
# @Date    : 2018-01-04 17:19
# @Author  : zhuyl

"""
多态是指，相同的成员方法名称，但是成员方法的行为（代码实现）却各不相同。这里所说的多态是通过 继承接口的方式实现的。Java中有interface，
但是Python中没有。Python中可以通过在一个成员方法体中抛出一个NotImplementedError异常来强制继承该接口的子类在调用该方法前必须先实现该方法的功能代码。


    接口的所有子类拥有接口中定义的所有同名的方法；
    接口的所有子类在调用接口中定义的方法时，必须先自己实现方法代码；
    接口的各个子类在实现接口中同一个方法时，具体的代码实现各不相同，这就是多态。

"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def walk(self):
        raise NotImplemented("Subclass must implements the abstract method by self")

    def talk(self):
        raise NotImplemented("Subclass must implements the abstract method by self")


class Dog(Animal):
    def walk(self):
        print("%s is walking with 4 legs" % self.name)

    def talk(self):
        print("%s is talking wangwang" % self.name)


dog = Dog("大黄")
dog.talk()
dog.walk()


class Duck(Animal):
    def walk(self):
        print("%s is walking with 2 legs" % self.name)

    def talk(self):
        print("%s is talking gua gua" % self.name)


duck = Duck("唐老鸭")
duck.talk()
duck.walk()
