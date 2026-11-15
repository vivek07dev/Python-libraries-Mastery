# # numpy array functions( search,sort,search sorted,filter)

# #====Search:===:
# #  searching an array for a certain value, and return the indexes that get a macth.

# import numpy as np

# var = np.array([4,2,3,4,2,5,2,5,6,7])
# #      index     0,1,2,3,4,5,6,7,8,9
# x = np.where((var%2) == 0)
# print(x)

# =====search sorted array====== :  which performs a binary search in the array, 
# and returns the index where the specified value would be inserted to maintain the search order

# import numpy as np
# var1 = np. array([1,2,3,4,9,10])

# x1 = np.searchsorted(var1 ,[5,6,7], side ="right")
# print(x1)

# #======Sort======
# #==:

# # 2d array..
# import numpy as np
# a = np.array([[4,3,2],[1,12,5],[22,45,6]])

# print (np.sort(a))


# ====Filter Array====
#: Getting some elements out of an  existing array and creating a new array out of them

#=== filter array ===

import numpy as np

var2 = np.array(["a","s","d","f"])
f = [True,False,False,True]

new_a = var2[f]

print(new_a)
print(type(new_a))