import numpy as np
import time 

# Python list..
start=time.perf_counter()

a = [j**4 for j in range(1,9)]
end =time.perf_counter()
print("Python List:",a)
print("List time",end-start)

#Numpy Array..
start=time.perf_counter()
b=np.array(range(1,9))**4
end =time.perf_counter()

print("Numpy Array:",b)
print("Array time",end-start)