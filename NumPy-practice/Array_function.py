#  how to create NumPy Array using NumPy Arrray Function

#array filled with 0's
# Zeros Arrray....

import numpy as np
arr_zero = np.zeros(4)
arr_zero1 = np.zeros((3,4)) # dimensional array with 3 rows and 4 columns
print(arr_zero)
print()
print(arr_zero1)

#ones Array....
# array filled with 1's

import numpy as np
arr_ones = np.ones(4)
print(arr_ones)


## Empty Array....
import numpy as np
arr_empty = np.empty(4)
print(arr_empty)


#Range Array....
import numpy as np
arr_rn = np.arange(5) # 0 to 4
print(arr_rn)



# Array diagonal element filled with 1's
import numpy as np
arr_dia = np.eye(4) # 4x4 array with diagonal elements as 1's   # eye() function ka use karte hai
print(arr_dia)


arr_dia = np.eye(3,5) # 3x5 array with diagonal elements as 1's
print(arr_dia)



# create an array with values that are spaced linerarly in a specified interval
#Linespace Array....
import numpy as np
arr_line = np.linspace(1, 10, 5) # 5 values from 1 to 10
print(arr_line)