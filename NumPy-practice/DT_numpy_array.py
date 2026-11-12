# Datatype in numpy array....
#In NumPy, data type (dtype) defines the type of elements stored in an array, such as integers, floating-point numbers, or strings.

#integers....
import numpy as np
var = np. array([1,2,3,4,12,14,15])  
print("data type:", var.dtype)  # 

#floats.....
var2 = np.array([1.0,1.2,1.3])
print("data type:", var2.dtype)  # Output: float64

#strings....
var = np.array(["A", "s", "C", "D"])
print("data type:", var.dtype)  

var = np.array(["A", "s", "C", "D",1,2,3,4])  # If you mix data types in a NumPy array, it will upcast to the most general type that can accommodate all the values. In this case, it will upcast to a string type.
print("Data Type:", var.dtype)  


x = np.array([1,2,3,4],dtype=np.int8)
print("Data Type:",x.dtype)
print(x)

x1 = np.array([1,2,3,4],dtype = "f") 
print("Data Type:",x1.dtype)
print(x1)

# datatype ko function ki tarah use kar sakte hai

x2 = np.array([1,2,3,4])
new =np.float32(x2)

new_one = np.int_(new)
print("Data Type :",x2.dtype)
print("Data Type :",new_one.dtype)

print(x2)
print(new)
print(new_one)

#direct method..

x3 = np. array([1,2,3,4])
new_1 = x3.astype(float)

print(x)
print(new_1)
