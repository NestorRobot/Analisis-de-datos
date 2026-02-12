import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

product_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
product_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
product_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])

meses=np.array(["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio", "Agosto",
                "Septiembre", "Octubre","Noviembre","Diciembre"])



ventas_A=np.sum([product_A])
ventas_B=np.sum([product_B])
ventas_C=np.sum([product_C])

media_A=np.mean(product_A)
media_B=np.mean(product_B)
media_C=np.mean(product_C)

print(f'Media ventas producto A:{media_A},Suma de ventas producto A {ventas_A}',
      f'Media ventas producto B:{media_B},Suma de ventas producto B {ventas_B}',
      f'Media ventas producto A:{media_C},Suma de ventas producto C {ventas_C}')

Ventas_total=np.array(product_A+product_B+product_C)
print(f'Ventas_total:{Ventas_total}')
for i in range(len(meses)):
    print(f'{meses[i]}:{Ventas_total[i]}')

Valor_mayor_venta=np.argmax(Ventas_total)
Valor_menor_venta=np.argmin(Ventas_total)


print(f'Mes de mayor venta:{meses[Valor_mayor_venta]}, valor de venta : {Ventas_total.max()}')
print(f'Mes de menor venta:{meses[Valor_menor_venta]},valor de venta : {Ventas_total.min()}')

#RESHAPE

matrix=np.array([product_A,product_B,product_C])
print(matrix)
print('Matriz reshaped')
matriz_res=matrix.reshape(3,4,3)
print(matriz_res)

#transpuesta de ventas
venta_t=Ventas_total.T
print('ventas traspuesta')
print(venta_t)
#invertir
inv_venta_A=product_A[::-1]
inv_venta_B=product_B[::-1]
inv_venta_C=product_C[::-1]

print(f' inversion A:{inv_venta_A} ',
      f' inversion B:{inv_venta_B} ',
      f' inversion C:{inv_venta_C} ')
#FLAT VENTAS
Flat_ventas=Ventas_total.flatten()
print(Flat_ventas)