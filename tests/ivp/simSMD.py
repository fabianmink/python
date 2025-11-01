# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 07:13:39 2025

@author: Fabian Mink
"""

#Simulation of a Spring-Mass-Damper System

#import numpy as np
from scipy.integrate import solve_ivp
import rk4

import matplotlib.pyplot as plt

#Simulation step size
RK4_Ts = 0.1

RK45_Ts_first = 0.1
RK45_Ts_max = 0.1

#Spring-Mass-Damper System implementation
def smd(t, z):
    b = 1
    k=20
    m=1
    
    x, v = z
    
    dx_dt = v
    dv_dt = 1/m * -k*x -b*v

    return [dx_dt, dv_dt]  
    


#Own RK4 solver with fixed step size
sol_ownRK4 = solve_ivp(smd, [0,10], [0.01, 0], method=rk4.rk4Solver, stepsize=RK4_Ts)

#RK4 with fixed step size by setting tolerances to inf and first_step / max_step to desired value
sol_builtin_RK45 = solve_ivp(smd, [0,10], [0.01, 0], method='RK45', first_step=RK45_Ts_first, max_step=RK45_Ts_max, rtol=float('inf'), atol=float('inf'))


#t = sol.t     #time
#x = sol.y[0]  #position
#v = sol.y[1]  #velocity

plt.plot(sol_builtin_RK45.t, sol_builtin_RK45.y[0], 'kx-')
plt.plot(sol_ownRK4.t, sol_ownRK4.y[0], 'rx-')

print(sol_ownRK4.t)
print(sol_ownRK4.y[0])

print(sol_builtin_RK45.t)
print(sol_builtin_RK45.y[0])

