 # cerate numpy  array with randons numbers


# random array ......

import numpy as np
var =np.random.rand(4)  #4 values ka 1 diamenson array create ho jayega
print(var)

## multiple dimensional array create karne ke liye
#Rand()...
var1 = np.random.rand(2, 5)  
print(var1)

#rand(): the functionmis used to generate a random value between o and 1
#randn(): the finction ies used to generate aarndom value close to zero. this may return positive or negative numbers as well.
#ranf(): the function is used to generate a random value between 0 and 1. this function is similar to rand() function but it is faster than rand() function.
#randint(): the function is used to generate a random integer value between a specified range. this function takes two arguments, the lower limit and the upper limit of the range.


# Randn().....
import numpy as np
var2 = np.random.randn(5)  # 5 values ka 1 dimensional array create ho jayega
print(var2)

#Ranf()...
import numpy as np
var3 = np.random.ranf(4)  # 4 values ka 1 dimensional array create ho jayega
print(var3)

#Randint()...
import numpy as np
var4 = np.random.randint(5, 10, 4)  # 5 to 10 ke beech ka koi bhi integer value generate karega
print(var4)