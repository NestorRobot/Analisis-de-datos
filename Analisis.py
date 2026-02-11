import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#escalares
escalar =np.array(42)
print(type(escalar))
print(escalar)
#vectores
vector =np.array([30,29,35,31,33,36,45])
print(vector)
#matriz
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
#tensores ---> mas de tres dimensiones.
tensor=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)

array_arange=np.arange(10)
print(array_arange)

#matriz identidad
eye_matrix=np.eye(3)
print(eye_matrix)

#matriz diagonal
matrix_diag=np.diag([1,2,2,3,4])
print(matrix_diag)

#matriz aleatoria entre numeros de 0 a 1
random=np.random.random((2,3))
print(random)