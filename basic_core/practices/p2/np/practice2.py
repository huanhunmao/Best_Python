# Numpy Indexing and Selection
# 输出结果是啥 
import numpy as np
mat = np.arange(1,26).reshape(5,5)
# print(mat)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

# 如何打出这个结果
# [[12, 13, 14, 15],
#  [17, 18, 19, 20],
#  [22, 23, 24, 25]]
# 2:：表示从第2行开始（因为 Python 使用零索引），即选择从第三行到最后一行的所有行。
# 1:：表示从第1列开始，即选择从第二列到最后一列的所有列。
# print(mat[2:,1:])

# 如何拿到上面的数据 20
# print(mat[3,4]) # 3 行 4列  从 0 开始计

# 如何拿到这个 
# [[ 2],
#  [ 7],
#  [12]]
# print(mat[0:3,1:2])

# 如何拿到这个 
#  [[21 22 23 24 25]]
# print(mat[4:])

# 如何拿到这个
# [[16, 17, 18, 19, 20],
# [21, 22, 23, 24, 25]]
# print(mat[3:])

# Get the sum of all the values in mat
# print(mat.sum()) # 325

# Get the standard deviation(标准差) of the values in mat
print(mat.std()) # 7.211102550927978

# Get the sum of all the columns（列之和） in mat
# mat.sum(axis=1) 按行求和
print(mat.sum(axis=0)) # [55 60 65 70 75]