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
from matplotlib.widgets import Slider, CheckButtons
#import sys


U_DC = 500.0  #V
f_sw = 1000 #Hz switching frequency



A = 0.5 #0...1 Amplitude, relative to triangle reference maximum
f = 100 #Hz fundamental frequency


lent = 10000
t = np.linspace(-1.0e-3, 11.0e-3, lent)
idx_tpos = 0
tpos = t[idx_tpos]

ualpha = 0*t
ubeta = 0*t
#ualpha_mavg = 0*t
#ubeta_mavg = 0*t


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
ax_ref.set(xlim=(t[0]*1000, t[-1]*1000))
#ax_ref.get_xaxis().set_visible(False)
ax_ref.set_xticklabels([])

ax_uA.grid(1)
#ax_uA.set_xlabel("$t  /  \mathrm{ms}$")
ax_uA.set_ylabel("$u/V$")
ax_uA.set(xlim=(t[0]*1000, t[-1]*1000))
#ax_uA.get_xaxis().set_visible(False)
ax_uA.set_xticklabels([])

ax_uM.grid(1)
ax_uM.set_xlabel(r"$t  /  \mathrm{ms}$")
ax_uM.set_ylabel(r"$u/V$")
ax_uM.set(xlim=(t[0]*1000, t[-1]*1000))

fig_sv, (ax_sv) = plt.subplots(1, 1)
ax_sv.grid(1)
#redo after each update
ax_sv.axis('equal')

ax_sv.set_xlabel(r"$u_{\alpha}  /  \mathrm{V}$")
ax_sv.set_ylabel(r"$u_{\beta}  /  \mathrm{V}$")
line_sv, = ax_sv.plot( ualpha, ubeta, 'kx--', linewidth=0.5)
#line_sv_mavg, = ax_sv.plot( 0, 0, 'b-', linewidth=1)
arrow_sv = ax_sv.arrow(0,0,0,0,width=5,head_width=20,head_length=50,length_includes_head=True,ec='black',fc='black')
arrow_sv_zero, = ax_sv.plot( 0, 0, 'ko', linewidth=2, markersize=10)

arrow_sva = ax_sv.arrow(-U_DC,0,U_DC*2,0,width=1,head_width=20,head_length=50,length_includes_head=True,ec='red',fc='red')
arrow_svb = ax_sv.arrow(U_DC/2,-U_DC*0.866,-U_DC/2*2,U_DC*0.866*2,width=1,head_width=20,head_length=50,length_includes_head=True,ec='green',fc='green')
arrow_svc = ax_sv.arrow(U_DC/2,U_DC*0.866,-U_DC/2*2,-U_DC*0.866*2,width=1,head_width=20,head_length=50,length_includes_head=True,ec='blue',fc='blue')



line_sref, = ax_ref.plot( t*1000, sref, 'k', linewidth=1, label=r'$s_\mathrm{ref}$')
line_sa, = ax_ref.plot( t*1000, t*0, 'r', linewidth=1, label=r'$s_\mathrm{a}$')
line_sb, = ax_ref.plot( t*1000, t*0, 'g', linewidth=1, label=r'$s_\mathrm{b}$')
line_sc, = ax_ref.plot( t*1000, t*0, 'b', linewidth=1, label=r'$s_\mathrm{c}$')
line_s_tpos, = ax_ref.plot( 0*np.array([1, 1]) * 1000, np.array([-1, 1]), 'k-', linewidth=2)


line_uAa, = ax_uA.plot( t*1000, t*0, 'r', linewidth=1, label=r'$u_\mathrm{Aa}$')
line_uAb, = ax_uA.plot( t*1000, t*0, 'g', linewidth=1, label=r'$u_\mathrm{Ab}$')
line_uAc, = ax_uA.plot( t*1000, t*0, 'b', linewidth=1, label=r'$u_\mathrm{Ac}$')
line_uA_tpos, = ax_uA.plot( 0*np.array([1, 1]) * 1000, np.array([-1, 1]) * U_DC/2, 'k-', linewidth=2)


line_uaM, = ax_uM.plot( t*1000, t*0, 'r', linewidth=1, label=r'$u_\mathrm{aM}$')
line_ubM, = ax_uM.plot( t*1000, t*0, 'g', linewidth=1, label=r'$u_\mathrm{bM}$')
line_ucM, = ax_uM.plot( t*1000, t*0, 'b', linewidth=1, label=r'$u_\mathrm{cM}$')
line_uM,  = ax_uM.plot( t*1000, t*0, 'k', linewidth=1, label=r'$u_\mathrm{M0}$')
line_uM_tpos, = ax_uM.plot( 0*np.array([1, 1]) * 1000, np.array([-1, 1]) * 2*U_DC/3, 'k-', linewidth=2)

