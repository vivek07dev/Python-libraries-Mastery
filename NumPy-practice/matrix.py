# matrix in numpy arrays====

#====MAtrix  aur array me differnce=====
# import numpy as np

# var1 = np.matrix([[1,2],[1,2]])
# var2  = np.matrix([[1,2],[1,2]])

# print(var1)
# print(type(var1))
# print(var1*var2)
# print()
# print(var1.dot(var2))

# array =====
# import numpy as np
# var1 = np.array([[1,2,3],[1,2,3]])

# print(var1)
# print(type(var1))
# print()
# print(var1*var1)




#===== Matrix function in numpy arrays=======


#....Transpose......
#Transpose means converting rows into columns and columns into rows in a matrix.

#In NumPy, we use the transpose() function or .T attribute.


# import numpy as np

# var = np.matrix([[1,2,3],[4,5,6]])
# print(var)
# print(np.transpose(var))
# print()
# print(var.T)

#....Swapaxes.....

# import numpy as np

# var2 = np.matrix([[1,2],[3,4]])
# print(var2)

# print(np.swapaxes(var2,0,1))


# ....Inverse matrix......

# import numpy as np
# var3 = np.matrix([[1,2],[3,4]])
# print(var3)
# print(np.linalg.inv(var3))


#.....power......
import numpy as np
var4 = np.matrix([[1,2],[3,4]])
print(var4)

print(np.linalg.matrix_power(var4,2))
print()

print(np.linalg.matrix_power(var4,0))
print()

print(np.linalg.matrix_power(var4,-2))
print()



#... determinate.....

import numpy as np

var4 = np.matrix([[1,2,3],[3,4,3],[1,2,3]])
print(var4)
print()
print(np.linalg.det(var4))
