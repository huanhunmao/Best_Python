# Numbers 
# print(1 + 3)
# print(1 * 3)
# print(1/2)
# print(2 ** 4)
# print(4%2)
# print(5%2)
# print((2 +3) * (5+5))

#  Variable assignment
# Can not start with number or special characters
# name_of_var  = 666
# print(name_of_var)
# x = 2 
# y = 3
# z = x + y 
# print(z)

# Strings
# print('single string')
# print("double string")
# print("It's good")
# num = 18
# name = 'Marxu'
# print('My name is {}, and my num is {}'.format(name, num)) # My name is Marxu, and my num is 18
# or
# print('My name is {name}, and my num is {num}'.format(name=name, num=num)) #  My name is Marxu, and my num is 18
# print('My name is {name}, and my num is {num}'.format(name=name, num=num)) # Error

# Lists  js 数组
# list = [1,2,3]
# print(list)
# list.append('hi')
# print(list) # [1, 2, 3, 'hi']
# print(list[0]) # 1

# 类似 js  slice 截取 功能
# print(list[:1])  # [0,1) 左闭右开
# print(list[1:3]) # [2,3]
# list_plus = [1,2,3,[4,5,['target']]]
# print(list_plus[3][2][0]) # target


# Dictionaries 词典  js 对象
# d = {"key1": "item1" , "key2": "item2"}
# print(d)
# print(d["key1"]) # item1
# # print(d.key1) # Error
# print(d.keys())  # dict_keys(['key1', 'key2'])
# print(d.values()) # dict_values(['item1', 'item2'])

# Booleans  和js 不一样 首字母大写
# print(true) # Error 
# print(True)
# print(False)

# Tuples 元组  js 无
# t = (1,2,3)
# print(t) # (1, 2, 3)
# print(t[0]) # 1
# t[0] = 'ADD'
# print(t[0]) # TypeError: 'tuple' object does not support item assignment

# Sets  和 js 一样 会忽略掉重复元素
print({1,2,3})  # {1, 2, 3}
print({1,1,2,3,3,4,5,5}) #{1, 2, 3, 4, 5}

