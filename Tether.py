from Particle import Particle
import numpy as np
import math
import copy
import scipy.constants

class Tether(Particle):
    """
    """
  
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), name='Ball', mass=1.0, Theta=0.0, Length = 0., omega=np.array([0,0,0], dtype=float), alpha=np.array([0,0,0], dtype=float)):
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, name=name, mass=mass)
        self.theta = self.set_theta()
        self.length = self.set_length()
        self.omega = self.set_omega()
        self.alpha = alpha


    def __repr__(self):
        return '{0}, {1}, {2}, {3},  {4}, {5},  {6}, {7}, {8}'.format(self.name,self.mass,self.position, self.velocity,self.acceleration,self.theta,self.length, self.omega, self.alpha)

    g=9.81
    
    def set_theta(self):
        if self.position[0] ==0:
            if self.position[1] < 0:
                return 0
            else:
                return scipy.constants.pi 
        if self.position[1] == 0:
            if self.position[0] < 0:
                return 3*scipy.constants.pi/2
            else:
                return scipy.constants.pi/2
        else:
            return np.arctan(self.position[1]/self.position[0]) - scipy.constants.pi/2 

    def set_length(self):
        return np.linalg.norm(self.position)

    def set_omega(self):
        return (np.cross(self.position, self.velocity)/(self.length**2))

    def update_angular(self, deltaT, method):

        def update_alpha(self, deltaT):
            self.alpha = np.array([0,0,-(9.81/self.length) * np.sin(self.theta)])

        def update_omega(self, deltaT):
            self.omega += self.alpha * deltaT

        def update_theta(self, deltaT):
            self.theta += self.omega[2] * deltaT

        def update_richardson(self, deltaT):
            alpha_mid = np.array([0,0,(-(9.81/self.length)*np.sin(self.theta + (self.omega[2]*deltaT/2)))])
            self.omega += alpha_mid*deltaT
            self.theta += (self.omega[2] +0.5*self.alpha[2]*deltaT)*deltaT
            self.alpha = alpha_mid

        if method == "Euler":
            update_alpha(self, deltaT)
            update_theta(self, deltaT)
            update_omega(self, deltaT)

        elif method == "Euler-Cromer":
            update_alpha(self, deltaT)
            update_omega(self, deltaT)
            update_theta(self, deltaT)

        elif method == "Euler-Richardson":
            update_alpha(self, deltaT)
            update_richardson(self, deltaT) 

    def update_linear(self, deltaT):
        self.position[0] = self.length * np.cos(self.theta - scipy.constants.pi/2)
        self.position[1] = self.length * np.sin(self.theta - scipy.constants.pi/2)
        #A = a x r + w x r
#        self.acceleration = np.cross((self.alpha), (self.length * (self.position/(np.linalg.norm(self.position))))) + np.cross((self.omega), np.cross(self.omega, (self.length * (self.position/(np.linalg.norm(self.position))))))

#        self.velocity +=  self.acceleration*deltaT

#        self.position += self.velocity*deltaT

    def GPE(self):
        return  self.mass * 9.81 * (self.position[1]+self.length)

    def KE(self):
        return 0.5 *self.mass * np.vdot(self.velocity, self.velocity)