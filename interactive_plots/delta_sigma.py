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


#import drawPaper as dp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

Ts = 1e-3
Uref = 2.5
R = 1000
C = 1e-6

#t_ue = np.array([-0.1, 1,   1,    3,  3, 4,    4,  5, 5, 6.5])
#ue = np.array([  0, 0, 0.5,  0.5,  0, 0,   -1, -1, 0, 0])

t = np.arange(0, 0.05, Ts)
numsteps = t.size



def update(val):
    #print("hello")
    ue = ue_slider.val
    u_int = 0;
    q = True;
    
    ue_store = ue * np.ones(numsteps)
    uint_store = np.zeros(numsteps)
    udelta_store = np.zeros(numsteps)
    q_store = np.zeros(numsteps)

        
    for i_step in range(numsteps):
        uint_store[i_step] = u_int 
        q_store[i_step] = q    
        
        u_ref_out = Uref
        if(q):
            u_ref_out = -Uref
                
        u_delta = ue + u_ref_out
        udelta_store[i_step] = u_delta
        
        u_int = u_int - u_delta * Ts/(R*C)
        
        q = False
        if(u_int<0):
            q = True
    
    line_uint.set_ydata(uint_store);
    line_udelta.set_ydata(udelta_store);
    line_ue.set_ydata(ue_store);
    line_q.set_ydata(q_store);
    
    fig.canvas.draw_idle()

fig, (ax_u, ax_q) = plt.subplots(2, 1)

line_uint, = ax_u.plot(t*1000, np.zeros(numsteps), 'bx-', lw=1)
line_udelta, = ax_u.step(t*1000, np.zeros(numsteps), 'g-', lw=1, where='post')
line_ue, = ax_u.step(t*1000, np.zeros(numsteps), 'r-', lw=1, where='post')
line_urefp, = ax_u.plot(t*1000, np.ones(numsteps)*Uref, 'k--', lw=1)
line_urefn, = ax_u.plot(t*1000, np.ones(numsteps)*-Uref, 'k--', lw=1)

line_q, = ax_q.plot(t*1000, np.zeros(numsteps), 'ko', fillstyle='none', lw=1)
#line_q, = ax_q.step(t*1000, np.zeros(numsteps), 'rx-', lw=1, where='post')



    
ax_u.grid(1)
#ax_u.set_xlim(0, 2)
ax_u.set_ylim(-Uref*2.1, Uref*2.1)
ax_u.set_ylabel(r"$u  /  \mathrm{V}$")
ax_u.set_position([0.125,0.4,0.8,0.45])

ax_q.set_axisbelow(True)
ax_q.grid(1)
#ax_u.set_xlim(0, 2)
ax_q.set_ylim(-0.1, 1.1)
ax_q.set_xlabel(r"$t  /  \mathrm{ms}$")
ax_q.set_ylabel(r"$q$")
ax_q.set_position([0.125,0.18,0.8,0.15])

ax_slider_ue = fig.add_axes([0.125, 0.025, 0.75, 0.03])
ue_slider = Slider(
    ax=ax_slider_ue,
    label='ue',
    valmin=-Uref,
    valmax=Uref,
    valinit=0,
    #valstep=1,
)


# register the update functions for each widget
ue_slider.on_changed(update)

#initial calculation
update(0)

plt.show()


