from Particle import Particle
import numpy as np
from unittest.mock import patch
import math
import copy
import pylab
import scipy.constants
import matplotlib.pyplot as plt 
i = 0

data = np.array([  
  [180.0, 6.147E-13],
  [190.0, 4.318E-13],
  [200.0, 3.100E-13],
  [210.0, 2.266E-13],
  [220.0, 1.680E-13],
  [230.0, 1.262E-13],
  [240.0, 9.584E-14],
  [250.0, 7.348E-14],
  [260.0, 5.683E-14],
  [270.0, 4.429E-14],
  [280.0, 3.476E-14],
  [290.0, 2.745E-14],
  [300.0, 2.181E-14],
  [320.0, 1.397E-14],
  [310.0, 1.741E-14],
  [330.0, 1.125E-14],
  [340.0, 9.102E-15],
  [350.0, 7.388E-15],
  [360.0, 6.017E-15],
  [370.0, 4.916E-15],
  [380.0, 4.027E-15],
  [390.0, 3.307E-15],
  [400.0, 2.723E-15],
  [410.0, 2.247E-15],
  [420.0, 1.859E-15],
  ])

height = np.array([ i[0] for i in data])
rho = np.array([(np.log10(i[1])*10**-3) for i in data])

p = pylab.polyfit(height, rho, 1)
p1 = pylab.poly1d(p)
params = p1.coefficients

print(params)

h1 = np.array([i for i in range(200, 400, 10)])

def density(h):
  return(-1.02634886e-05 *h + -1.05177549e-02)

rho1= np.array([(density(h1[i])) for i in range(len(h1))])

print(height)
print(rho)

plt.scatter([i for i in rho], [i for i in height])
plt.plot([i for i in rho1], [i for i in h1])
plt.show()