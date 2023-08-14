# map
def time2(var):
    return var * 2

seq = [1,2,3,4]
print(map(time2, seq)) # <map object at 0x104467370>
print(list(map(time2, seq))) # [2, 4, 6, 8] list 竟然是关键字 表示将后面的内容放入 list 内
# 等价于这个 
print(list(map(lambda var: var * 2, seq))) # [2, 4, 6, 8]


# filter
filterItem = filter(lambda item: item % 2, seq)
print(filterItem) # <filter object at 0x100b7bee0>
print(list(filter(lambda item: item % 2 == 0, seq))) # [2, 4]