import pandas as pd

df=pd.read_csv('Data/online_retail.csv',encoding='latin1')
print(df.head())
df.info()
df.columns
#pasar la columna de fecha a formato datetime
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
df.info()
#quitar filas con valores nulos en la columna de fecha
df.dropna(subset=['InvoiceDate'],inplace=True)
df.set_index('InvoiceDate',inplace=True)
print(df.head())
#extraer año, mes, dia y hora de la columna de fecha
df['Year']=df.index.year
df['Month']=df.index.month  
df['Day']=df.index.day
df['Hour']=df.index.hour
print(df.head())
#eliminar las columnas de año, mes, dia y hora
df.drop(columns=['Year','Month','Day','Hour'],inplace=True)
print(df.head())
#extraer informacion de un año especifico
df_2011_december=df.loc['2011-12']
print(df_2011_december.head())

#rango de fechas  y dias

df_dec_range=df.loc['2010-12-01':'2010-12-15']
print(df_dec_range.head())



