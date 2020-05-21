import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame

"""
plt.figure('E')
df_E1 = pd.read_pickle("data_E_0.1.csv")
plt.plot(df_E1['time'], (df_E1['total']- df_E1['total'][0])/df_E1['total'][0],'purple', label = "Euler 0.1")
df_E01 = pd.read_pickle("data_E_0.01.csv")
plt.plot(df_E01['time'], (df_E01['total']- df_E01['total'][0])/df_E01['total'][0],'blue', label = "Euler 0.01")
df_E001 = pd.read_pickle("data_E_0.001.csv")
plt.plot(df_E001['time'], (df_E001['total']- df_E001['total'][0])/df_E001['total'][0],'black', label = "Euler 0.001")
plt.legend()

plt.figure('EC')
df_EC1 = pd.read_pickle("data_EC_0.1.csv")
plt.plot(df_EC1['time'], (df_EC1['total']- df_EC1['total'][0])/df_EC1['total'][0],'purple', label = "Euler-Cromer 0.1")
df_EC01 = pd.read_pickle("data_EC_0.01.csv")
plt.plot(df_EC01['time'], (df_EC01['total']- df_EC01['total'][0])/df_EC01['total'][0],'blue', label = "Euler-Cromer 0.01")
df_EC001 = pd.read_pickle("data_EC_0.001.csv")
plt.plot(df_EC001['time'], (df_EC001['total']- df_EC001['total'][0])/df_EC001['total'][0],'black', label = "Euler-Cromer 0.001")
plt.legend()

plt.figure('ER')
df_ER1 = pd.read_pickle("data_ER_0.1.csv")
plt.plot(df_ER1['time'], (df_E1['total']- df_ER1['total'][0])/df_ER1['total'][0],'purple', label = "Euler-Richardson 0.1")
df_ER01 = pd.read_pickle("data_ER_0.01.csv")
plt.plot(df_ER01['time'], (df_ER01['total']- df_ER01['total'][0])/df_ER01['total'][0],'blue', label = "Euler-Richardson 0.01")
df_ER001 = pd.read_pickle("data_ER_0.001.csv")
plt.plot(df_ER001['time'], (df_ER001['total']- df_ER001['total'][0])/df_ER001['total'][0],'black', label = "Euler-Richardson 0.001")
plt.legend()
"""
plt.figure('RK')
df_RK1 = pd.read_pickle("data_RK_100_0.01.csv")
#plt.plot(df_RK1['time'], (df_RK1['total']- df_RK1['total'][0])/df_RK1['total'][0],'purple', label = "Runge-Kutta 0.1")
df_RK01 = pd.read_pickle("data_RK_100_0.001.csv")
plt.plot(df_RK01['time'], (df_RK01['total']- df_RK01['total'][0])/df_RK01['total'][0],'blue', label = "Runge-Kutta 0.001")
df_RK001 = pd.read_pickle("data_RK_100_0.0001.csv")
plt.plot(df_RK001['time'], (df_RK001['total']- df_RK001['total'][0])/df_RK001['total'][0],'black', label = "Runge-Kutta 0.0001")
df_RK0001 = pd.read_pickle("data_RK_100_0.00001.csv")
plt.plot(df_RK0001['time'], (df_RK0001['total']- df_RK0001['total'][0])/df_RK0001['total'][0],'green', label = "Runge-Kutta 0.00001")
plt.legend()

"""
plt.figure('0.001')
plt.plot(df_RK001['time'], (df_RK001['total']- df_RK001['total'][0])/df_RK001['total'][0],'purple', label = "Runge-Kutta 0.001")
plt.plot(df_ER001['time'], (df_ER001['total']- df_ER001['total'][0])/df_ER001['total'][0],'black', label = "Euler-Richardson 0.001")
plt.plot(df_EC001['time'], (df_EC001['total']- df_EC001['total'][0])/df_EC001['total'][0],'blue', label = "Euler-Cromer 0.001")
plt.plot(df_E001['time'], (df_E001['total']- df_E001['total'][0])/df_E001['total'][0],'green', label = "Euler 0.001")
"""
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
"""
plt.figure("energy_all")
plt.plot(df_E['time'], (df_E['total']- df_RK['total'][0])/df_RK['total'][0],'purple', label = "Euler")
plt.plot(df_E['time'], (df_EC['total']- df_RK['total'][0])/df_RK['total'][0],'violet', label = "Euler Cromer")
plt.plot(df_ER['time'], (df_ER['total']- df_RK['total'][0])/df_RK['total'][0],'blue', label = "Euler Richardson")
plt.plot(df_RK['time'], (df_RK['total'] - df_RK['total'][0])/df_RK['total'][0],'palegreen', label = "Runge Kutta")
plt.ylabel(' % error in Total energy')
plt.xlabel('Time / s')
plt.legend()
"""
"""
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
"""
"""
plt.figure()
plt.plot(df['time'], [np.linalg.norm(df['velocity'][i]) for i in range(len(df['velocity']))], label= "velocity")
plt.plot(df['time'], [df['omega'][i][2] for i in range(len(df['omega']))], label= "omega")
plt.xlabel('time')
plt.ylabel('velocity')
plt.legend()
plt.show()
"""
"""
plt.figure("1")

plt.plot(df_RK['time'], df_ER['KE'], 'yellow' , label = "KE_E")
plt.plot(df_RK['time'], df_ER['GPE'], 'green', label = "GPE_E")
plt.plot(df_RK['time'], df_ER['total'], 'palegreen',label = "total_E")

plt.legend()

"""
