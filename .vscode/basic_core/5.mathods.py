# methods
# lower upper
# str = 'ppx Good PP'
# print(str.lower()) # ppx good pp
# print(str.upper()) # PPX GOOD PP

# split
# print(str.split()) # ['ppx', 'Good', 'PP'] 神奇的是 和js 不同 不能用其他分割？
# 但可以将里面有的 分割出来
str2 = "ppx ##$hello"
print(str2.split('#')) # ['ppx ', '', '$hello']
print(str2.split('#')[2]) # $hello
 