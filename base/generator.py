# ！/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import sys

"""
生成器
1. 生成器的作用
 按照某种算法不断生成新的数据，直到满足某一个指定的条件结束。
2. 生成器的构造方式

构造生成器的两种方式：

    使用类似列表生成式的方式生成 (2*n + 1 for n in range(3, 11))
    使用包含yield的函数来生成

"""

# 3. 生成器构造实例
# 使用类似列表生成式的方式构造生成器
g1 = (2 * n + 1 for n in range(1, 11))


# 使用包含yield的函数构造生成器
def gen_1(start, end):
    for n in range(start, end):
        yield 2 * n + 1


g2 = gen_1(1, 11)
print(type(g1))
print(type(g2))

"""
4. 生成器的执行过程与特性
生成器的执行过程：

在执行过程中，遇到yield关键字就会中断执行，下次调用则继续从上次中断的位置继续执行。
生成器的特性：

    只有在调用时才会生成相应的数据
    只记录当前的位置
    只能next，不能prev

5. 生成器的调用方式

要调用生成器产生新的元素，有两种方式：

    调用内置的next()方法
    使用循环对生成器对象进行遍历（推荐）
    调用生成器对象的send()方法
"""

# 实例1：使用next()方法遍历生成器 使用next()方法遍历生成器时，最后是以抛出一个StopIeration异常终止
print(next(g1))
print(next(g1))

# 使用循环遍历生成器
for x in g1:
    print(x)

for x in g2:
    print(x)


# 调用生成器对象的send()方法
def gen_2(start, end):
    for m in range(start, end):
        result = yield 2 * m + 1
        print(result)


g3 = gen_2(1, 10)
print(g3.send(None))
print(g3.send('hello'))
print(g3.send("world"))

"""
6. 生成器与列表生成式对比

既然通过列表生成式就可以直接创建一个新的list，那么为什么还要有生成器存在呢？

因为列表生成式是直接创建一个新的list，它会一次性地把所有数据都存放到内存中，这会存在以下几个问题：

    内存容量有限，因此列表容量是有限的；
    当列表中的数据量很大时，会占用大量的内存空间，如果我们仅仅需要访问前面有限个元素时，就会造成内存资源的极大浪费；
    当数据量很大时，列表生成式的返回时间会很慢；

而生成器中的元素是按照指定的算法推算出来的，只有调用时才生成相应的数据。这样就不必一次性地把所有数据都生成，从而节省了大量的内存空间，
这使得其生成的元素个数几乎是没有限制的，并且操作的返回时间也是非常快速的（仅仅是创建一个变量而已）。
"""

time_start = time.time()
g4 = [x for x in range(100000)]
time_end = time.time()

print("列表生成式返回结果花费的时间：%s" % (time_end - time_start))
print("列表生成式返回结果占用的内存大小：%s" % sys.getsizeof(g4))

print()

time_start1 = time.time()
g5 = gen_1(0, 100000)
time_end1 = time.time()

print("生成器返回结果花费的时间：%s" % (time_end1 - time_start1))
print("生成器返回结果占用的内存大小：%s" % sys.getsizeof(g5))
