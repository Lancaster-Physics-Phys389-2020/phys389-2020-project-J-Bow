from Particle import Particle
import numpy as np
from unittest.mock import patch
import math
import copy
import scipy.constants

class Tether(Particle):
    """
    lengths in Km
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
        """
        Takes the input of cartesian coordinates in an array [x,y,z] and returns the polar coordiante angle theta
        """
        
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

        # The above is for the 4 cases where the initial position begins on the x or y axis

        else:
            return np.arctan2(self.position[1],self.position[0]) + scipy.constants.pi/2 

    def set_length(self):
        """
        Takes the input of cartesian coordinates in an array [x,y,z] and returns the length of the tether
        """
        return np.linalg.norm(self.position)

    def set_omega(self):
        """
        Takes the cartesian position and initial linear velocity, and returns the angular velocity
        """
        if self.length == 0: #prevents a divide by zero error
            return [0, 0, 0]
        else:
            return (np.cross(self.position, self.velocity)/(self.length**2))

    def update_alpha(self, deltaT):
        """
        Takes the angular position theta and tether length from self, and also a time step deltaT
        """
        if self.length == 0: #prevents a divide by zero error
            return [0,0,0] 
        else:
            self.alpha = np.array([0,0,(-(6.67E-23 * 5.97E24/ ((300 + 6371)- self.length*np.cos(self.theta))**2) * np.sin(self.theta) + self.Drag(self.theta, self.omega[2]))/self.length])
            return self.alpha

    def temp_alpha(self,deltaT,theta, omega):
        """
        returns a new temporary angular acceleration vector for the Runge-Kutta method. It uses the given theta and omega values instead of the values from self
        """
        return (-(6.67E-23 * 5.97E24/((300 + 6371) - self.length*np.cos(self.theta))**2) * np.sin(self.theta)  +self.Drag(theta, omega))/self.length

    def Drag(self, theta, omega):
        return 2 * 10 * (10**(-0.01026349 *(300 - (self.length*np.cos(theta)))-7.51775493  )) * (((7725*np.cos(theta)/self.length) -omega)**2) /(2*self.mass)


    def update_omega(self, deltaT):
        """
        Takes the angular acceleration vector and a time step deltaT and returns the updated angular velocity vector
        """
        self.omega += self.alpha * deltaT
        return self.omega

    def update_theta(self, deltaT):
        """
        Takes the angular velocity vector and a time step deltaT and return the scalar value of angular position
        """
        self.theta += self.omega[2] * deltaT
        return self.theta   

    def update_richardson(self, deltaT):
        """
        Method for updating the position and angular velocity using the Euler-Richardson method
        """
        omega_mid = self.omega +0.5*self.alpha*deltaT
        theta_mid = self.theta +0.5*self.omega[2]*deltaT
        alpha_mid = np.array([0,0,self.temp_alpha(deltaT, theta_mid, omega_mid)])
        self.omega = self.omega + alpha_mid * deltaT
        self.theta = self.theta + omega_mid[2] *deltaT

        return self.theta, self.omega
 

    def update_RK(self, deltaT):
        """
        Method for updating the position and angular velocity using the Runge-Kutta method
        """
        k1a, k1b, k2a, k2b, k3a, k3b, k4a, k4b = 0,0,0,0,0,0,0,0
        k1a = deltaT * self.omega[2]
        k1b = deltaT * self.temp_alpha(deltaT,self.theta,self.omega[2])
        k2a = deltaT * (self.omega[2]+(k1b/2))
        k2b = deltaT * self.temp_alpha(deltaT/2, (self.theta +(k1a/2)), (self.omega[2] + (k1b/2)))
        k3a = deltaT * (self.omega[2]+(k2b/2))
        k3b = deltaT * self.temp_alpha(deltaT/2, (self.theta +(k2a/2)), (self.omega[2] + (k2b/2)))
        k4a = deltaT * (self.omega[2] + (k3b))
        k4b = deltaT * self.temp_alpha(deltaT, (self.theta +(k3a)), (self.omega[2] + (k3b)))
        theta_new = self.theta + ((k1a + 2*k2a + 2*k3a + k4a)/6)
        omega_new =np.array([0,0, self.omega[2] + ((k1b + 2*k2b + 2*k3b + k4b)/6)])

        return theta_new, omega_new
    
    def update_angular(self, deltaT, method):
        """
        The main function which dictates which update method is used.
        """
        if method == "E": #Euler method
            self.update_alpha(deltaT)
            self.update_theta(deltaT)
            self.update_omega(deltaT)
 
        elif method == "EC": #Euler-Cromer method
            self.update_alpha(deltaT)
            self.update_omega(deltaT)
            self.update_theta(deltaT)

        elif method == "ER": #Euler-Richardson method
            self.update_alpha(deltaT)
            self.update_richardson(deltaT) 
        
        elif method == "RK": #Runge-Kutta method 
            self.theta, self.omega = self.update_RK(deltaT)
            self.alpha = self.update_alpha(deltaT)
            
        return self    

    def update_position(self):
        """
        Converts from polar position to cartesian position
        """
        self.position[0] = self.length * np.cos(self.theta - scipy.constants.pi/2)
        self.position[1] = self.length * np.sin(self.theta - scipy.constants.pi/2)
        return self.position

    def update_velocity(self):
        """
        Converts from angular velocity to linear velocity
        """
        self.velocity = np.cross(self.omega, self.position)
        return self.velocity

    def KE_angular(self):
        """
        Calculates the kinetic energy from the angular velocity
        """
        return 0.5 * self.mass * ((self.length)**2) *np.vdot(self.omega, self.omega)


    def GPE_ang(self):
        """
        find the gravitational potential energy
        """
        return  self.mass * -(6.67E-23 * 5.97E24)/((300 + 6371 - self.length*np.cos(self.theta)) )
