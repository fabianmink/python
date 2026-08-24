#   Copyright (c) 2026 Fabian Mink <fabian.mink@gmx.de>
#
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this
#      list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#   ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#
#   Steady-State torque-speed characteristics of DC Machine 
#   including field weakeing (fw) operation
#
import drawPaper as dp
import matplotlib.pyplot as plt
import math
import numpy as np


# Motor 1
Ra = 38      #Ohm
La = 40e-3   #H
kPhi = 0.05  #Vs

Ua = 20
nMax = 10000/60 #s^-1
Iamax = 200e-3  #A

kPhi_fw = np.linspace(kPhi*0.4,kPhi,6)
Ua_vals = np.linspace(-Ua,Ua,9)


myDim = {
         'x_scale': 2.5,
         'y_scale': 2000,
         'x_cm_zero': 5,
         'y_cm_zero': 6.5,
         'x_cm' : 11.5,
         'x_cm_tick' : 2,
         'y_cm_tick' : 1,
         'x_cm_max' : 9.5,
         'y_cm' : 13.5,
         'y_label' : r'$n / \mathrm{min^{-1}}$',
         'x_label' : r'$M / \mathrm{mNm}$',
}
M_scale = 1000

# Motor 2
# Ra = 1.2    #Ohm
# La = 2e-3   #H
# kPhi = 1.4  #Vs

# Ua = 500
# nMax = 4000/60 #s^-1
# Iamax = 20      #A

# kPhi_fw = []
# Ua_vals = np.linspace(-Ua,Ua,9)


# myDim = {
#          'x_scale': 10,
#          'y_scale': 1000,
#          'x_cm_zero': 5,
#          'y_cm_zero': 6.5,
#          'x_cm' : 11.5,
#          'x_cm_tick' : 2,
#          'y_cm_tick' : 1,
#          'x_cm_max' : 9.5,
#          'y_cm' : 13.5,
#          'y_label' : r'$n / \mathrm{min^{-1}}$',
#          'x_label' : r'$M / \mathrm{Nm}$',
# }
# M_scale = 1


def ss_DCM_n(Ua, Me):
    n = Ua/(2*math.pi*kPhi) - Ra/(2*math.pi*(kPhi**2))*Me
    return n

def ss_DCM_n_Ia(Ua, Ia, kPhi):
    n = Ua/(2*math.pi*kPhi) - Ra/(2*math.pi*kPhi) * Ia
    return n

def ss_DCM_n_maxM(Ua, Iamax, Me):
    n = 1/Me * 1/(2*math.pi) * Iamax * (Ua - Ra*Iamax)
    return n

def ss_DCM_maxM_n(Ua, Iamax, n):
    Me = 1/n * 1/(2*math.pi) * Iamax * (Ua - Ra*Iamax)
    return Me


Ia_ss = np.linspace(-Iamax,Iamax,1000)
Me_ss = Ia_ss * kPhi

#Steady-state torque-speed without field weakening
for Ua_nofw in Ua_vals:
    n_ss_mot = ss_DCM_n(Ua_nofw, Me_ss)
    plt.plot(Me_ss*M_scale, n_ss_mot*60, 'k-', lw=1)
    
    #no-load speed
    #n0 = ss_DCM_n_Ia(Ua_nofw, 0, kPhi)
    #plt.plot([0], [n0*60], 'gx')


#Speed for maximum torque, non-fw
n_Iamax_mot = ss_DCM_n_Ia(Ua, Iamax, kPhi)
n_Iamax_gen = ss_DCM_n_Ia(Ua, -Iamax, kPhi)
Me_Iamax = kPhi * Iamax

#Speed for maximum torque, in fw operation
n_ss_maxM_mot = ss_DCM_n_maxM(Ua, Iamax, Me_ss)
n_ss_maxM_mot[(n_ss_maxM_mot > nMax)] = np.nan
n_ss_maxM_mot[(n_ss_maxM_mot < -nMax)] = np.nan

n_ss_maxM_gen = ss_DCM_n_maxM(Ua, -Iamax, Me_ss)
n_ss_maxM_gen[(n_ss_maxM_gen > nMax)] = np.nan
n_ss_maxM_gen[(n_ss_maxM_gen < -nMax)] = np.nan

plt.plot(Me_ss*M_scale, n_ss_maxM_mot*60, 'r-', lw=1)
plt.plot(Me_ss*M_scale, n_ss_maxM_gen*60, 'r-', lw=1)

Me_nmax_mot = ss_DCM_maxM_n(Ua, Iamax, nMax)
Me_nmax_gen = ss_DCM_maxM_n(Ua, -Iamax, nMax)

plt.plot([Me_Iamax*M_scale, Me_Iamax*M_scale], [n_Iamax_mot*60, -n_Iamax_gen*60], 'r-')
plt.plot([-Me_Iamax*M_scale, -Me_Iamax*M_scale], [-n_Iamax_mot*60, n_Iamax_gen*60], 'r-')

plt.plot([Me_nmax_mot*M_scale, Me_nmax_gen*M_scale], [nMax*60, nMax*60], 'r-')
plt.plot([-Me_nmax_mot*M_scale, -Me_nmax_gen*M_scale], [-nMax*60, -nMax*60], 'r-')

#Steady-state torque-speed in field weakening
for kPhi in kPhi_fw :
    Ia_ss_fw = np.linspace(-Iamax,Iamax,1000)
    Me_ss_fw = Ia_ss_fw * kPhi
    n_ss_fw_mot = ss_DCM_n_Ia(Ua, Ia_ss_fw, kPhi)
    n_ss_fw_mot[(n_ss_fw_mot > nMax)] = np.nan
    
    n_ss_fw_gen = ss_DCM_n_Ia(-Ua, Ia_ss_fw, kPhi)
    n_ss_fw_gen[(n_ss_fw_gen < -nMax)] = np.nan
    
    plt.plot(Me_ss_fw*M_scale, n_ss_fw_mot*60, 'k-', lw=1)
    plt.plot(Me_ss_fw*M_scale, n_ss_fw_gen*60, 'k-', lw=1)


fig = plt.gcf()
dp.drawPaper(fig, **myDim);
plt.savefig("torque_speed_fw.png", dpi=300)