import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
import copy as copy
from pandas import DataFrame
import time
start_time = time.time()


deltaT = 0.001
T = 0
endT = 1000
Number = 1000 # number of data points you want
Data = []
i = 10
TotalIterations = endT/ deltaT
Number_i = TotalIterations/Number

T_array = []

head = Tether(np.array([0,100,0]),np.array([-5,0,0]),'head', 10., scipy.constants.pi/2, 1., 0., 0. )


while T <= endT:
    T += deltaT
    head.update_angular(deltaT, "RK")
    head.update_position()
    head.update_velocity()
    temp_head =copy.deepcopy(head)
    E_total = temp_head.KE_angular() + temp_head.GPE_ang()
    if i >= Number_i:
        temp_head =copy.deepcopy(head)
        E_total = temp_head.KE_angular() + temp_head.GPE_ang()
        Data.append([temp_head.KE_angular(), temp_head.GPE_ang(), E_total,  temp_head.name, temp_head.mass, temp_head.position, temp_head.theta, temp_head.omega, temp_head.alpha, T, temp_head.velocity])
        i = 0
    i += 1


df = pd.DataFrame(data = Data, columns= ['KE', 'GPE', 'total', 'name', 'mass', 'position', 'theta', 'omega', 'alpha', 'time', 'velocity'])
df.to_pickle("data_ER.csv")

print(df)
print("--- %s seconds ---" % (time.time() - start_time))
