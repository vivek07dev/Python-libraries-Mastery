# Arithmetic Operation in numpy arrays....

#Arithmatic Operation..

import numpy as np
var = np.array([1,2,3,4])
varadd = var + 3

print(varadd)

# two variable..

import numpy as np
var1 = np.array([1,2,3,4])
var2 =np.array([2,1,3,4])

#varadd = np.add(var1,var2)
varadd = var1 + var2
print(varadd)

# subtract..
import numpy as np
var1 = np.array([1,2,3,4])
varadd = var-2
print(varadd)

# multiple...
import numpy as np
var1 = np.array([1,2,3,4])
varadd = var*2
print(varadd)

# divide..
import numpy as np
var1 = np.array([1,2,3,4])
varadd = var/2
print(varadd)

# mod...
import numpy as np
var1 = np.array([1,2,3,4])
varadd = var%2
print(varadd)

#power...
import numpy as np
var1 = np.array([1,2,3,4])
varadd = var**2
print(varadd)

#reciprocal...
import numpy as np
var1 = np.array([1,2,3,4])
varadd = np.reciprocal(var)
print(varadd)


#2d Array....

var21 = np.array([[1,2,3,4],[1,2,3,4]])
var22 = np.array([[1,2,3,4],[1,2,3,4]])

print(var21)
print()
print(var22)
print()


varadd2 =var21 + var22
print(varadd)