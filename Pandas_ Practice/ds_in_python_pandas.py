# =====data Structure in pythom pandas..=======

# ===...the Pandas provide two data structures for processing the data.
#==... Series & Dataframe and Panel====


#======== Series:======
#.... it is define as a one -dimenstional array that is capable of stroing various adata types.

# import pandas as pd

# a= pd.Series()
# print(a)


# import pandas as pd
# x = [3,4,5,6,]

# var = pd.Series(x)

#  var = pd.Series(x,index=['a','s','d','f'],dtype="float",name="python")

# print(var)
# print(type(var))
# print(var[2])

# ......dictionary......

# import pandas as pd
# dic = {"name":['python','c','c++','java'],"por":[12,13,14,15],"rank":[1,4,3,2]}

# var1 = pd.Series(dic)

# print(var1)

# # single data to find series...

# import pandas as pd
# a = pd .Series(12)

# print(a)
# print(type[a])


#    ye data ka multiple series ban jaye...
import pandas as pd
s = pd.Series(12,index=[1,2,3,4,5,6])
print(s)
print(type(s))


# missing data bhi print kar de raha hai
s1 = pd.Series(12,index=[1,2,3,4,5,6,7])
s2 = pd.Series(12,index=[1,2,3,4])

print(s1+s2)