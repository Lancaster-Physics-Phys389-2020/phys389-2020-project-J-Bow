from Particle import Particle
import numpy as np
import math
import scipy.constants

class Tether(Particle):
    """
    """

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), name='Ball', mass=1.0, Theta=1.0, Length = 1., omega=1.0, alpha=1.0 ):
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, name=name, mass=mass)
        if self.position[1] == 0 :
            self.theta = 0
        else:
            self.theta = np.arctan(self.position[0]/self.position[1])
        self.length = np.linalg.norm(self.position)
        self.omega = np.linalg.norm(np.cross(self.position, self.velocity)/(self.length**2))
        self.alpha = alpha


    def __repr__(self):
        return '{0}, {1}, {2}, {3},  {4}, {5},  {6}, {7}, {8}'.format(self.name,self.mass,self.position, self.velocity,self.acceleration,self.theta,self.length, self.omega, self.alpha)

    g=9.81


    def update_angular(self, deltaT):
        self.alpha = -(9.81/self.length) * math.sin(self.theta)
        
        self.omega += self.alpha * deltaT
        
        if self.theta <= 2*scipy.constants.pi:
            self.theta += self.omega * deltaT
        else:
            self.theta =self.theta - 2*scipy.constants.pi
            self.theta += self.omega * deltaT 

        self.position[0] = (self.length**2 - math.sin(self.theta)**2)**0.5
        
        self.position[1] = (self.length**2 - math.cos(self.theta)**2)**0.5
        #print("Position=", self.position)
        #print("Theta=", self.theta)
        #self.acceleration = np.cross(np.array([0,0,self.alpha]), (self.length * (self.position/(np.linalg.norm(self.position))))) + np.cross(np.array([0,0,self.omega]), np.cross(np.array([0,0,self.omega]), (self.length * (self.position/(np.linalg.norm(self.position))))))
    