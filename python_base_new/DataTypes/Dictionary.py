# Key: Value pair, JSON like object  键值对组合 或 JSON 类对象
empty_dict = {}
dic = {'one': 1, 'two': 2, 'three': 3}
print(dic)
print(dic['two']) # 2

print(dic.keys()) # dict_keys(['one', 'two', 'three'])
print(dic.values()) # dict_values([1, 2, 3])

dic.update({'four': 666})
print(dic) # {'one': 1, 'two': 2, 'three': 3, 'four': 666}

print(dic.items()) # dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 666)])
