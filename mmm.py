import numpy as np
print(np.__version__)

# import pandas as pd
#import matplotlib.pyplot as plt
data = np.array([10,7,4,3,2,1])
median_value = np.median(data)
print(f"Median: {median_value:.2f}")
x= np.array([1,7,8,9,13,14,5,3])
print("the mean is", x.mean())
print("the maximum is", x.max())
print("the minimum is ",x.min())
print("the sort is", x.sorat())
for i in x:
     print(x)
     print(x[2:])
     print(x.shape)
     mydata=np.reshape(2,4)
