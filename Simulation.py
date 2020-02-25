import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame
deltaT = 0.001
T = 0
endT = 10
Data = []
T_array = []

head = Tether(np.array([4,0,0]),np.array([0,0,0]),np.array([0,0,0]),'head', 1, scipy.constants.pi/2, 1., 0., 0. )

while T <= endT:
    T += deltaT
    head.update_angular(deltaT)
    Data.append([head.name, head.mass, head.position, head.velocity, head.acceleration, head.theta, head.omega, head.alpha, T])
    
    

df = pd.DataFrame(data = Data, columns= ['name', 'mass', 'position', 'velocity', 'acceleration', 'theta', 'omega', 'alpha', 'time'])
df.to_pickle("output_data.csv")

