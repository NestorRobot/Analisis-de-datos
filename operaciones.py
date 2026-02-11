import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

prices=np.array([100,200,300])
discount=np.array([0.9])


pices_discount=prices*discount
print(pices_discount)

prices2=np.random.randint(100,500 , size=(3,3))
discount2=np.array([10,20,30])
prices_discount2=prices2+discount2
print(prices_discount2)

array3=np.array([1,2,3,4,5])
print(np.all(array3>0))

#concatenacion 
array_a=np.array([1,2,3])
array_b=np.array([3,42,35])
array_b_a=np.concatenate((array_b,array_a))
print(array_b_a)
array_a_b=np.concatenate((array_a,array_b))
print(array_a_b)

#stacking concatenacion vertical u horizontal
stacked_v=np.vstack((array_a,array_b))
print(stacked_v)
stacked_h=np.hstack((array_a,array_b))
print(stacked_h)

#
array_c=np.arange(1,10)
split_array=np.split(array_c,3)
print(split_array)