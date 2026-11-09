#  diffrence between numpy array and python list

# python list  multiplication repeats the elements,whereas NumPy Array multiplication performs element-wise multiplication.

import numpy as np

#python list...
my_list = [1, 2, 3, 4, 5]

#NumPy Array..
my_array = np.array([1, 2, 3, 4, 5])

print("Python List:",my_list)
print("NumPy Array:",my_array)

print("Python List Multiplication:",my_list*2) # repeats the elements
print("NumPy Array Multiplication:",my_array*2) # performs element-wise multiplication







