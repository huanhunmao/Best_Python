import numpy as np

# basic 
arr = np.arange(0,11)
print(arr) # [ 0  1  2  3  4  5  6  7  8  9 10]


# Bracket Indexing and Selection
print(arr[8]) # 8
print(arr[1:5]) # [1  2  3  4]
print(arr[0:5]) # [0  1  2  3  4 ]

# Numpy arrays 广播能力 Broadcasting 相比普通数组不同
# 将一个范围的内容都改成一个数 
st = arr[0:5] = 100 
print(st) # 100
print(arr) # [100 100 100 100 100   5   6   7   8   9  10]

#  Reset array
arr1 = np.arange(0,11)
print(arr1) # [ 0  1  2  3  4  5  6  7  8  9 10]

#Important notes on Slices
slice_of_arr1 = arr1[0:6]
print(slice_of_arr1) # [0 1 2 3 4 5]

#Change Slice
slice_of_arr1[:] = 666
print(slice_of_arr1) # [666 666 666 666 666 666]

#To get a copy, need to be explicit
# This avoids memory problems!
arr1_copy = arr1.copy()
print(arr1_copy) # [666 666 666 666 666 666   6   7   8   9  10]\
# change arr1 
arr1 = np.arange(0,12)
print(arr1) # [ 0  1  2  3  4  5  6  7  8  9 10 11] 
print(arr1_copy)