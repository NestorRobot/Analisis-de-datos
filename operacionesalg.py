import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
#SUMA DE MATRICES
Sum=A+B
print(Sum)
#MULTIPLICACION DE MATRICES
Mult=np.dot(A,B)
print(Mult)
#DETERMINANTE DE UNA MATRIZ
Det_b=np.linalg.det(B)
print(Det_b)
Det_A=np.linalg.det(A)
print(Det_A)
#INVERSA DE UNA MATRIZ
Inv_A=np.linalg.inv(A)
print(Inv_A)

#RESOLVER SISTEMA DE ECUACIONES AX=B
A=np.array([[1,2],[3,4]])
x=np.array([9,11])
u=np.linalg.solve(A,x)
print(u)
