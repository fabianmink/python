# -*- coding: utf-8 -*-
"""
Simulation of a pendulum

@author: Fabian Mink
"""

import math
import numpy as np
from scipy.integrate import solve_ivp
import rk4
import euler

import matplotlib.pyplot as plt

#Simulation step size
sim_Ts = 0.01
#Simulation stop time
sim_Tend = 10

#Parameters
l = 1      #m
m = 0.5    #kg
d = 0.2    #N/(m/s)
g = 9.81   #m/(s^2)

#initial conditions (IC)
theta_0_deg = 150  #deg
omega_0 = 0        #rad/s

#type of plot
plottype = 0 #0 = theta / omega, 1 = x,y / v_x, v_y

#deg -> rad conversion for IC
theta_0 = theta_0_deg * math.pi/180   

#Pendulum ODEs
def pendulum(t, statevars):
   
    theta, omega = statevars
    
    dtheta_dt = omega
    domega_dt = -g/l*np.sin(theta) -d/m*omega
    
    der_statevars = [dtheta_dt, domega_dt]

    return der_statevars  



#Pendulum linearized ODEs
def pendulum_lin(t, statevars):
   
    theta, omega = statevars
    
    dtheta_dt = omega
    domega_dt = -g/l*theta -d/m*omega
    
    der_statevars = [dtheta_dt, domega_dt]

    return der_statevars  
    



#RK4 solver with fixed step size
sol_rk4 = solve_ivp(pendulum, [0,sim_Tend], [theta_0, omega_0], method=rk4.rk4Solver, stepsize=sim_Ts)
sol_euler = solve_ivp(pendulum, [0,sim_Tend], [theta_0, omega_0], method=euler.eulerSolver, stepsize=sim_Ts)

time = sol_rk4.t
theta = sol_rk4.y[0]  #rad
omega = sol_rk4.y[1]  #rad/s
x = l*np.sin(theta)
y = -l*np.cos(theta)
vx = l*np.sin(omega)
vy = -l*np.cos(omega)

theta_euler = sol_euler.y[0]  #rad
omega_euler = sol_euler.y[1]  #rad/s

#Plotting
fig, (ax_x, ax_v) = plt.subplots(2, 1)

if plottype == 0:
    ax_x.plot(time, theta*180/math.pi, 'b-')
    ax_x.plot(time, theta_euler*180/math.pi, 'r-')
    ax_v.plot(time, omega, 'b-')
    ax_v.plot(time, omega_euler, 'r-')
    ax_x.set_ylabel(r"$\theta  /  \mathrm{\degree}$")
    ax_v.set_ylabel(r"$\omega  /  \mathrm{(rad/s)}$")
    ax_v.set_xlabel(r"$t  /  \mathrm{s}$")


if plottype == 1:
    ax_x.plot(time, x, 'b-')
    ax_x.plot(time, y, 'r-')
    ax_v.plot(time, vx, 'b-')
    ax_v.plot(time, vy, 'r-')
    ax_x.set_ylabel(r"$s / \mathrm{m}$")
    ax_v.set_ylabel(r"$v / \mathrm{(m/s)}$")
    ax_v.set_xlabel(r"$t  /  \mathrm{s}$")


ax_x.grid(1)
ax_v.grid(1)


plt.show()

