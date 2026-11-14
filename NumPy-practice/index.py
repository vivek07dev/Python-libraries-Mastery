# # =======Indexing NumPy  Array=============......


# import numpy as np

# var = np.array([9,8,7,6])
# #                0,1,2,3
# #                -4,-3,-2,-1
# print(var[2])
# print(var[-3])

# # 2d array idexing.....

# import numpy as np
# var1 = np.array([[6,5,4,],[8,5,6]])
# print(var1)
# print(var1.ndim)

# print()
# print(var1[0,2])


# #3d array indexing...
# import numpy as np
# var2 = np.array([[[1,2],[6,7]]])
# print(var2)
# print(var2.ndim)

# print()

# print(var2[0,1,1])

#====Slicing =====........
import numpy as np
var = np.array([9,8,7,6,5,4,3])
   #            0,1,2,3,4,5,6 indexing
print(var)

print()

print("2 to 5:",var[1:5])

print("2 to end:",var[1:])

print("start to 5:",var[:5])

print("stop:",var[1:6:2])


#===2d array===....

import numpy as np
var1 = np.array([[1,2,3,4,5],[9,8,7,6,5],[11,12,13,14,15,]])
print(var1)

print("8 to 5:",var1[2,1:])


