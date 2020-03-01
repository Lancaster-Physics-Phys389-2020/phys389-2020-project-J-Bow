import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
import copy as copy
from pandas import DataFrame

deltaT = 0.01
T = 0
endT = 100
Data = []
i = 10


head = Tether(np.array([5,0,0]),np.array([0,0,0]),np.array([0,0,0]),'head', 1, scipy.constants.pi/2, 1., 0., 0. )


while T <= endT:
    T += deltaT
    head.update_angular(deltaT, "Euler")
    head.update_linear(deltaT)
    temp_head =copy.deepcopy(head)
    E_total = temp_head.KE() +temp_head.GPE()
#    if i >= 100:
    Data.append([temp_head.KE(), temp_head.GPE(), E_total,  temp_head.name, temp_head.mass, temp_head.position, temp_head.acceleration, temp_head.theta, temp_head.omega, temp_head.alpha, T, temp_head.velocity])
#        i = 0
#    i += 1


df = pd.DataFrame(data = Data, columns= ['KE', 'GPE', 'total', 'name', 'mass', 'position', 'acceleration', 'theta', 'omega', 'alpha', 'time', 'velocity'])
df.to_pickle("output_data_Euler.csv")
print(df)