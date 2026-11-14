#==== Iterating Numpy Array======......
#Iterating a NumPy array means accessing each element of an array one by one using loops.


# iterating 1d array......

# import numpy as np
# var = np.array([9,8,7,6,5,4,3])
# print(var)

# for i in var :
#     print(i)


# 2d array.....

# import numpy as np

# var1 = np. array([[1,2,3,4],[1,2,3,4]])
# print(var1)
# print()

# for j in var1 :
#     print(j)

# print()

# for k in var1:
#     for i in k:
#         print(i)

#3d array....
# import numpy as np
# var3 = np.array([[[1,2,3,4],[1,2,3,4]]])
# print(var3)
# print(var3.ndim)
# print()

# for i in var3:
#     for j in i:
#         for k in j:
#             print(k)

# direct method without loop

# import numpy as np
# var3 = np.array([[[1,2,3,4],[1,2,3,4]]])
# print(var3)
# print(var3.ndim)
# print()

# for i in np.nditer(var3):
#     print(i)


 # iteration me indexing de sakte hai
 # 
import numpy as np
var3 = np.array([[[9,8,7,6],[1,2,3,4]]])
print(var3)
print(var3.ndim)
print()

for i,d in np.ndenumerate(var3):
    print(i,d)
