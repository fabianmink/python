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

A = 325
f = 50 #frequency

lent = 1000

t = np.linspace(0.00, 40.0e-3, lent)
tcur = 5e-3


def clarke(a,b,c):
    alpha = 2/3*a - 1/3*b -1/3*c
    beta = 1/np.sqrt(3)*b - 1/np.sqrt(3)*c
    return alpha,beta


fig, (ax_t, ax_sv) = plt.subplots(1, 2)

ax_t.set_position([0.13,0.3,0.38,0.6])
ax_sv.set_position([0.65,0.3,0.3,0.6])

ax_t.grid(1)
ax_t.set(xlim=(0, 40), ylim=(-350, 350))
ax_t.set_xlabel("$t  /  \mathrm{ms}$")
ax_t.set_ylabel("$u  /  \mathrm{V}$")

ax_sv.grid(1)
#redu after each update
ax_sv.axis('equal')
ax_sv.set(xlim=(-350, 350), ylim=(-350, 350))
ax_sv.set_xlabel(r"$u_{\alpha}  /  \mathrm{V}$")
ax_sv.set_ylabel(r"$u_{\beta}  /  \mathrm{V}$")


ua = A*np.sin(2*np.pi*f*t);
ub = A*np.sin(2*np.pi*f*t-2*np.pi/3);
uc = A*np.sin(2*np.pi*f*t-4*np.pi/3);

ualpha, ubeta = clarke(ua, ub, uc);

line_a, = ax_t.plot(t* 1000, ua, 'r-', linewidth=1, label='$u_\mathrm{a}$');
line_b, = ax_t.plot(t* 1000, ub, 'g-', linewidth=1, label='$u_\mathrm{b}$');
line_c, = ax_t.plot(t* 1000, uc, 'b-', linewidth=1, label='$u_\mathrm{c}$');

line_pos_t, = ax_t.plot( tcur*np.array([1, 1]) * 1000, np.array([-400, 400]), 'k-', linewidth=1)

ax_t.legend(loc='upper left')  

line_sv, = ax_sv.plot( ualpha, ubeta, 'k--', linewidth=1)

arrow_sva = ax_sv.arrow(-350,0,350*2,0,width=1,head_width=20,head_length=50,length_includes_head=True,ec='red',fc='red')
arrow_svb = ax_sv.arrow(350/2,-350*0.866,-350/2*2,350*0.866*2,width=1,head_width=20,head_length=50,length_includes_head=True,ec='green',fc='green')
arrow_svc = ax_sv.arrow(350/2,350*0.866,-350/2*2,-350*0.866*2,width=1,head_width=20,head_length=50,length_includes_head=True,ec='blue',fc='blue')

line_sva, = ax_sv.plot( np.array([0, 0]), np.array([0, 0]), 'r--', linewidth=1)
line_svb, = ax_sv.plot( np.array([0, 0]), np.array([0, 0]), 'g--', linewidth=1)
line_svc, = ax_sv.plot( np.array([0, 0]), np.array([0, 0]), 'b--', linewidth=1)

arrow_sv = ax_sv.arrow(0,0,0,0,width=1,head_width=20,head_length=50,length_includes_head=True,ec='black',fc='black')


axshift = fig.add_axes([0.075, 0.125, 0.8, 0.03])
shift_slider = Slider(
    ax=axshift,
    label=r'$\frac{t}{2 T}$',
    #label='position',
    valmin=0,
    valmax=1,
    valinit=0.125,
)



# The function to be called anytime a slider's value changes
def update(val):
    #get GUI values
    #alpha_shift = 2*np.pi*shift_slider.val/360
    idx_pos = int(shift_slider.val*(lent-1))
    tcur = t[idx_pos];
        
    ualpha_cur = ualpha[idx_pos]
    ubeta_cur = ubeta[idx_pos]
    
    ua_cur = ua[idx_pos]
    ub_cur = ub[idx_pos]
    uc_cur = uc[idx_pos]
    
    arrow_sv.set_data(dx=ualpha_cur,dy=ubeta_cur)
    line_pos_t.set_xdata(tcur*np.array([1, 1])*1000)
    
    line_sva.set_xdata(np.array([ualpha_cur, ua_cur]))
    line_sva.set_ydata(np.array([ubeta_cur, 0]))
    
    line_svb.set_xdata(np.array([ualpha_cur, ub_cur*-0.5]))
    line_svb.set_ydata(np.array([ubeta_cur, ub_cur*0.866]))
    
    line_svc.set_xdata(np.array([ualpha_cur, uc_cur*-0.5]))
    line_svc.set_ydata(np.array([ubeta_cur, uc_cur*-0.866]))
    #( np.array([0, 0]), np.array([0, 0]), 'r--', linewidth=1)
    
    ax_sv.axis('equal')
    ax_sv.set(xlim=(-350, 350), ylim=(-350, 350))
      
    
   


# register the update functions for each widget
shift_slider.on_changed(update)


#initial calculation
update(0)

plt.show()