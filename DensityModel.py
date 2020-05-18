from Particle import Particle
import numpy as np
from unittest.mock import patch
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt 

data = np.array[  200.0, 3.100E-13,
  210.0, 2.266E-13,
  220.0, 1.680E-13,
  230.0, 1.262E-13,
  240.0, 9.584E-14,
  250.0, 7.348E-14,
  260.0, 5.683E-14,
  270.0, 4.429E-14,
  280.0, 3.476E-14,
  290.0, 2.745E-14,
  300.0, 2.181E-14,
  310.0, 1.741E-14,
  320.0, 1.397E-14,
  330.0, 1.125E-14,
  340.0, 9.102E-15,
  350.0, 7.388E-15,
  360.0, 6.017E-15,
  370.0, 4.916E-15,
  380.0, 4.027E-15,
  390.0, 3.307E-15,
  400.0, 2.723E-15]

h = [i for i in data[2*i] ]
print h