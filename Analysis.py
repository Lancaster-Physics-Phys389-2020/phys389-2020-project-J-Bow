import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame


df_E = pd.read_pickle("output_data_Euler_100_0.0001.csv")
df_EC = pd.read_pickle("output_data_Euler-Cromer_100_0.0001.csv")
df_ER = pd.read_pickle("output_data_Euler-Richardson_100_0.0001.csv")

df = pd.read_pickle("output_data_Euler.csv")

#plt.plot(df_E['time'], df_E['KE'], 'lightcoral' , label = "KE_E")
#plt.plot(df_E['time'], df_E['GPE'], 'indianred', label = "GPE_E")
##plt.plot(df_E['time'], df_E['total'], 'brown',label = "total_E")

#plt.plot(df_EC['time'], df_EC['KE'], 'limegreen',label = "KE_EC")
#plt.plot(df_EC['time'], df_EC['GPE'], 'forestgreen', label = "GPE_EC")
#plt.plot(df_EC['time'], df_EC['total'], 'darkgreen', label = "total_EC")

#plt.plot(df_ER['time'], df_ER['KE'], 'violet', label = "KE_ER")
#plt.plot(df_ER['time'], df_ER['GPE'], 'blueviolet', label = "GPE_ER")
#plt.plot(df_ER['time'], df_ER['total'], 'purple', label = "total_ER")

#plt.legend()
#plt.show()

plt.plot([df['position'][i][0] for i in range(len(df['position']))],[df['position'][i][1] for i in range(len(df['position']))], 'purple', label = "Richardson")

#plt.plot([df_EC['position'][i][0] for i in range(len(df_EC['position']))],[df_EC['position'][i][1] for i in range(len(df_EC['position']))], 'darkgreen', label = "Cromer")

#plt.plot([df_E['position'][i][0] for i in range(len(df_E['position']))],[df_E['position'][i][1] for i in range(len(df_E['position']))], 'brown', label = "Euler")

#plt.legend()
plt.show()


