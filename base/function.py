# 定义一个空的函数 pass可以用来做占位符 保证程序的正常执行
def emptyFunction():
    pass


print(emptyFunction())


def multiplacation(x, y):
    if (not isinstance(x, (int, float))):
        raise TypeError('bad operator type')
    if (not isinstance(y, (int, float))):
        raise TypeError('bad operator type')
    return x * y


# wrong parameter
# print(multiplacation(10, 'a'))

print(multiplacation(10, 10.3))

print(multiplacation(10, 10))


# 返回多个值的函数 原来返回值是一个tuple
def multiResult(x, y):
    return x + '1', y + '2'


print(multiResult('1', 'd'))

m, n = multiResult('10', "9dfadfa")
print(m)
print(n)
