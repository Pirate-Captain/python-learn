#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: test_calcsupport
# @Date    : 2018-01-10 14:33
# @Author  : zhuyl

import unittest
from com.zyl.unittest.calcsupport import CalcSupport

"""
为了编写单元测试，我们需要引入Python自带的unittest模块
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是
我们所期望的。最常用的断言就是assertEqual()

另一种重要的断言就是期待抛出指定类型的Error

setUp与tearDown

可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，
这样，不必在每个测试方法中重复相同的代码


运行单元测试

一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：

if __name__ == '__main__':
    unittest.main()


另一种方法是在命令行通过参数-m unittest直接运行单元测试：
"""


class TestCalcSupport(unittest.TestCase):
    def setUp(self):
        print("Set Up")

    def test_div_zero(self):
        cal = CalcSupport(10, 0)
        with self.assertRaises(ZeroDivisionError):
            cal.div()

    def test_div_normal(self):
        cal = CalcSupport(4, 2)
        self.assertTrue(2 == cal.div())

    def tearDown(self):
        print("tear down")
