# -*- coding: utf-8 -*-
"""
Calculate operating point of cicuit with voltage source, resistor and diode

@author: Fabian Mink
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

#Voltage source and Resistor
Us = 2   #V
R = 200  #Ohm

#1N4148 parameters
Isat = 2.52e-9 #A
UT = 0.025 #V thermal voltage
n = 1.94 #emission coefficient

#solver settings
Utol = 1e-4 #V, tolerance for voltage calculation (1e-4V = 0.1mV)

#current of voltage source with series Resistor
def vs_i(vs_u):
    vs_i = (Us - vs_u)/R
    return(vs_i)

#Diode current according to Shockley diode equation
def diode_Id(Ud):  
    Id = Isat*(np.exp(Ud/(UT*n)) - 1) 
    return(Id)

#difference of currents (source+resistor vs Diode) for certain voltage
def fdelta_i(u):  
    if(record_steps): #record step, if enabled
        stepsU.append(u)
    
    f = diode_Id(u) - vs_i(u) 
    
    return(f)


#Calculate solution (find fdelta_i == 0)
stepsU = []
record_steps = True
solU = optimize.bisect(fdelta_i, 0, 2, xtol=Utol)
record_steps = False
stepsU = np.array(stepsU)

#Plot results (U-I)
plt.figure()
ax = plt.gca()
testU = np.arange(-1, 2.5, 0.01)
   
ax.plot(testU, vs_i(testU)*1000, 'b-')
ax.plot(testU, diode_Id(testU)*1000, 'g-')
plt.plot(stepsU, vs_i(stepsU)*1000, 'rx',ms=4)
plt.plot(solU, vs_i(solU)*1000, 'ro')

ax.set_ylabel(r"$I / \mathrm{mA}$")
ax.set_xlabel(r"$U /  \mathrm{V}$")
ax.set_ylim([-2,14])
ax.set_xlim([-0.5,2.5])
ax.grid(1)

#Plot steps of solution
plt.figure()
ax = plt.gca()
ax.plot(stepsU,'kx-')
ax.set_ylabel(r"$U /  \mathrm{V}$")
ax.set_xlabel("Step")
ax.grid(1)

#Display figures
plt.show()


