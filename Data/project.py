import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df=pd.read_csv('Data/online_retail.csv',encoding='latin1')
print(df.head().info())
print(df.describe())

print(df.isnull().sum())
print("Número de filas duplicadas:", df.duplicated().sum())
unique_values={col: df[col].unique()for col in df.columns}
for col, values in unique_values.items():
    print(f"Columna: {col}, Valores únicos: {len(values)}...")  # Mostrar solo los primeros 5 valores únicos
    print(f'Valores Unicos :{values[:10]}')
    print("\n")

#limpiar los datos eliminando filas con valores faltantes
df_cleaned=df.drop_duplicates()
dt_cleaned=df.dropna(subset=['CustomerID'])

print(dt_cleaned.isnull().sum())
print(dt_cleaned.isna().sum())

df_cleaned['Total_amount']=df_cleaned['Quantity']*df_cleaned['UnitPrice']
print(df_cleaned.head())

df_cleaned['InvoiceDate']=pd.to_datetime(df_cleaned['InvoiceDate'])
print(df_cleaned.info())

df_cleaned['Year']=df_cleaned['InvoiceDate'].dt.year
df_cleaned['Month']=df_cleaned['InvoiceDate'].dt.month
print(df_cleaned.head())

sales_by_year=df_cleaned.groupby('Year')['Total_amount'].sum()
print(sales_by_year)

df_cleaned['Semester']=df_cleaned['Month'].apply(lambda x:1 if x<=6 else 2)
sales_by_semester=df_cleaned.groupby(['Year','Semester'])['Total_amount'].sum()
print(sales_by_semester)

def month_to_quarter(month):
    if month in [1, 2, 3]:
        return 'Q1'
    elif month in [4, 5, 6]:
        return 'Q2'
    elif month in [7, 8, 9]:
        return 'Q3'
    else:
        return 'Q4'
df_cleaned['Quarter']=df_cleaned['Month'].apply(month_to_quarter)
sales_by_quarter=df_cleaned.groupby(['Year','Quarter'])['Total_amount'].sum()
print(sales_by_quarter)

def convert_to_month_name(month):
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
    return month_names[month-1]

df_cleaned['Month_name']=df_cleaned['Month'].apply(convert_to_month_name)

sales_by_month=df_cleaned.groupby(['Month_name','Country'])['Total_amount'].sum()
print(sales_by_month)

total_returns=df_cleaned[df_cleaned['Quantity']<0].shape[0]
print(total_returns)

total_no_returns=df_cleaned[df_cleaned['Quantity']>=0].shape[0]
print(total_no_returns)

labels=['Devoluciones','No Devoluciones']
sizes=[total_returns,total_no_returns]
colors=['red','green']
plt.figure(figsize=(8,8))
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('Proporción de Devoluciones vs No Devoluciones')
plt.show()

plt.figure(figsize=(12,6))
df_cleaned.groupby('Country')['Total_amount'].sum().plot(kind='bar',color='blue')
plt.title('Ventas por Mes año por País')
plt.xlabel('País')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45) 
plt.show()

top_products=df_cleaned.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(10)
print(top_products)

top_products.reset_index()
top_products=pd.merge(top_products,df_cleaned[['StockCode','Description']].drop_duplicates(),on='StockCode',how='left')

plt.figure(figsize=(12,6))
plt.barh(top_products['Description'],top_products['Quantity'],color='orange')
plt.title('Top 10 Productos más Vendidos')
plt.xlabel('Cantidad Vendida')
plt.ylabel('Producto')  
plt.gca().invert_yaxis()
plt.show()