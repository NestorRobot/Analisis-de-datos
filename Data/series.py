import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.dates import DateFormatter

dates=pd.date_range(start='2023-01-01',periods=100)
values=np.random.rand(100).cumsum()
data=pd.DataFrame({'Date':dates,'Value':values})

#grafico de lineas
fig,ax=plt.subplots(figsize=(12,6))
ax.plot(data['Date'],data['Value'],marker='o',color='blue',linestyle='-',label='Valor acumulado')
plt.xticks(rotation=45)
plt.title('Serie de tiempo con formato en las fechas')
plt.xlabel('Fecha')
plt.ylabel('Valor acumulado')       
plt.show()

dates=pd.date_range(start='2023-01-01',periods=12,freq='M')
sales=np.random.randint(1000,5000,size=12)
sales_data=pd.DataFrame({'Date':dates,'Sales':sales})
plt.plot(sales_data['Date'],sales_data['Sales'],marker='o',color='red',linestyle='-',label='Ventas mensuales')
plt.gca().xaxis.set_major_formatter(DateFormatter('%d-%b-%Y'))
plt.xticks(rotation=45)
plt.title('Ventas mensuales ')
plt.xlabel('Fecha')
plt.ylabel('Ventas en miles de dolares')
plt.legend()  
plt.tight_layout()
plt.show()