ax_ref.legend(loc='upper right') 
ax_uA.legend(loc='upper right')
ax_uM.legend(loc='upper right')

def update_t():
    line_s_tpos.set_xdata(tpos*np.array([1, 1]) * 1000)
    line_uA_tpos.set_xdata(tpos*np.array([1, 1]) * 1000)
    line_uM_tpos.set_xdata(tpos*np.array([1, 1]) * 1000)
    
    ualpha_tpos = ualpha[idx_tpos]
    ubeta_tpos = ubeta[idx_tpos]
    
    #ualpha_mavg_tpos = (ualpha_mavg[:idx_tpos])[-1000:] #get last elements before tpos
    #ubeta_mavg_tpos = (ubeta_mavg[:idx_tpos])[-1000:] #get last elements before tpos
        
    arrow_sv.set_data(dx=ualpha_tpos,dy=ubeta_tpos)
    
    if  (  (np.square(ualpha_tpos) + np.square(ubeta_tpos)) <  0.1 ):
        arrow_sv_zero.set_visible(True)
    else:
        arrow_sv_zero.set_visible(False)
        
    ax_sv.axis('equal')
    ax_sv.set(xlim=(-U_DC, U_DC), ylim=(-U_DC, U_DC))
    
    #line_sv_mavg.set_data(ualpha_mavg_tpos,ubeta_mavg_tpos)
    
    #print(tcur)
    
 
#update Amplitude and freq of reference (recalc all signals)
def update_Af():
    global ualpha, ubeta
    global ualpha_mavg, ubeta_mavg
    
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
    
    ualpha_mavg = np.convolve(ualpha, np.ones(1000)/1000, mode='valid')
    ubeta_mavg = np.convolve(ubeta, np.ones(1000)/1000, mode='valid')
    
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
    
    line_sv.set_data(ualpha, ubeta)
    
  

  

fig_widgets = plt.figure()

ax_tpos = fig_widgets.add_axes([0.075, 0.1, 0.8, 0.03])
tpos_slider = Slider(
    ax=ax_tpos,
    label=r'$\frac{t}{t_\mathrm{max}}$',
    #label='position',
    valmin=0,
    valmax=1,
    valinit=0.0,
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

ax_check = fig_widgets.add_axes([0.075, 0.5, 0.2, 0.4])
para_check = CheckButtons(
    ax=ax_check,
    labels=['uAa', 'uAb', 'uAc', 'uM0', 'uaM', 'ubM', 'ucM'],
    actives=[True, False, False, False, True, False, False],
    #labels=['all harmonics', 'test'],
    #actives=[False, True],
    #label_props={'color': 'black'},
    #frame_props={'edgecolor': 'black'},
    #check_props={'facecolor': 'red'},
)


def tpos_slider_upd(val):
    global idx_tpos, tpos
    
    #get GUI values
    idx_tpos = int(tpos_slider.val*(lent-1))
    tpos = t[idx_tpos];
    
    
    update_t()
    fig_t.canvas.draw_idle()
    fig_sv.canvas.draw_idle()
        
def Af_slider_upd(val):
    global A,f
    
    f = f_slider.val
    A = A_slider.val
    
    
    update_Af()
    fig_t.canvas.draw_idle()
    fig_sv.canvas.draw_idle()
    
def visibility_upd(val):
    show_uAa = para_check.get_status()[0]
    show_uAb = para_check.get_status()[1]
    show_uAc = para_check.get_status()[2]
    
    show_uM0 = para_check.get_status()[3]
    
    show_uaM = para_check.get_status()[4]
    show_ubM = para_check.get_status()[5]
    show_ucM = para_check.get_status()[6]

    line_uAa.set_visible(show_uAa)
    line_uAb.set_visible(show_uAb)
    line_uAc.set_visible(show_uAc)
    
    line_uM.set_visible(show_uM0)
    
    line_uaM.set_visible(show_uaM)
    line_ubM.set_visible(show_ubM)
    line_ucM.set_visible(show_ucM)
    
    fig_t.canvas.draw_idle()
       

def on_close(event):
    #print('Closed Figure!')
    
    plt.close('all')
    #sys.exit()
    

fig_t.canvas.mpl_connect('close_event', on_close)
fig_sv.canvas.mpl_connect('close_event', on_close)
fig_widgets.canvas.mpl_connect('close_event', on_close)

   

# register the update functions for each widget
tpos_slider.on_changed(tpos_slider_upd)
f_slider.on_changed(Af_slider_upd)
A_slider.on_changed(Af_slider_upd)
para_check.on_clicked(visibility_upd)


#initial update
tpos_slider_upd(0)
Af_slider_upd(0)
visibility_upd(0)


plt.show()