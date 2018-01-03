#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

# 简单的list生成
list1 = list(range(1, 11))
print(list1)

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10], 使用for循环
list2 = []
for x in range(1, 11):
    list2.append(x * x)
print(list2)

# 使用列表生成式生成
list3 = [x * x for x in range(1, 11)]
print(list3)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
list4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list4)

# 还可以使用两层循环，可以生成全排列
list5 = [m + n for m in "ABC" for n in "XYZ"]
print(list5)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
list6 = [d for d in os.listdir(".")]
print(list6)

# 字符串列表转换为小写
list7 = ["zhangsan", "lisi", 18, "20", "MiKle", "Jack"]
list8 = [x.lower() if isinstance(x, str) else x for x in list7]
print(list8)
