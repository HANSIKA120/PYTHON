from scipy import stats as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
age=[45,67,34,55,28,33]
salary=[30000,40000,55000,34000,25000,46000]
# plt.plot(age, salary, marker='o', color = 'r', linestyle='-', linewidth= 3)
# plt.scatter(age, salary, color='blue')
# plt.xlabel('age')
# plt.ylabel('salary')
# plt.title('age vs. salary')
# plt.show()

#COMBINING BOTH DATAS

data= list(zip(age, salary))
blank_array=[]
for mydata in range(1,6):
    kmean=KMeans(n_clusters=mydata)
    kmean.fit(data)
    blank_array.append(kmean.inertia_)
plt.plot(range(1,6),blank_array,marker='o')
plt.show()