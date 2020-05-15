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
plt.plot([df_E['position'][i][0] for i in range(len(df_E['position']))],[df_E['position'][i][1] for i in range(len(df_E['position']))], 'purple', label = "Euler")
plt.plot([df_EC['position'][i][0] for i in range(len(df_EC['position']))],[df_EC['position'][i][1] for i in range(len(df_EC['position']))], 'violet', label = "Euler-Cromer")
plt.plot([df_ER['position'][i][0] for i in range(len(df_ER['position']))],[df_ER['position'][i][1] for i in range(len(df_ER['position']))], 'blue', label = "Euler-Richardson")
plt.plot([df_RK['position'][i][0] for i in range(len(df_RK['position']))],[df_RK['position'][i][1] for i in range(len(df_RK['position']))], 'steelblue', label = "Runge Kutta")
plt.legend()

plt.figure("energy")
plt.plot(df_E['time'], df_E['total'], label = "Euler")
plt.plot(df_E['time'], df_EC['total'], label = "Euler Cromer")
plt.plot(df_ER['time'], df_ER['total'], label = "Euler Richardson")
plt.plot(df_E['time'], df_RK['total'], label = "Runge Kutta")
plt.legend()

plt.show()

"""
plt.figure()
plt.plot(df['time'], [np.linalg.norm(df['velocity'][i]) for i in range(len(df['velocity']))], label= "velocity")
plt.plot(df['time'], [df['omega'][i][2] for i in range(len(df['omega']))], label= "omega")
plt.xlabel('time')
plt.ylabel('velocity')
plt.legend()
plt.show()
"""
plt.figure("1")

plt.plot(df_ER['time'], df_ER['KE'], 'lightcoral' , label = "KE_E")
plt.plot(df_ER['time'], df_ER['GPE'], 'indianred', label = "GPE_E")
plt.plot(df_ER['time'], df_ER['total'], 'brown',label = "total_E")

plt.legend()
plt.show()

