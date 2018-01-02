# 必选参数、默认参数、可变参数、关键字参数、命名关键字参数

# 必选参数
def fun1(a):
    print(a)


fun1('abcd')


# 默认参数
# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def fun2(a, b="10"):
    print(a, b)


fun2("100")

fun2("100", "20")


# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上
def fun3(a, b="10", c="20"):
    print(a, b, c)


fun3("11", c="30")


# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
def add_end(L=[]):
    L.append("END")
    return L


print(add_end())
print(add_end())


# 问题改进
def add_end(L=None):
    if L is None:
        L = []
    L.append("END")
    return L


print(add_end())
print(add_end())


# 可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calcMulti(numbers):
    sum = 1
    for number in numbers:
        sum *= number
    return sum


# print(calcMulti(1,2,3))
print(calcMulti([1, 2, 3, 4, 5]))
print(calcMulti((1, 2, 3, 4, 5)))


def calcMultiChangeable(*numbers):
    sum = 1
    for number in numbers:
        sum *= number
    return sum


print(calcMultiChangeable(1, 2, 3, 4, 5))

numbers = [1, 2, 3, 4, 5]
print(calcMultiChangeable(*numbers))
calcMultiChangeable()


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def fun4(a, b, **kw):
    print("name:", a, "age:", b, "other:", kw)


fun4("zhangsan", 20, city="beijing", province="beijing")

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# 对kw的改动不会影响到函数外的extra
extra = {"city": "beijing", "province": "beijing"}
fun4("zhangsan", 20, **extra)


# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def fun5(name, age, *, city, province):
    print("name:", name, "age:", age, "city:", city, "province:", province)


fun5("zhangsan", 20, city="beijing", province="beijing")


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def fun6(name, age, *args, city, province):
    print("name:", name, "age:", age, "args:", args, "city:", city, "province:", province)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
fun6("zhangsan", 20, 10, 15, 16, city="beijing", province="beijing")


# 命名关键字参数可以有缺省值，从而简化调用
def fun7(name, age, *args, city="beijing", province="beijing"):
    print("name:", name, "age:", age, "args:", args, "city:", city, "province:", province)


fun7("zhangsan", 20, 10)


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def fun8(name, age=20, *args, city, province="beijing", **kw):
    print("name:", name, "age:", age, "args:", args, "city:", city, "province:", province, "other:", kw)


fun8("zhangsan", 10, 20, city="beijing", address="street 1")

p1 = ["zhangsan", 30]
args = [10, "lisi", "hello"]
kw = {"city": "beijing", "address": "street 1", "sex": "male"}
fun8(*p1, *args, **kw)
fun8(p1, *args, **kw)

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
