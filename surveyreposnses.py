import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

respuestas = np.array(['bueno', 'excelente', 'malo', 'bueno', 'excelente', 'bueno', 'malo', 'excelente'])
#respuestas mas comunes con el metodo unique
print(np.unique(respuestas))

#conteo de elemetos
unique_elements, counts=np.unique(respuestas,return_counts=True)

print(unique_elements)
print(counts)
array_x=np.arange(10)
view_y=array_x[1:3]
print(view_y)