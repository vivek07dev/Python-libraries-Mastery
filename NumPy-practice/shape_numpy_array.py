# Shape & Reshaping in numpy arrays..

# # Shape..

# import numpy as np
# var = np.array([[1,2,3,4],[1,2,3,4]])
# print(var)
# print(var.shape)

# # multidimension array..
# import numpy as np
# var1 = np.array([1,2,3,4], ndmin=4)
# print(var1)
# print(var1.ndim)
# print()
# print(var1.shape)


## Reshape....

# import numpy as np
# var2 = np.array([1,2,3,4,5,6,1,2,3])  # one dimension ko 2d..me kaise chage kare...

# print(var2)
# print(var2.ndim)

# x = var2.reshape(3,3)

# print(x)
# print(x.ndim)



##..one dim. ko 3d.. me convert ...
# import numpy as np
# var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(var3)
# print(var3.ndim)
# print(var3)

# x1 = var3.reshape(2,3,2)
# print(x1)
# print(x1.ndim)


#...one dim. ko 3d.. me convert ..fir 1d me convert

import numpy as np
var4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var4)
print(var4.ndim)

x2 = var4.reshape(2,3,2)
print(x2)
print(x2.ndim)

one = x2.reshape(-1)
print(one)
print(one.ndim)








