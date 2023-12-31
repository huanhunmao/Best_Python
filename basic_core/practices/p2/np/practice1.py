# NumPy Exercises 
# Create an array of 10 zeros
import numpy as np
arr = np.zeros(10)
# print(arr) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Create an array of 10 fives
arr1 = np.ones(10) * 5
# print(arr1) #  [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

# Create an array of the integers from 10 to 50
arr2 = np.arange(10,51)
# print(arr2) 
# [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
#  34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50]

# Create an array of all the even integers from 10 to 50
arr3 = np.arange(10,51,2)
# print(arr3) #  [10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50]

# Create a 3x3 matrix with values ranging from 0 to 8
arr4 = np.arange(9)
# res = arr4.reshape(3,3)
# print(res)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# Create a 3x3 identity matrix
arr5 = np.eye(3)
# print(arr5) 
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Use NumPy to generate a random number between 0 and 1
arr6 = np.random.rand(1)
# print(arr6) # [0.16501517]

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
arr7 = np.random.randn(5,5)
# print(arr7) 
# [[ 1.34350347 -0.78704473 -0.82293981 -0.39381437  1.03497656]
#  [-0.16359207 -0.86094244 -0.67273169  0.67869156  0.09847862]
#  [-0.30213647 -0.89281024 -0.10025258 -0.24027684  0.89364792]
#  [-0.06778667  0.92202073  0.25981253 -1.47553511 -1.45183181]
#  [-1.43898081 -0.32404707  0.52012631 -0.58538486 -1.30045619]]

# Create the following matrix:
# [[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
#        [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
#        [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
#        [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
#        [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
#        [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
#        [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
#        [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
#        [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
#        [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]]

arr8 = np.arange(0.01, 1.01, 0.01) # 开始 结束 步长
matrix = arr8.reshape(10,10) #  10x10 的二维数组
# print(matrix)

# 线性间隔 Create an array of 20 linearly spaced points between 0 and 1:
linear_points = np.linspace(0,1,20)
print(linear_points)
# [0.         0.05263158 0.10526316 0.15789474 0.21052632 0.26315789
#  0.31578947 0.36842105 0.42105263 0.47368421 0.52631579 0.57894737
#  0.63157895 0.68421053 0.73684211 0.78947368 0.84210526 0.89473684
#  0.94736842 1.        ]

