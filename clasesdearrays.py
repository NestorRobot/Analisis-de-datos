import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

array =np.array([[1,2,3],[4,5,6]])
print(array.ndim)
print(array.dtype)

z=np.array(3,dtype=np.uint8)
print(z)

double_array=np.array([1,2,3],dtype='d')
print(double_array)
z=z.astype(np.float64)
print(z)

sum=np.sum(array)
print(sum)
mean=np.mean(array)
std=np.std(array)
print(f'desviacion estandar:{std},promedio : {mean}')