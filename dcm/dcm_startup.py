import math
import numpy as np
from scipy import signal
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
#import drawPaper as dp      #graph paper background

J = 2e-6     #kgm^2
Ra = 38      #Ohm
La = 40e-3   #H
kPhi = 0.05  #Vs

b_v = 0      #Nm/(rad/s)
#b_v = 0.00001  #Nm/ (rad/s)  #optional viscous friction

Ua = 20
Ml_step = 10e-3
t_Ml_step = 0.2

#add IVP / simulation parameters
T_max = 0.4
Ts = 0.1e-3 
w0 = 0
ia0 = 0


Asys = np.array([[-Ra/La, -kPhi/La], [kPhi/J, 0/J]])
bsys = np.array([[1/La, 0],  [0, 1/J]])
csys = np.array([[0, 1]])
#dsys = np.array([[0]])

sys = signal.StateSpace(Asys, bsys, csys)
eigv = np.linalg.eigvals(Asys)
print(eigv)


def ss_DCM(Ua, Me):
    n = Ua/(2*math.pi*kPhi) - Ra/(2*math.pi*(kPhi**2))*Me
    return n

def ode_DCM(t, statevars):
    w = statevars[0]
    ia = statevars[1]
    
    Ui = kPhi * w
    Me = kPhi * ia
    Ml = 0
    
    if(t > t_Ml_step):
        Ml = Ml_step
    #calculation of derivatives    
    dia_dt = 1/La * (Ua - Ra*ia - Ui)  
    dw_dt = 1/J * (Me - b_v*w - Ml)  
    
    
    der_statevars = [dw_dt, dia_dt]

    return der_statevars 

#Simplified; for La = 0
def ode_DCM_simplified(t, statevars):
    w = statevars[0]
    
    Ui = kPhi * w
    ia = (Ua - Ui)/Ra
    Me = kPhi * ia
    Ml = 0
    
    if(t > t_Ml_step):
        Ml = Ml_step
        
    #calculation of derivatives    
    dw_dt = 1/J * (Me - b_v*w - Ml)  
    
    der_statevars = [dw_dt]

    return der_statevars

#Simplified; for La = 0, without calculation of intermediate results
def ode_DCM_simplified2(t, statevars):
    w = statevars[0]
    
    Ml = 0
    
    if(t > t_Ml_step):
        Ml = Ml_step
        
    #calculation of derivatives    
    dw_dt = -1/J*kPhi**2/Ra * w  +  1/J*kPhi/Ra * Ua  -  1/J * Ml
    
    der_statevars = [dw_dt]

    return der_statevars



sol = solve_ivp(ode_DCM, [0,T_max], [w0,ia0], method='RK45', max_step=Ts)
w = sol.y[0]
ia = sol.y[1]
Me = sol.y[1] * kPhi
t = sol.t

sol_simplified = solve_ivp(ode_DCM_simplified2, [0,T_max], [w0], method='RK45', max_step=Ts)
w_simplified = sol_simplified.y[0]
ia_simplified = (Ua - w_simplified*kPhi)/Ra
Me_simplified = ia_simplified * kPhi
t_simplified = sol_simplified.t

fig, (ax_n, ax_i, ax_M) = plt.subplots(3, 1)

ax_n.plot(t, w/2/math.pi*60, 'b-')
ax_n.plot(t_simplified, w_simplified/2/math.pi*60, 'k--')
ax_n.grid(1)
ax_n.set_ylabel(r"$n/ \mathrm{min^{-1}}$")

ax_i.plot(t, ia, 'b-')
ax_i.plot(t_simplified, ia_simplified, 'k--')
ax_i.grid(1)
ax_i.set_ylabel(r"$i_\mathrm{A}/ \mathrm{A}$")

ax_M.plot(t, Me*1000, 'b-')
ax_M.plot(t_simplified, Me_simplified*1000, 'k--')
ax_M.grid(1)
ax_M.set_ylabel(r"$M_\mathrm{e}/ \mathrm{mNm}$")


ax_M.set_xlabel(r"$t/ \mathrm{s}$")


plt.savefig("dcm_dynamic.png", dpi=300)


plt.figure()
plt.plot(Me*1000, w/2/math.pi*60, 'b-')
plt.plot([0, Ua/Ra*kPhi*1000, 0, 10], [0, 0, ss_DCM(Ua, 0)*60, ss_DCM(Ua, Ml_step)*60], 'rx')

Me_ss = np.linspace(-5e-3,28e-3,1000)
n_ss = ss_DCM(Ua, Me_ss)
plt.plot(Me_ss*1000, n_ss*60, 'k--', lw=1)


ax = plt.gca()
ax.set_xlabel(r"$M_\mathrm{e}/ \mathrm{mNm}$")
ax.set_ylabel(r"$n/ \mathrm{min^{-1}}$")
ax.grid(1)

myDim = {
         'x_scale': 5,
         'y_scale': 1000,
         'x_cm_zero': 2,
         'y_cm_zero': 2,
         'x_cm' : 10,
         'x_cm_tick' : 2,
         'y_cm_tick' : 1,
         'x_cm_max' : 8,
         'y_cm' : 8.5,
         'y_label' : r'$n / \mathrm{min^{-1}}$',
         'x_label' : r'$M / \mathrm{mNm}$',
}

#fig = plt.gcf()
#dp.drawPaper(fig, **myDim);   #graph paper background

plt.savefig("dcm_dynamic_n_M.png", dpi=300)
