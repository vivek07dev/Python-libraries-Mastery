# ========copy vs views in numpy array========

#Creates a separate array.	1. Creates a new view of an array.
# 2. Does not share data.	2. Shares underlying data.
# 3. Changes in original do not affect copy.	3. Changes in original can affect view.
# 4. Changes in copy do not affect original.	4. Changes in view can affect original.

# copy...
#A Copy creates a completely separate array. Changes made to the original array do not affect the copied array

import numpy as np
var = np.array([1,2,3,4])

co = var.copy()

print("var :",var)
print("copy :",co)


#=====Views====
#A View creates a new array that shares the same underlying data as the original array. Changes in one array can affect the other.

import numpy as np
x = np.array([5,4,3,2])

vi = x.view()

print("x :",x)
print("view",vi)

 #difference -------
import numpy as np
var = np.array([1,2,3,4])

co = var.copy()

var[1]=40

print("var :",var)
print("copy :",co)

#views...
import numpy as np
x = np.array([5,4,3,2])

vi = x.view()
x[1]=40

print("x :",x)
print("view",vi)





