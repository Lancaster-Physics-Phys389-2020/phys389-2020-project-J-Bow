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
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,xlim=(-6, 6), ylim=(-6, 6))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

df_RK = pd.read_pickle("output_data_Euler-RK.csv")
df_E = pd.read_pickle("output_data_Euler.csv")
df_EC = pd.read_pickle("output_data_Euler-Cromer.csv")
df_ER = pd.read_pickle("output_data_Euler-Richardson.csv")

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate_1(i):
    line.set_data(df_E['position'][i][0], df_E['position'][i][1])
    time_text.set_text('time = %.1f' % df_EC['time'][i])
    return line, time_text

def animate_2(i):
    line.set_data(df_EC['position'][i][0], df_EC['position'][i][1])
    time_text.set_text('time = %.1f' % df_EC['time'][i])
    return line, time_text

def animate_3(i):
    line.set_data(df_ER['position'][i][0], df_ER['position'][i][1])
    time_text.set_text('time = %.1f' % df_ER['time'][i])
    return line, time_text

def animate_4(i):
    line.set_data(df_RK['position'][i][0], df_RK['position'][i][1])
    time_text.set_text('time = %.1f' % df_RK['time'][i])
    return line, time_text

anim_1 = animation.FuncAnimation(fig, animate_1, init_func=init,frames=10000, interval=1, blit=True)
anim_2 = animation.FuncAnimation(fig, animate_2, init_func=init,frames=10000, interval=1, blit=True)
anim_3 = animation.FuncAnimation(fig, animate_3, init_func=init,frames=10000, interval=1, blit=True)
anim_4 = animation.FuncAnimation(fig, animate_4, init_func=init,frames=10000, interval=1, blit=True)

plt.show()