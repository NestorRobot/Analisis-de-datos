import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df=pd.read_csv('Data/online_retail.csv',encoding='latin1')


month=np.array(['January','February','March','April','May','June','July','August','September','October','November','December'])
sales=np.array([1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500])
#configurar el tamaño de la figura
plt.figure(figsize=(8,6))
#crear un grafico 
plt.plot(month,sales,marker='o',color='blue',linestyle='-',label='Ventas mensuales')
plt.title('ventas totales por mes')
plt.xlabel('Meses')
plt.ylabel('Ventas en miles de dolares')
plt.show()
#grafico de dispersion
plt.figure(figsize=(8,6))
plt.scatter(month,sales,color='red',label='Ventas mensuales')
plt.title('ventas totales por mes')
plt.xlabel('Meses')
plt.ylabel('Ventas en miles de dolares')
plt.show()
#grafico de barras
plt.figure(figsize=(8,6))
plt.bar(month,sales,color='green',label='Ventas mensuales')
plt.title('ventas totales por mes')
plt.xlabel('Meses')
plt.ylabel('Ventas en miles de dolares')
plt.show()

plt.figure(figsize=(10,10))
categories=['A','B','C','D','E']
sales=[20,30,15,25,10]
plt.bar(categories,sales,color=['black','red','blue','green','orange'],label='ventas por categoria')
plt.title('Ventas de productos por mes')
plt.xlabel('Categorias')
plt.ylabel('Ventas ')      
plt.show()


plt.figure(figsize=(10,10))
categories=['A','B','C','D','E']
sales=[20,30,15,25,10]
plt.barh(categories,sales,color=['black','red','blue','green','orange'],label='ventas por categoria')
plt.title('Ventas de productos por mes')
plt.xlabel('Categorias')
plt.ylabel('Ventas ')      
plt.show()

plt.figure(figsize=(10,10))
plt.pie(sales,labels=categories,autopct='%1.1f%%',colors=['black','red','blue','green','orange'],startangle=90)
plt.axis('equal')
plt.title('Distribucion de ventas por categoria')  
plt.show()
