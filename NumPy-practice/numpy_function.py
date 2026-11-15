# === Shuffle===
# import numpy as np

# var = np.array([1,2,3,4,5])

# np.random.shuffle(var)

# print(var)

# ==== Unique====  

# import numpy as np

# var1 = np.array([1,2,3,2,3,2,4,5,2,6,2,7])

# x = np.unique(var1,return_index=True,return_counts=True)

# print(x)


#====Resize====


# import numpy as np
# var2 = np.array([1,2,3,4,5,6])

# y = np.resize(var2,(2,3))

# print(y)


# ===== flatten====

import numpy as np
var3 = np.array([1,2,3,4,5,6])

y = np.resize(var3,(3,2))
print(y)

print("Flatten : ",y.flatten(order="f"))

print("Revel : ",np.ravel(y)) # iska bhi order pass kara sakte hai
                           # ,order="f"