import pandas as pd
df=pd.read_csv('Data/online_retail.csv',encoding='latin1')
print(df.head())
print(type(df))

print(df.describe())
#nombre de columnas
colums_names=df.columns
print(colums_names)
#dimension del dataframe
dimension=df.ndim
print(f'la dimension del dataframe es : {dimension}')
#numero de filas y columnas
num_rows,num_cols=df.shape
print(f'El numero de filas es : {num_rows} y el numero de columnas es : {num_cols}')

daily_sells=df['Quantity']
print(daily_sells)
mean_dally_sells=daily_sells.mean()
print(f'la media de ventas diarias es : {mean_dally_sells}')
median_daily_sells=daily_sells.median()
print(f'la mediana de ventas diarias es : {median_daily_sells}')
desv_daily_sells=daily_sells.std()
print(f'la desviacion estandar de ventas diarias es : {desv_daily_sells}')
#conteo de los valores
cont_daily_sales=daily_sells.count()
print(f'el conteo de ventas diarias es : {cont_daily_sales}')
#usando iloc y loc
first_row=df.iloc[0]
print(f'la primera fila del dataframe es : {first_row}')
first_row=df.iloc[:5]
print(f'la primera fila del dataframe es : {first_row}')

subset=df.iloc[:3,:2]
print(subset)
#usando la etiqueta de las columnas

row_index=df.loc[3]
print(f'la fila con indice 3 es : {row_index}')

data_quanttiy_priceunit=df.loc[:,['Quantity','UnitPrice']]
print(data_quanttiy_priceunit)
#identificar datos faltantes

missing_data=df.isna()
print(missing_data)
count_missing_data=df.isna().sum()
print(f'el conteo de datos faltantes por columna es : {count_missing_data}')
#elimina las filas con datos faltantes
no_missing_rows=df.dropna()
print(no_missing_rows)
#quitando columnas con datos faltantes
no_missing_colums=df.dropna(axis=1)
print(no_missing_colums)
#rellenar faltantes con un valor especifico
filled_zeros=df.fillna(0)  
print(filled_zeros)     

#rellenando con la media de los datos 
mean_unitprice=df['UnitPrice'].mean()
filled_mean=df['UnitPrice'].fillna(mean_unitprice)
print(filled_mean)
#crear una nueva columna con el total de precio
df['TotalPrice']=df['Quantity']*df['UnitPrice']
print(df.head())

#creando una nueva columna con comparativos
df['high_value']=df['TotalPrice']>10
print(df['high_value'].head(30))

df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
print(df['InvoiceDate'].head())

#aplicando lambda para crear una nueva columna con descuento del 10% en el precio unitario
df['DiscuntPrice']=df['UnitPrice'].apply(lambda x: x*0.9)
print(df.head())

#categoriza precios

def categorize_price(price):
    if price >50:
        return 'High'
    elif price < 20:
        return 'Medium'
    else:
        return 'Low'

df['PriceCategory']=df['UnitPrice'].apply(categorize_price)
print(df.head(30))