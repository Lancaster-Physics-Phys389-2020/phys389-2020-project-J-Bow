import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame

df = pd.read_pickle("output_data.csv")


x = [((df['position'][i][0])**2 + (df['position'][i][1])**2)**0.5 for i in range(len(df['position']))]
print(x)

plt.plot([df['position'][i][0] for i in range(len(df['position']))],[df['position'][i][1] for i in range(len(df['position']))], 'red')
plt.show()