## what  are Arithmetic Function in numpy Arrays...

##.Arithmetic functions in NumPy are built-in mathematical functions used to perform calculations on array elements, such as addition, subtraction, multiplication, division, square root, and power.

#1d array...

# import numpy as np

# var = np.array([1,2,3,4,5,3,2])
# print("min : ",np.min(var))

# print("max:",np.max(var))

# print("argmin:",np.argmin(var))
# print("sqrt:",np.sqrt(var))

#sin ,cos ,cumsum value..
import numpy as np

var2 =np.array([1,2,3])
print(np.sin(var2))
print(np.cos(var2))
print(np.cumsum(var2)) #static medium 



# 2d array..
import numpy as np
var1 = np.array([[2,1,3],[9,5,6]])
print(np.min(var1,axis=1))
print(np.min(var1,axis=0))

print(np.max(var1,axis=1))
print(np.max(var1,axis=0))

