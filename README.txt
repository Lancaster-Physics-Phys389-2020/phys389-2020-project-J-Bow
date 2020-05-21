Particle.py
- A file containing the Particle class. The class is capable of calculating the gravitational potential energy and the kinetc energy from the linear components.

Tether.py
- A file containing the Tether class. The class contains the four update methods which are used in updating the state each iteration. 
- It also contains methods for calculating the potential gravitational and kinetic energise from the angular components. 

test_Tether.py 
- A test file containing tests for each of the classes and functions. 

Density.py
- a file which creates a useable equation for the air density with respect to height for the desired range. The data is from NASA's MSISE-90. 
- the data can be found at https://ccmc.gsfc.nasa.gov/modelweb/models/msis_vitmo.php

Simulation.py
- A file which contains the variable for the simulation. The variables of the Tether object are set in this and also the length and deltaT for the desired simulation. 
- It also handles all of the collating and exporting of the data into a panda dataframe. 


To Run the Simulation:
set:
endT to the length you would like the simulation to run for in seconds. 
deltaT to the length of the desired time step in seconds. 
Numer to the number of data points you would like. 
initial_position to [x, y, 0.]. The vector of linear position in km. 
initial_velocity to [x, y, 0.]. The vector of linear velocity in km. 
mass to the mass of the head.
method to the desired method for the simulation, of the options: E = Euler, EC = Euler-Cromer, ER = Euler-Richard, RK = Runge-Kutta
dataName to the name you would like the file to be saved as. it must end in .csv.
C_d to the coefficient of drag for the head.
A to the surface area of the head in km^2.
h to the altitude of the anchors orbit in km.
v to the orbital velocity of the anchor in kms^-1. 

Then run the Simulation.py file and a .csv file of the desired name will be created in the folder.

