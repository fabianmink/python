#   Copyright (c) 2025 Fabian Mink <fabian.mink@gmx.de>
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
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider, CheckButtons


U_DC = 500.0  #V
f_sw = 2000 #Hz switching frequency



A = 0.5 #0...1 Amplitude, relative to triangle reference maximum
f = 100 #Hz fundamental frequency


lent = 10000
t = np.linspace(-2.0e-3, 10.0e-3, lent)
tcur = 0e-3


#generates triangle signal from -1 ... 1 with frequency f
def triangle_t(t, f):
    #phase = np.divmod(t*f,1)[1]
    phase_shifted = np.divmod(t*f+0.25,1)[1]
    
    x = 4*phase_shifted - 1
    x += 2*(1-x) * (phase_shifted > 0.5)
    
    return x


def clarke(a,b,c):
    alpha = 2/3*a - 1/3*b -1/3*c
    beta = 1/np.sqrt(3)*b - 1/np.sqrt(3)*c
    return alpha,beta



sref = triangle_t(t, f_sw)



fig_t, (ax_ref, ax_uA, ax_uM) = plt.subplots(3, 1)


ax_ref.grid(1)
#ax_ref.set_xlabel("$t  /  \mathrm{ms}$")
ax_ref.set_ylabel("$s$")

ax_uA.grid(1)
#ax_uA.set_xlabel("$t  /  \mathrm{ms}$")
ax_uA.set_ylabel("$u/V$")

ax_uM.grid(1)
ax_uM.set_xlabel("$t  /  \mathrm{ms}$")
ax_uM.set_ylabel("$u/V$")

# fig_sv, (ax_sv) = plt.subplots(1, 1)
# ax_sv.grid(1)
# #redo after each update
# ax_sv.axis('equal')
# ax_sv.set(xlim=(-350, 350), ylim=(-350, 350))
# ax_sv.set_xlabel(r"$u_{\alpha}  /  \mathrm{V}$")
# ax_sv.set_ylabel(r"$u_{\beta}  /  \mathrm{V}$")
# arrow_sv = ax_sv.arrow(0,0,0,0,width=1,head_width=20,head_length=50,length_includes_head=True,ec='black',fc='black')


line_sref, = ax_ref.plot( t*1000, sref, 'k', linewidth=1)
line_sa, = ax_ref.plot( t*1000, t*0, 'r', linewidth=1)
line_sb, = ax_ref.plot( t*1000, t*0, 'g', linewidth=1)
line_sc, = ax_ref.plot( t*1000, t*0, 'b', linewidth=1)
line_s_tpos, = ax_ref.plot( 0*np.array([1, 1]) * 1000, np.array([-1, 1]), 'k-', linewidth=2)


line_uAa, = ax_uA.plot( t*1000, t*0, 'r', linewidth=1)
line_uAb, = ax_uA.plot( t*1000, t*0, 'g', linewidth=1)
line_uAc, = ax_uA.plot( t*1000, t*0, 'b', linewidth=1)
line_uA_tpos, = ax_uA.plot( 0*np.array([1, 1]) * 1000, np.array([-1, 1]) * U_DC/2, 'k-', linewidth=2)


line_uaM, = ax_uM.plot( t*1000, t*0, 'r', linewidth=1)
line_ubM, = ax_uM.plot( t*1000, t*0, 'g', linewidth=1)
line_ucM, = ax_uM.plot( t*1000, t*0, 'b', linewidth=1)
line_uM,  = ax_uM.plot( t*1000, t*0, 'k', linewidth=1)
line_uM_tpos, = ax_uM.plot( 0*np.array([1, 1]) * 1000, np.array([-1, 1]) * 2*U_DC/3, 'k-', linewidth=2)


#line_sv = ax_sv.plot( ualpha, ubeta, 'rx', linewidth=1)

def update_t():
    line_s_tpos.set_xdata(tcur*np.array([1, 1]) * 1000)
    line_uA_tpos.set_xdata(tcur*np.array([1, 1]) * 1000)
    line_uM_tpos.set_xdata(tcur*np.array([1, 1]) * 1000)
    
    #print(tcur)
    
 
#update Amplitude and freq of reference (recalc all signals)
def update_Af():
    sa = A*np.sin(2*np.pi*f*t)
    sb = A*np.sin(2*np.pi*f*t-2/3*np.pi)
    sc = A*np.sin(2*np.pi*f*t-4/3*np.pi)

    uAa = U_DC * (-0.5 + 1.0*(sa > sref) )
    uAb = U_DC * (-0.5 + 1.0*(sb > sref) )
    uAc = U_DC * (-0.5 + 1.0*(sc > sref) )

    uM = 1/3 * (uAa + uAb + uAc)
    uaM = uAa - uM
    ubM = uAb - uM
    ucM = uAc - uM

    ualpha, ubeta = clarke(uaM, ubM, ucM);
    
    line_sa.set_ydata(sa)
    line_sb.set_ydata(sb)
    line_sc.set_ydata(sc)
    

    line_uAa.set_ydata(uAa)
    line_uAb.set_ydata(uAb)
    line_uAc.set_ydata(uAc)

    line_uaM.set_ydata(uaM)
    line_ubM.set_ydata(ubM)
    line_ucM.set_ydata(ucM)
    line_uM.set_ydata(uM)    
    

  

fig_widgets = plt.figure()

ax_tpos = fig_widgets.add_axes([0.075, 0.1, 0.8, 0.03])
tpos_slider = Slider(
    ax=ax_tpos,
    label=r'$\frac{t}{t_\mathrm{max}}$',
    #label='position',
    valmin=0,
    valmax=1,
    valinit=0.125,
)


ax_f = fig_widgets.add_axes([0.075, 0.2, 0.8, 0.03])
f_slider = Slider(
    ax=ax_f,
    label=r'$f/\mathrm{Hz}$',
    #label='position',
    valmin=0,
    valmax=200,
    valinit=100,
)

ax_A = fig_widgets.add_axes([0.075, 0.3, 0.8, 0.03])
A_slider = Slider(
    ax=ax_A,
    label=r'$A_s$',
    #label='position',
    valmin=0.0,
    valmax=1.0,
    valinit=0.5,
)


def tpos_slider_upd(val):
    global tcur
    
    #get GUI values
    idx_pos = int(tpos_slider.val*(lent-1))
    tcur = t[idx_pos];
    
    
    update_t()
    fig_t.canvas.draw_idle()
        
def Af_slider_upd(val):
    global A,f
    
    f = f_slider.val
    A = A_slider.val
    
    
    update_Af()
    fig_t.canvas.draw_idle()

    

# register the update functions for each widget
tpos_slider.on_changed(tpos_slider_upd)
f_slider.on_changed(Af_slider_upd)
A_slider.on_changed(Af_slider_upd)


#initial calculation
tpos_slider_upd(0)
Af_slider_upd(0)


plt.show()