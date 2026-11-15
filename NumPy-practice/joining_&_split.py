# # ===Join & Split function numpy array========

# # Join array ===:
# #joining means putting contents of two or more arrays in a single array.

# import numpy as np
# var = np.array([1,2,3,4]) 
# var1 = np.array([9,8,7,6]) 

# ar = np.concatenate((var,var1))
# print(ar)

# #2 array ko concatenate karke new array add karna
# import numpy as np 
# vr = np.array([[1,2],[3,4]])
# vr1 = np.array([[9,8],[7,6]])

# ar_new = np.concatenate((vr,vr1),axis=1)

# print(vr)
# print()
# print(vr1)
# print(ar_new)

# # stack function ke through merage kar sakte hai

# import numpy as np

# var_1 = np.array([1,2,3,4])
# var_2 = np.array([9,8,7,6])

# a_new = np.stack((var_1,var_2),axis = 1)
# a_new1 = np.hstack((var_1,var_2))#row
# a_new2 = np.vstack((var_1,var_2)) # coloums
# a_new3 = np.dstack((var_1,var_2)) # height

# print(a_new)
# print(a_new1)
# print(a_new2)
# print(a_new3)

# split Array: Spliting break one array  into multiple

# split  array
# import numpy as np
# var = np.array([1,2,3,4,5,6])

# print(var)
# ar = np.array_split(var,3)
# print(ar)
# print(ar[0])


# 2d array..
import numpy as np
var1 = np.array([[1,2],[3,4],[5,6]]) #axis ke along split kara sakte hai
print(var1)

ar1 = np.array_split(var1,3)
ar2 = np.array_split(var1,3, axis=1)

print(ar1)
print()
print(ar2)
