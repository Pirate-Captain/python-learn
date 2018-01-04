#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""A test moulde"""

__author__ = "zhuyl"

import sys


def _private_print(args):
    if len(args) == 0:
        print("there is no args")
    elif len(args) == 1:
        print("the args is %s" % args[0])
    elif len(args) == 2:
        print("the second arg is %s" % args[1])
    else:
        print("there is too many args")


def test():
    args = sys.argv
    _private_print(args)


if __name__ == "__main__":
    test()

"""
第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

后面开始就是真正的代码部分。

当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
"""
