import numpy as np 

# arange random 
# arr = np.arange(25) 
# print(arr) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
# ranarr = np.random.randint(0,50,10)
# print(ranarr) # [49  1 47 43 14 38 14 10 33 39]

# reshape
# 来改变数组的形状。具体来说，arr.reshape(5, 5) 将一个数组重新组织为一个 5x5 的二维数组
# 它会被重新排列为 5 行 5 列的二维数组
# 始数组的元素数量必须与目标形状的元素数量一致。换句话说，原始数组的总元素数量必须等于 5x5 = 25
arr = np.arange(25)
arr1 = arr.reshape(5,5)
print(arr1) 
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]