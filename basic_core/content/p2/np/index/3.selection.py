# Selection 选择
import numpy as np
arr = np.arange(1,11)
print(arr) # [ 1  2  3  4  5  6  7  8  9 10]
bool_arr = arr>4
print(bool_arr) # [False False False False  True  True  True  True  True  True]
print(arr[bool_arr]) # [ 5  6  7  8  9 10]
print(arr[arr > 2]) # [ 3  4  5  6  7  8  9 10]

x = 5 
print(arr[arr > x]) # [ 6  7  8  9 10]