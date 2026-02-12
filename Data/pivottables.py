import pandas as pd
df=pd.read_csv('Data/online_retail.csv',encoding='latin1')
#creando una tabla pivote para analizar la cantidad total de ventas por pais y por producto
pivot_table=pd.pivot_table(df,values='Quantity',index='Country',
                           columns='StockCode',aggfunc='sum')
print(pivot_table)

#MAS COLUMNAS
pivot_table=pd.pivot_table(df,values='Quantity',index='Country',
                           columns=['StockCode','Description'],aggfunc='sum')