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


deltaT = 0.00001  #time step in seconds  
endT = 100  #length of simulation in seconds
Number = 1000   # number of data points you want
initial_position = np.array([-2,-2,0])  #position vector [x, y, z] in km
initial_velocity = np.array([0,0,0])    #velocity vector [x, y, z] in kms^-1
mass = 1.0  #mass in kg
method = "EC"
dataName = "data_EC_100_0.00001.csv" # must end in .csv
C_d = 2 #coefficient of drag of head
A = 1   #surface area of head in km^2
h = 300 #altitude in km
v = 7.725   #orbital velocity in kms^-1


T = 0
Data = []
i = 0
TotalIterations = endT/ deltaT
Number_i = TotalIterations/Number
head = Tether(initial_position,initial_velocity,'head', mass, scipy.constants.pi/2, 1., 0., 0. )
T_array = []



while T <= endT:
    T += deltaT
    head.update_angular(deltaT, method)
    head.update_position()
    head.update_velocity()
    temp_head =copy.deepcopy(head)
    E_total = temp_head.KE_angular() + temp_head.GPE()
    if i >= Number_i:
        temp_head =copy.deepcopy(head)
        E_total = temp_head.KE_angular() + temp_head.GPE()
        Data.append([temp_head.KE_angular(), temp_head.GPE(), E_total,  temp_head.name, temp_head.mass, temp_head.position, temp_head.theta, temp_head.omega, temp_head.alpha, T, temp_head.velocity])
        i = 0
    i += 1


df = pd.DataFrame(data = Data, columns= ['KE', 'GPE', 'total', 'name', 'mass', 'position', 'theta', 'omega', 'alpha', 'time', 'velocity'])
df.to_pickle(dataName)

print(df)
print("--- %s seconds ---" % (time.time() - start_time))
