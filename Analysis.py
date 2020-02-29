import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame

df_1 = pd.read_pickle("output_data_[-1,0].csv")
df_2 = pd.read_pickle("output_data_[0,1].csv")
df_3 = pd.read_pickle("output_data_[1,0].csv")
df_4 = pd.read_pickle("output_data_[0,2].csv")

df_E = pd.read_pickle("output_data.csv")
df_EC = pd.read_pickle("output_data_1.csv")

print(df_E['position'])

#x = [((df['position'][i][0])**2 + (df['position'][i][1])**2)**0.5 for i in range(len(df['position']))]

plt.plot([df_E['position'][i][0] for i in range(len(df_E['position']))],[df_E['position'][i][1] for i in range(len(df_E['position']))], 'red')
plt.plot([df_EC['position'][i][0] for i in range(len(df_EC['position']))],[df_EC['position'][i][1] for i in range(len(df_EC['position']))], 'blue')
plt.show()
#plt.plot(df_EC['time'], [df_EC['omega'][i][2] for i in range(len(df_EC['position']))])
#plt.plot(df_EC['time'], [np.vdot(df_EC['velocity'][i],df_EC['velocity'][i]) for i in range(len(df_EC['position']))])

