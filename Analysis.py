import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame


df = pd.read_pickle("output_data_1.csv")


print(df['position'])

#x = [((df['position'][i][0])**2 + (df['position'][i][1])**2)**0.5 for i in range(len(df['position']))]

plt.plot([df['position'][i][0] for i in range(len(df['position']))],[df['position'][i][1] for i in range(len(df['position']))], 'red')
#plt.plot([df_EC['position'][i][0] for i in range(len(df_EC['position']))],[df_EC['position'][i][1] for i in range(len(df_EC['position']))], 'blue')
plt.show()

plt.plot(df['time'], df['KE'], label = "KE")
plt.plot(df['time'], df['GPE'], label = "GPE")
plt.plot(df['time'], df['total'], label = "total")
plt.legend()
plt.show()