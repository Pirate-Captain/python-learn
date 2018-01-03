#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce

"""
高阶函数
函数是一个接受另外一个函数作为参数的，而这种函数就称为高阶函数
"""


def num_add(x, y, f):
    return f(x) + f(y)


print(num_add(10, 20, abs))

"""
高阶函数 map
map函数的参数说明：

    map函数接收两类参数：函数和可迭代对象（Iterable）
    第一个参数是函数，后面的参数都是可迭代对象。
    处理函数的参数个数需要与传入的可迭代对象参数的个数对应，否则会报错。
    如果传入的可迭代对象参数有多个，且每个iterable元素数量不相等时，结果中的元素个数与最短的那个iterable的元素个数一致。

"""

list1 = list(range(10, 20))
list2 = list(range(15, 25))

listResult = list(map(lambda x, y: x * y, list1, list2))

print(listResult)

"""
reduce(function, sequence, initializer=None)
reduce函数的参数说明：

    接收一个函数参数、一个序列参数和一个可选的initalizer参数
    如果可选参数initializer被提供，则相当于把它作为sequence的一个元素插入sequence的首部

reduce函数的作用是：

把一个函数作用在指定的序列上，这个函数必须接收两个参数，然后把计算结果继续和序列的下一个元素做累计计算，最终返回一个结果。
简单来讲，就是对一个序列中的元素做聚合运算。
"""

list3 = list(range(1, 50))
result = reduce(lambda x, y: x + y, list3)
print(result)

list4 = ["zhangsan", "lisi", "wangwu"]
result = reduce(lambda x, y: x + y, list4)
print(result)

# 将数字字符串转成int
print(reduce(lambda x, y: int(x) * 10 + int(y), "12345"))

"""
filter函数

filter(function, iterable)

filter函数的参数说明：

    filter函数接收一个函数参数和一个可迭代对象参数，函数参数可以为None
    函数的返回值（True或False）用于判断可迭代对象的当前元素是否要保留

filter函数的作用是：

用于过滤可迭代对象，具体过程是：把传入的函数依次作用于可迭代对象的每个元素，如果函数返回值为Ture则保留该元素，如果返回值为False则丢弃该元素，
并最终把保留的元素作为一个iterator（迭代器）返回。如果function是None，则根据可迭代对象各元素的真值测试结果决定是否保留该元素。

与Python内置的filter函数作用刚好相反的函数是itertools.filterfalse(function, sequence)，它用于过滤出序列中通过function函数计算结果为False的元素。
"""

# 分别打印出指定列表中的奇数和偶数
list5 = list(range(10, 1000))
odd_num = list(filter(lambda x: x % 2 == 1, list5))
print(odd_num)
even_num = list(filter(lambda x: x % 2 == 0, list5))
print(even_num)

# 删除序列中的空字符串
list6 = ["zhangsan", "", "lisi", "wangwu", "", "zhaoqian"]
result = list(filter(lambda x: x and x.strip(), list6))
print(result)

"""
sorted函数

sorted(iterable[, key][, reverse])

sorted函数的参数说明：

    sorted函数可以接收一个可迭代对象iterable作为必选参数，还可以接收两个可选参数key和reverse，但是这两个可选参数如果要提供的话，需要作为关键字参数进行传递；
    参数key接收的是一个函数名，该函数用来实现自定义排序；如，要按照绝对值大小进行排序：key=abs
    参数reverse接收的是一个布尔值：如果reverse=Ture，表示倒叙排序，如果reverse=False，表示正序排序；reverse默认值为False

    关于参数key的进一步说明： 排序的核心是比较两个元素的大小。如果要比较的是两个数字，我们可以直接比较；如果是字符串，也可以按照ASCII码的大小进行比较。
    但是，如果要比较的元素是两个序列或dict等复杂数据呢？这时，我们可能需要指定一个计算“用于比较的值”的运算规则，比如我们指定取两个dict中的某个共同的
    key对应的值来进行比较，又比如我们指定用将两个字符串都转换为小写或者大写后的结果值进行比较。其实说简单点，参数key这个函数作用是：
    计算/获取用来进行比较的值。如果我们需要自定义这个函数时，需要注意该函数应该有一个参数，这个参数接收的就是可迭代对象中每个元素的值。

sorted函数的作用是：

对可迭代对象iterable中的元素进行排序，并将排序结果作为一个新的list返回。
"""

list7 = [10, 12, 80, 100, 9, 6, 23, 20, 56, 89, 34, 70, 95, 22, 12, 66]
print(list7)
print(sorted(list7))

list8 = ["zhao", "lisi", "Abc", "qian", "sunli", "wang", "men"]
print(sorted(list8))

# tuple列表排序
list9 = [("zhangsan", 20), ("lisi", 18), ("wangwu", 10), ("zhaoliu", 40)]
print(sorted(list9, key=lambda x: x[0]))
print(sorted(list9, key=lambda x: x[1]))

# 字典内容排序
# 对字典排序的方法有很多中，但核心思想都是一样的：把dict中的key或value或item分离出来放到一个list中，然后在对这个list进行排序，从而间接实现对dict的排序。
dic1 = {"zhangsan": 20, "lisi": 18, "wangwu": 10, "zhaoliu": 40}
print(sorted(dic1.items(), key=lambda x: x[0]))
print(sorted(dic1.items(), key=lambda x: x[1], reverse=True))
