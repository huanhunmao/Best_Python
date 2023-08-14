# js 关键词 function py -> def 
# def my_func(params = 'default'):
#     """ 
#      Docstring goes here.
#     """
#     print(params)

# print(my_func) # <function my_func at 0x1005ffeb0> 这部分是函数对象在内存中的地址
# my_func() # default
# print(my_func()) #  default None
# my_func('good input') # good input

# def quare(x):
#     return x ** 2
# out = quare(2)
# print(out) # 4


#  lambda expressions 匿名函数，也称为"lambda 表达式"
def times2(var):
    return var * 2
print(times2(2)) # 4
# 用 lambda 怎么写 简化函数？
print('lambda',lambda var: var * 2) # lambda <function <lambda> at 0x10104e710>

