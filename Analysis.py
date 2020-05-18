import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame

df_RK = pd.read_pickle("output_data_Euler-RK.csv")
df_E = pd.read_pickle("output_data_Euler.csv")
df_EC = pd.read_pickle("output_data_Euler-Cromer.csv")
df_ER = pd.read_pickle("output_data_Euler-Richardson.csv")
plt.figure("position")
#plt.plot([df_E['position'][i][0] for i in range(len(df_E['position']))],[df_E['position'][i][1] for i in range(len(df_E['position']))], 'purple', label = "Euler")
#plt.plot([df_EC['position'][i][0] for i in range(len(df_EC['position']))],[df_EC['position'][i][1] for i in range(len(df_EC['position']))], 'violet', label = "Euler-Cromer")
plt.plot([df_ER['position'][i][0] for i in range(len(df_ER['position']))],[df_ER['position'][i][1] for i in range(len(df_ER['position']))], 'blue', label = "Euler-Richardson")
#plt.plot([df_RK['position'][i][0] for i in range(len(df_RK['position']))],[df_RK['position'][i][1] for i in range(len(df_RK['position']))], 'steelblue', label = "Runge Kutta")
plt.legend()

plt.figure("energy")
#plt.plot(df_E['time'], df_E['total'], label = "Euler")
#plt.plot(df_E['time'], df_EC['total'], label = "Euler Cromer")
plt.plot(df_ER['time'], df_ER['total'], label = "Euler Richardson")
#plt.plot(df_E['time'], df_RK['total'], label = "Runge Kutta")
plt.legend()

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


