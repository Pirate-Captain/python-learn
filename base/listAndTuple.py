# list是一种有序的集合，可以随时添加和删除其中的元素
strList = ['zhang', 'li', 'wang']
print(strList)

# 用len()函数可以获得list元素的个数
print(len(strList))

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(strList[-1])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
strList.append("zhao")

print(strList)

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
strList.insert(1, "liu")

print(strList)

# 要删除list末尾的元素，用pop()方法
strList.pop()

print(strList)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
print(strList.pop(1))

print(strList)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
strList[1] = "qian"

print(strList)

# list里面的元素的数据类型也可以不同
strList.append(['wang wu', 'jack', 'mickle'])

print(strList)




# tuple

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
strTuple = ("zhang", "li", "wang")

print(strTuple)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
singleElementErr = (1)
print(singleElementErr)

singleElementCorrect = (1,)
print(singleElementCorrect)

# “可变的”tuple
changeAbleTuple = (0, "1", ["zhang", "li", "wang"])
print(changeAbleTuple)

# this is error
# changeAbleTuple[0] = "4"

changeAbleTuple[2][1] = "zhao"
print(changeAbleTuple)