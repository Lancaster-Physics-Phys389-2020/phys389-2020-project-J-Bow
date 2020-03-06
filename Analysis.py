import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame




df = pd.read_pickle("output_data_Euler.csv")
plt.plot(df['time'], df['KE'], 'lightcoral' , label = "KE_E")
plt.plot(df['time'], df['GPE'], 'indianred', label = "GPE_E")
plt.plot(df['time'], df['total'], 'brown',label = "total_E")

plt.legend()
plt.show()

plt.plot([df['position'][i][0] for i in range(len(df['position']))],[df['position'][i][1] for i in range(len(df['position']))], 'purple', label = "Euler-Cromer")

plt.legend()
plt.show()

plt.plot(df['time'], df['KE'], label = "KE")
plt.plot(df['time'], df['GPE'], label = "GPE")
plt.plot(df['time'], df['total'], label = "total")
plt.legend()
plt.show()