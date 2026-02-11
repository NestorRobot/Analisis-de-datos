import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
#MATRIZ TRASPUESTA.
transposed_matriz=matrix.T

print(matrix)
print(transposed_matriz)

arreglo=np.arange(1,21)

reshaped_array=arreglo.reshape(5,4)
print(reshaped_array)

reversed_array=arreglo[::-1]
print(reversed_array)

#aplanar matriz
flattened_matriz=matrix.flatten()
print(matrix)
print(flattened_matriz)