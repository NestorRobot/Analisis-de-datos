import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data= np.random.normal(170,10,200)
print(data)

plt.hist(data,bins=10,color='blue',edgecolor='black',alpha=0.7)
plt.title("Distribucion de alturas")
plt.xlabel("Altura (cm)")
plt.ylabel("densidad")
plt.show()

np.random.seed(0)
ages=[np.random.normal(30,5,100),
      np.random.normal(40,5,100),
      np.random.normal(35,5,100)]
print(ages)

plt.boxplot(ages,labels=['Grupo 1','Grupo 2','Grupo 3'],patch_artist=True ,notch=True,vert=True,
            showmeans=True,meanline=True, tick_labels=['Grupo 1','Grupo 2','Grupo 3'])
plt.title("Distribucion de edades por grupo")
plt.xlabel("Grupos de edad")
plt.ylabel("Edad (años)")
plt.show()