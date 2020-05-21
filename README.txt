Particle.py
- A file containing the Particle class. The class is capable of calculating the gravitational potential energy and the kinetc energy from the linear components.

Tether.py
- A file containing the Tether class. The class contains the four update methods which are used in updating the state each iteration. 
- It also contains methods for calculating the potential gravitational and kinetic energise from the angular components. 

test_Tether.py 
- A test file containing tests for each of the classes and functions. 

Simulation.py
- A file which contains the variable for the simulation. The variables of the Tether object are set in this and also the length and deltaT for the desired simulation. 
- It also handles all of the collating and exporting of the data into a panda dataframe. 

To Run the Simulation:
set:
endT to the length you would like the simulation to for in seconds. 
deltaT to the length of the desired time step in seconds. 
Numer to the number of data points you would like. 

