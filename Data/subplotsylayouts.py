import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec

x=np.linspace(0,10,100)
y=np.sin(x)
data=np.random.rand(100)
gs=gridspec.GridSpec(2,2,height_ratios=[2,1],width_ratios=[1,2])
fig=plt.figure(figsize=(10,8))
#Primer subplot grande
ax1=fig.add_subplot(gs[0,1])
ax1.plot(x,y,color='blue',label='Seno de x')
ax1.set_title('Grafico de Seno')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.legend()
#Segundo subplot pequeño ocupa la parte inferior izquierda
ax2=fig.add_subplot(gs[1,0])
ax2.hist(data,bins=20,color='green',edgecolor='black',alpha=0.7)
ax2.set_title('Histograma de datos aleatorios')
ax2.set_xlabel('Valor')
ax2.set_ylabel('Frecuencia')
#Tercer subplot pequeño ocupa la parte inferior derecha
ax3=fig.add_subplot(gs[1,1])
ax3.scatter(x,y,color='red')
ax3.set_title('Grafico de dispersion')
ax3.set_xlabel('x')
ax3.set_ylabel('sin(x)')

#cuarto subplot con posicion personalizada
ax4=fig.add_subplot(gs[0,0])
ax4.barh(['A','B','C','D','E'],[5,7,3,8,6],color='orange')
ax4.set_title('Grafico de barras horizontal')
ax4.set_xlabel('Valor')
ax4.set_ylabel('Categorias')    

plt.show()