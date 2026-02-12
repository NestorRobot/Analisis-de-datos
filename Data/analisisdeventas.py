import pandas as pd
df=pd.read_csv('Data/online_retail.csv',encoding='latin1')
print(df.head())
print(type(df))
#cantidad de ventas por pais
country_counts=df['Country'].value_counts()
print(country_counts)

#agrupamiento por pais ventas totales en $
sales_by_country=df.groupby('Country')['Quantity'].sum()
print(sales_by_country)

#ESTADISTICOS 
country_stats=df.groupby('Country')['UnitPrice'].agg(['mean','median','std'])
print(country_stats)

country_stock=df.groupby(['Country','StockCode'])['Quantity'].sum()
print(country_stock)

def revenue_total(group):
    return (group['Quantity'])*group['UnitPrice'].sum()
revenue_per_country=df.groupby('Country').apply(revenue_total)
print(revenue_per_country)

df['Total_sales']=df['Quantity']*df['UnitPrice']
print(df)

total_sales_by_country=df.groupby('Country')['Total_sales'].sum()
print(total_sales_by_country)

top3_sellers=total_sales_by_country.sort_values(ascending=False).head(3)
print(top3_sellers)

top3_low_sellers=total_sales_by_country.sort_values(ascending=True).head(3) 
print(top3_low_sellers)    