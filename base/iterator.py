from collections import Iterable

# 只要是可迭代对象，无论有无下标，都可以迭代
# list
listInfo = ['zhang', "li", "zhao", "qian"]
for value in listInfo:
    print(value)

# dic
dic = {"11": "北京", "12": "天津", "41": "河南", "42": "山东"}
for key in dic:
    print(key)

# 循环dic中的value
for value in dic.values():
    print(value)

# 同时循环key、value
for x, y in dic.items():
    print(x, y)

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
# 通过collections模块的Iterable类型判断是否是可迭代对象

print(isinstance("abc", Iterable))

# 如果要对list实现类似Java那样的下标循环 Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for x, y in enumerate(listInfo):
    print(x, y)
