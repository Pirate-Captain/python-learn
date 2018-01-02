# 切片，取list或tuple中某区间的直 l[x:y] 取 l list（tuple）中下标x开始到y（不包含y）的元素
l = ['zhang', 'li', 'wang', 'zhao', 'qian']

print(l[0:3])

# 如果第一个索引是0，还可以省略
print(l[:3])

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(l[-2:])
print(l[-2:-1])

l = list(range(100))
print(l)

# 前10个数
print(l[:10])

# 后10个数
print(l[-10:])

# 前11-20个数
print(l[10:20])

# 前10个数，每两个取一个
print(l[:10:2])

# 所有数，每5个取一个
print(l[::5])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
l = (1, 10, 20, 11, 8, 9, 20, 50, 46, 32)
print(l[:20:2])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
l = "dkajfaiofuadiueuriwrwqjrkwejrkqwjoejqwe"
print(l[:10:5])