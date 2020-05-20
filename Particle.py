import numpy as np
import math
import copy
import scipy.constants

class Particle:
    """
    Class to model a particle being acted on by a force. 
    Calculates conserved properties.

    mass in kg 
    position and velocity in m 
    """

    

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float),name='Ball', mass=1.0):
        self.name = name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.mass = mass

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}'.format(self.name,self.mass,self.position, self.velocity)

    def GPE(self):
        """
        find the gravitational potential energy
        """
        return  self.mass * 9.81 * (self.position[1]+np.linalg.norm(self.position))

    def KE_linear(self):
        return 0.5 *self.mass * np.vdot(self.velocity, self.velocity)
  
    def momentum(self):
        return self.mass*np.array(self.velocity)



 