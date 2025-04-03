# import numpy as np
# import pandas as pd
# #import matplotlib.pyplot as plt
# data = np.array([10,7,4,3,2,1])
# median_value = np.median(data)
# print(f"Median: {median_value:.2f}")
# x= np.array([1,7,8,9,13,14,5,3])
# print("the mean is", x.mean())
# print("the maximum is", x.max())
# print("the minimum is ",x.min())
# print("the sort is", x.sort())
# for i in x:
#      print(x)
#      print(x[2:])
#      print(x.shape)
#      mydata=np.reshape(2,4)

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
x= np.array([1,7,8,11,9,3,2,4])
print("the mean is",x.mean())
print("the maximum is",x.max())
print("the minimum is",x.min())

for i in x:
    print (i)
    print(x[-6:-2])
    print(x.shape)
    mydata = x.reshape(2,4)
    print(mydata)
    y=np.array([3,1,7,9,2,11,8,10])
    z=x+y
    print(z)
    
    
    
    
    
    