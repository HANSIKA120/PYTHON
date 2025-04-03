import numpy as np
from sklearn.metrics import r2_score
age=[20,25,35,45,50,60]
salary=[40000,15000,30000,25000,22000,45000]
futuresalary= np.poly1d(np.polyfit(age,salary,3))
print(r2_score, salary, futuresalary(19))

# find the amazon, flipcart, zomato, makemy trip, swiggy, oyo next year sale.


from scipy import stats as st
import matplotlib.pyplot as plt
year=[2014,2015,2016,2017,2018,2019,2020]
amaprofit=[241, 596, 2370, 241, 3030, 10070, 15900]
slope, intercept, r, p, std_err= st.linregress(year,amaprofit)
print("slope", slope, "intercept", intercept,"r",r,"p",p,"std_err",std_err)
def futuresales(year):
    return slope*year+intercept
print("future salary",futuresales(2022))
plt.scatter(year, amaprofit, color='blue')
plt.xlabel('year')
plt.ylabel('Sales')
plt.title('year vs. Sales Scatter Plot')
plt.show()



#k mean model is an unsupervised machine learning technique for making clustering
#this model will divide the data points in k cluster format  minimizing the variance in data set

