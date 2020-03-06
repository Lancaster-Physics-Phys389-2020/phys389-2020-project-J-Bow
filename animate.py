import math
import numpy as np 
from Particle import Particle
from Tether import Tether
import scipy.constants
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import DataFrame
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,xlim=(-20, 20), ylim=(-20, 20))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

df= pd.read_pickle("output_data_Euler_100_0.0001.csv")

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    line.set_data(df['position'][i][0], df['position'][i][1])
    time_text.set_text('time = %.1f' % df['time'][i])
    return line, time_text

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=1000, interval=5, blit=True)


plt.show()