# Array creation in NumPy

# import numpy as np
# x = [1,2,3,4,5]
# y = np.array([1,2,3,4,5])

# print(y)
# print(type(y)) # prints the type of the array



# l =[] # values ko append karne ke liye empty list banai hai

# for i in range(1,5):
#     int_1 = int(input('enter:'))
#     l.append(int_1)
# print(np.array(l))    

#... type of array.......

#1d array creation in NumPy.....

import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(arr1.ndim)


# 2d array creation in NumPy....

import numpy as np
arr2= np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.ndim)


# 3d Array creation in numpy.....


import numpy as np
arr3 = np.array([[[2,3,4,5],[12,4,5,6],[7,8,9,10]]])
print(arr3)
print(arr3.ndim) # prints the dimension of the array


# multidimensional array creation in numpy...

import numpy as np
arn = np.array([1,2,3,4],ndmin = 10) # prints the dimension of the array
print(arn)
print(arn.ndim)
