# numpy Arrays fuction ( insert and delete function)

#=== Numpy Insert() Function=====
# The insert() function is used to insert an element at a specific position in an array.

import numpy as np

arr = np.array([10, 20, 30, 40])

new_arr = np.insert(arr, 2, 25)

print(new_arr)


#....apprnd value se data koi bhi insert kae sakte hai
#1d array....
var = np.array([1,2,3,4])
print(var)
x = np.append(var,6.5)

print(x)

#2d arrat....

var2 = np.array([1,2,3],[1,2,4])
print(var)
v2 = np.append(var2,[[45,44,34]],axis=0)
print(v2)

#=== numpy delete() Function =====
# The delete() function is used to remove an element from a specific position in an array.

# import numpy as np

# arr = np.array([10, 20, 30, 40])

# new_arr = np.delete(arr, 2)

# print(new_arr)