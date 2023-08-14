# 次方
# print(7 ** 4) # 2401

# ** Split this string:** **into a list. **
# s = "Hi there Sam!"
# print(list(s.split())) # ['Hi', 'there', 'Sam!']

# .format() 使用 变量
# planet = "Earth"
# diameter = 12742
# print('The diameter of {} is {} kilometers.'.format(planet, diameter))
# # or
# print('The diameter of {planet} is {diameter} kilometers.'.format(planet=planet,diameter=diameter))

# 索引查找list中值 Given this nested list, use indexing to grab the word "hello" 
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# print(lst[3][1][2][0]) # hello

# 拿到 字典内的 value hello
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# print(d['k1'][3]["tricky"][3]["target"][3]) # hello

# What is the main difference between a tuple and a list?
# Tuple is immutable

# 写个函数 So for example, passing "user@domain.com" would return: domain.com
# def getDomain(url):
#     splitUrl = url.split('@')
#     return splitUrl[1]

# print(getDomain('user@domain.com')) # domain.com

# 写一个函数包含 dog 返回 True 不考虑边缘符号 但是考虑大小写 
# def findDog(item):
#     dog = 'dog'
#     splitItem = item.split()
#     for item in splitItem:
#         if item.lower() == dog:
#             return True
#     return False
# res = findDog('Is there a dog here?')
# print(res)

# 写一个函数统计 dog 出现次数 
# def countDog(str):
#     count = 0
#     dog = 'dog'
#     splitItem = str.split()
#     for item in splitItem:
#         if item.lower() == dog:
#             count = count + 1
    
#     return count

# res = countDog('This dog runs faster than the other dog dog dog dude!')
# print(res) # 4

#  Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.
# seq = ['soup','dog','salad','cat','great']
# res = filter(lambda item: item[0] == 's', seq)
# print(list(res)) # ['soup', 'salad']

# caught_speeding 超速罚单问题
# **You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", 
# "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive,
#  the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". 
#  Unless it is your birthday (encoded as a boolean value in the parameters of the function)
#   -- on your birthday, your speed can be 5 higher in all cases. **
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 6:
        return "No ticket"
    elif speed > 61 and speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"

res1 = caught_speeding(81,True)
print(res1) # Small Ticket
res2 = caught_speeding(81,False)
print(res2) # Big Ticket