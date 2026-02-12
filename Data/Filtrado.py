import pandas as pd
df=pd.read_csv('Data/online_retail.csv',encoding='latin1')

#filtrar ventas en el reuno unido
uk_sales=df[df['Country']=='United Kingdom']
print(uk_sales)

#filtrar ventas con cantidad mayor a 10
high_quantity_Sales=df[df['Quantity']>10]
print(high_quantity_Sales)

#Otra forma de filtrar ventas con cantidad mayor a 10 combinando condiciones
uk_high_quantity_sales=df[(df['Country']=='United Kingdom')&(df['Quantity']>10)]
print(uk_high_quantity_sales)

#fitrado de ventas por año
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
sales_2010=df[df['InvoiceDate'].dt.year==2010]
print(sales_2010)
#por mes y año
december_sales_2010=df[(df['InvoiceDate'].dt.year==2010) & (df['InvoiceDate'].dt.month==12)]
print(december_sales_2010)