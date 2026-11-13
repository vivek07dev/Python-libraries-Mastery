##.. Broadcasting numpy Array..
# Broadcasting in NumPy is a feature that allows arithmetic operations between arrays of different shapes without creating copies of data.

import numpy as np

a = np.array([10,30,20])
b = 5
result = (a+b)
print (result)
#....ex..

var1 = np.array([1,2,3,4])
print (var1.shape)
print()
print(var1)
print()
var2 = np.array([[1],[2],[3]])
print(var2.shape)
print()
print(var2)
x = (var1 + var2)
print(x)

# 2 cross one ka array.
x = np.array([[1],[2]])
print(x.shape)

y = np.array([[1,2,3],[1,2,3]])
print(y.shape)
print(x+y)