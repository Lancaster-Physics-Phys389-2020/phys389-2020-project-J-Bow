import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame

df = pd.read_pickle("data_ER_0.01.csv")


plt.figure("amplitude")
plt.plot(df['time'], [df['position'][i][0] for i in range(len(df['position']))])

plt.figure('energy')
plt.plot(df['time'], -(df['KE'][0]-df['KE']), 'yellow' , label = "KE_E")
plt.plot(df['time'], -(df['GPE'][0]-df['GPE']), 'green', label = "GPE_E")
plt.plot(df['time'], -(df['total'][0]-df['total']), 'palegreen',label = "total_E")
plt.legend()

plt.show()


"""
df_RK01 = pd.read_pickle("data_RK_0.01.csv")
df_RK001 = pd.read_pickle("data_RK_0.001.csv")
df_RK0001 = pd.read_pickle("data_RK_0.0001.csv")


df_ER01 = pd.read_pickle("data_ER_0.01.csv")
df_ER001 = pd.read_pickle("data_ER_0.001.csv")
df_ER0001 = pd.read_pickle("data_ER_0.0001.csv")

df_E = pd.read_pickle("data_E_0.001.csv")
df_EC = pd.read_pickle("data_EC_0.001.csv")

plt.figure("Euler_richardson_deltaT")
plt.plot(df_ER01['time'], (df_ER01['total']- df_RK01['total'][0])/df_RK01['total'][0],'cornflowerblue', label = "deltaT = 0.01")
plt.plot(df_ER001['time'], (df_ER001['total']- df_RK01['total'][0])/df_RK01['total'][0],'royalblue', label = "deltaT = 0.001")
plt.plot(df_ER0001['time'], (df_ER0001['total']- df_RK01['total'][0])/df_RK01['total'][0],'mediumblue', label = "deltaT = 0.0001")
plt.ylabel(' % error in Total energy')
plt.xlabel('Time / s')
plt.legend()

plt.figure("RK_deltaT")
plt.plot(df_RK01['time'], (df_RK01['total']- df_RK01['total'][0])/df_RK01['total'][0],'palegreen', label = "deltaT = 0.01")
plt.plot(df_RK001['time'], (df_RK001['total']- df_RK01['total'][0])/df_RK01['total'][0],'limegreen', label = "deltaT = 0.001")
plt.plot(df_RK0001['time'], (df_RK0001['total']- df_RK01['total'][0])/df_RK01['total'][0],'green', label = "deltaT = 0.0001")
plt.ylabel(' % error in Total energy')
plt.xlabel('Time / s')
plt.legend()


plt.show()

"""


#plt.figure("position")
#plt.plot([df_E['position'][i][0] for i in range(len(df_E['position']))],[df_E['position'][i][1] for i in range(len(df_E['position']))], 'purple', label = "Euler")
#plt.plot([df_EC['position'][i][0] for i in range(len(df_EC['position']))],[df_EC['position'][i][1] for i in range(len(df_EC['position']))], 'violet', label = "Euler-Cromer")
#plt.plot([df_ER['position'][i][0] for i in range(len(df_ER['position']))],[df_ER['position'][i][1] for i in range(len(df_ER['position']))], 'blue', label = "Euler-Richardson")
#plt.plot([df_RK['position'][i][0] for i in range(len(df_RK['position']))],[df_RK['position'][i][1] for i in range(len(df_RK['position']))], 'palegreen', label = "Runge Kutta")

#plt.legend()


df_E = pd.read_pickle("data_E_100_0.001.csv")
df_EC = pd.read_pickle("data_EC_100_0.001.csv")
df_ER = pd.read_pickle("data_ER_100_0.001.csv")
df_RK = pd.read_pickle("data_RK_100_0.001.csv")

plt.figure("energy_all")
plt.plot(df_E['time'], (df_E['total']- df_RK['total'][0])/df_RK['total'][0],'purple', label = "Euler")
plt.plot(df_E['time'], (df_EC['total']- df_RK['total'][0])/df_RK['total'][0],'violet', label = "Euler Cromer")
plt.plot(df_ER['time'], (df_ER['total']- df_RK['total'][0])/df_RK['total'][0],'blue', label = "Euler Richardson")
plt.plot(df_RK['time'], (df_RK['total'] - df_RK['total'][0])/df_RK['total'][0],'palegreen', label = "Runge Kutta")
plt.ylabel(' % error in Total energy')
plt.xlabel('Time / s')
plt.legend()

plt.figure("energy-E")
plt.plot(df_E['time'], (df_EC['total']- df_RK['total'][0])/df_RK['total'][0],'violet', label = "Euler Cromer")
plt.plot(df_E['time'], (df_ER['total']- df_RK['total'][0])/df_RK['total'][0],'blue', label = "Euler Richardson")
plt.plot(df_E['time'], (df_RK['total'] - df_RK['total'][0])/df_RK['total'][0],'palegreen', label = "Runge Kutta")
plt.ylabel(' % error in Total energy')
plt.xlabel('Time / s')
plt.legend()

plt.figure("energy_ER+RK_0.0001")
plt.plot(df_ER['time'], (df_ER['total']- df_RK['total'][0])/df_RK['total'][0],'blue', label = "Euler Richardson")
plt.plot(df_RK['time'], (df_RK['total'] - df_RK['total'][0])/df_RK['total'][0],'palegreen', label = "Runge Kutta")
plt.ylabel(' % error in Total energy')
plt.xlabel('Time / s')
plt.legend()

plt.figure("energy_RK_only_0.0001")
plt.plot(df_RK['time'], (df_RK['total'] - df_RK['total'][0])/df_RK['total'][0],'palegreen', label = "Runge Kutta")
plt.ylabel(' % error in Total energy')
plt.xlabel('Time / s')
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

plt.figure("1")

plt.plot(df_RK['time'], df_ER['KE'], 'yellow' , label = "KE_E")
plt.plot(df_RK['time'], df_ER['GPE'], 'green', label = "GPE_E")
plt.plot(df_RK['time'], df_ER['total'], 'palegreen',label = "total_E")

plt.legend()
"""




