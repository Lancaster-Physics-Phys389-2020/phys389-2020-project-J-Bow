import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame

df = pd.read_pickle("output_data.csv")
#print(df['acceleration'][0][0])
#x_ = [df['acceleration'][i][0] for i in range(len(df['acceleration'])) ]
#print(x_)
#print(df)
"""
y =  [df['position'][i][0] for i in range(len(df['position']))]
print(y)
x =  [df['position'][i][1] for i in range(len(df['position']))]
print(x)
plt.plot([df['position'][i][1] for i in range(len(df['position']))],[df['position'][i][0] for i in range(len(df['position']))], 'red')
plt.show()
"""
"""
plt.plot(df['time'], [df['acceleration'][i][0] for i in range(len(df['acceleration'])) ], 'red', label = 'x')
plt.plot(df['time'], [df['acceleration'][i][1] for i in range(len(df['acceleration'])) ], 'blue', label = 'y')
plt.plot(df['time'], df['alpha'], 'green', label = 'alpha')
plt.legend()
plt.show()
"""


plt.plot(df['time'], df['theta'])
plt.show()