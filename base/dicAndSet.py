# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储
provinces = {"11":"北京", "12":"天津", "41":"河南"}
print(provinces)

# 修改key对应的值
provinces["12"] = "河北"
print(provinces)

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
# print(provinces["16"])
print("16" in provinces)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(provinces.get("19"))
print(provinces.get("19", "未知"))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
provinces.pop("12")
print(provinces)


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# provinceCode = set([11, 12, 13, 14, 15, 11])
provinceCode = {11, 12, 13, 14, 15, 11}
print(provinceCode)

# 通过add(key)方法可以添加元素到set中
provinceCode.add(18)
print(provinceCode)

#通过remove(key)方法可以删除元素
provinceCode.remove(13)
print(provinceCode)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
provinceCodeAnother = {11, 15, 18, 30, 36, 38}

print(provinceCode & provinceCodeAnother)
provinceResult = provinceCode | provinceCodeAnother
print(provinceResult)
print(provinceCode)