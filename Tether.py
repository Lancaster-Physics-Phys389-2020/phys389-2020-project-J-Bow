from Particle import Particle
import numpy as np
import math
import copy
import scipy.constants

class Tether(Particle):
    """
    """
  
    def __init__(self, Position=np.array([1,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), name='Ball', mass=1.0, Theta=0.0, Length = 0., omega=np.array([0,0,0], dtype=float), alpha=np.array([0,0,0], dtype=float)):
        super().__init__(Position=Position, Velocity=Velocity, name=name, mass=mass)
        self.theta = self.set_theta()
        self.length = self.set_length()
        self.omega = self.set_omega()
        self.alpha = alpha


    def __repr__(self):
        return '{0}, {1}, {2}, {3},  {4}, {5},  {6}, {7}'.format(self.name,self.mass,self.position, self.velocity,self.theta,self.length, self.omega, self.alpha)

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
            return np.arctan2(self.position[1],self.position[0]) - scipy.constants.pi/2 

    def set_length(self):
        return np.linalg.norm(self.position)

    def set_omega(self):
        if self.length == 0:
            return [0, 0, 0]
        else:
            return (np.cross(self.position, self.velocity)/(self.length**2))

    

    def update_alpha(self, deltaT):
        if self.length == 0:
            return [0,0,0]
        else:
            self.alpha = np.array([0,0,-(9.81/self.length) * np.sin(self.theta)])
            return self.alpha

    def update_omega(self, deltaT):
        self.omega += self.alpha * deltaT
        return self.omega

    def update_theta(self, deltaT):
        self.theta += self.omega[2] * deltaT
        return self.theta

    def update_richardson(self, deltaT):
        alpha_mid = np.array([0,0,(-(9.81/self.length)*np.sin(self.theta + (self.omega[2]*deltaT/2)))])
        self.omega += alpha_mid*deltaT
        self.theta += (self.omega[2] +0.5*self.alpha[2]*deltaT)*deltaT
        self.alpha = alpha_mid
        return self.theta, self.omega, self.alpha
    
    def update_angular(self, deltaT, method):
        if method == "Euler":
            self.update_alpha(deltaT)
            self.update_theta(deltaT)
            self.update_omega(deltaT)

        elif method == "Euler-Cromer":
            self.update_alpha(deltaT)
            self.update_omega(deltaT)
            self.update_theta(deltaT)

        elif method == "Euler-Richardson":
            self.update_alpha(deltaT)
            self.update_richardson(deltaT) 

        return self    

    def update_position(self):
        self.position[0] = self.length * np.cos(self.theta - scipy.constants.pi/2)
        self.position[1] = self.length * np.sin(self.theta - scipy.constants.pi/2)
        return self.position

    def update_velocity(self):
        self.velocity = np.cross(self.omega, self.position)
        return self.velocity

    def KE_angular(self):
        return 0.5 * self.mass * (self.length**2) *np.vdot(self.omega, self.omega)