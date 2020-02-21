import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib
import pandas as pd 

deltaT = 0.01
T = 0
endT = 20


head = Tether(np.array([1,0,0]),np.array([0,0,0]),np.array([0,0,0]),'head', 1, scipy.constants.pi/2, 1., 0., 0. )
print("theta after inheritance",head.theta)
while T <= endT:
    T += deltaT
    head.update(deltaT)

    print(head)