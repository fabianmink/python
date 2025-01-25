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
from matplotlib.widgets import Slider
import drawPaper as dp

scaleu = 1;
scalei = 0.05;

line_width = 0.02
head_length = 0.4
head_width = head_length*0.5

u = 10;
f = 500;

R0 = 2.2;
L0 = 1e-3;
RL0 = 1.3;


L1 = 10e-3;
RL1 = 11;
R2 = 33;
R3 = 22;
R4 = 47;
C4 = 22e-6;

r2_loc = np.linspace(15,40,100)
r4_loc =  np.linspace(30,55,100)
 

#R2_abgl = L1/C4/R3;
#R4_abgl = R2_abgl * R3/RL1;
#%R2 = R2_abgl;
#%R4 = R4_abgl;

myDim = {
         'x_cm_zero' : 1, 
         'y_cm_zero': 4,
         'x_scale': 1,
         'y_scale': 1,
         'x_cm' : 13,
         'y_cm' : 11,
         'x_label' : '$\mathrm{Re}$',
         'y_label' : '$\mathrm{Im}$',
         'x_cm_tick' : 0,
         'y_cm_tick' : 0,
}


def phasors(R2, R4):
    w = 2*np.pi*f;
    
    XL0 = w*L0;
    XL1 = w*L1;
    
    XC4 = -1/(w*C4);
    
    Z0 = R0 + 1j*XL0 + RL0;
    
    Z1 = RL1 + 1j*XL1;
    Z2 = R2;
    Z3 = R3;
    Z4 = 1/( 1/R4 + 1/(1j*XC4) ); 
    
    Z12 = Z1 + Z2;
    Z34 = Z3 + Z4;
    
    ZBr = Z12*Z34/(Z12+Z34);
    
    Zges = Z0 + ZBr;
    
    i0 = u/Zges;
    
    u0 = i0*Z0;
    uBr = u - u0;
    
    i12 = uBr/Z12;
    i34 = uBr/Z34;
    
    u1 = i12*Z1;
    u2 = i12*Z2;
    
    u3 = i34*Z3;
    u4 = i34*Z4;
    
    ud = u2-u4;
    
    return (u0,u1,u2,u3,u4,uBr,ud,i0,i12,i34)
    

def clarke(a,b,c):
    alpha = 2/3*a - 1/3*b -1/3*c
    beta = 1/np.sqrt(3)*b - 1/np.sqrt(3)*c
    return alpha,beta



fig_phasor, (ax_phasor) = plt.subplots(1, 1)
ax_phasor.autoscale(False)

ax_phasor.set_xlabel(r"$\mathrm{Re}$")
ax_phasor.set_ylabel(r"$\mathrm{Im}$")

arrow_u0 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='black',fc='black')

ax_phasor.annotate(r"$1\mathrm{V}/ \mathrm{cm}$" + "\n" + "$50\mathrm{mA}/ \mathrm{cm}$", xy=(1.5, 5), xycoords='data', bbox=dict(boxstyle="round", fc="0.8"))

line_loc_ud_r2, = ax_phasor.plot(0*r2_loc, 0*r2_loc, 'k-', linewidth=0.5);
line_loc_ud_r4, = ax_phasor.plot(0*r4_loc, 0*r4_loc, 'k-' ,linewidth=0.5);

line_loc_u1_r2, = ax_phasor.plot(0*r2_loc, 0*r2_loc, 'k-', linewidth=0.5);
line_loc_u1_r4, = ax_phasor.plot(0*r4_loc, 0*r4_loc, 'k-' ,linewidth=0.5);

line_loc_u3_r2, = ax_phasor.plot(0*r2_loc, 0*r2_loc, 'k-', linewidth=0.5);
line_loc_u3_r4, = ax_phasor.plot(0*r4_loc, 0*r4_loc, 'k-' ,linewidth=0.5);

arrow_ubr = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='yellow',fc='yellow')

arrow_u1 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='green',fc='green')
arrow_u2 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='green',fc='green')
arrow_u3 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='blue',fc='blue')
arrow_u4 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='blue',fc='blue')

arrow_ud = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='red',fc='red')
arrow_ud2 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='red',fc='red')

arrow_u = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='magenta',fc='magenta')


arrow_i12 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='green',fc='green')
arrow_i34 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='blue',fc='blue')

arrow_i0 = ax_phasor.arrow(0,0,0,0,width=line_width,head_width=head_width,head_length=head_length,length_includes_head=True,ec='grey',fc='grey')

annotate_u = ax_phasor.annotate(r"$\hat{u}$", xy=(0, 0), xycoords='data', fontsize=12, color='magenta')
annotate_u0 = ax_phasor.annotate(r"$\hat{u}_0$", xy=(0, 0), xycoords='data', fontsize=12)
annotate_u1 = ax_phasor.annotate(r"$\hat{u}_\mathrm{1}$", xy=(0, 0), xycoords='data', fontsize=12, color='green')
annotate_u2 = ax_phasor.annotate(r"$\hat{u}_\mathrm{2}$", xy=(0, 0), xycoords='data', fontsize=12, color='green')
annotate_u3 = ax_phasor.annotate(r"$\hat{u}_\mathrm{3}$", xy=(0, 0), xycoords='data', fontsize=12, color='blue')
annotate_u4 = ax_phasor.annotate(r"$\hat{u}_\mathrm{4}$", xy=(0, 0), xycoords='data', fontsize=12, color='blue')
annotate_ud = ax_phasor.annotate(r"$\hat{u}_\mathrm{d}$", xy=(0, 0), xycoords='data', fontsize=12, color='red')
annotate_i0 = ax_phasor.annotate(r"$\hat{i}_0$", xy=(0, 0), xycoords='data', fontsize=12, color='grey')
annotate_i12 = ax_phasor.annotate(r"$\hat{i}_{12}$", xy=(0, 0), xycoords='data', fontsize=12, color='green')
annotate_i34 = ax_phasor.annotate(r"$\hat{i}_{34}$", xy=(0, 0), xycoords='data', fontsize=12, color='blue')


dp.drawPaper(fig_phasor, **myDim);

#todo: do all impedance / phasor calculations here
def update_phasors():
    u0,u1,u2,u3,u4,uBr,ud,i0,i12,i34 = phasors(R2, R4)
    
    arrow_u.set_data(x=0, y=0, dx=u.real/scaleu,dy=u.imag/scaleu)
    arrow_u0.set_data(x=0, y=0, dx=u0.real/scaleu,dy=u0.imag/scaleu)
    
    arrow_ubr.set_data(x=u0.real/scaleu, y=u0.imag/scaleu, dx=uBr.real/scaleu,dy=uBr.imag/scaleu)
    
    arrow_u1.set_data(x=u0.real/scaleu, y=u0.imag/scaleu, dx=u1.real/scaleu,dy=u1.imag/scaleu)
    arrow_u2.set_data(x=(u0.real+u1.real)/scaleu, y=(u0.imag+u1.imag)/scaleu, dx=u2.real/scaleu,dy=u2.imag/scaleu)
    arrow_u3.set_data(x=u0.real/scaleu, y=u0.imag/scaleu, dx=u3.real/scaleu,dy=u3.imag/scaleu)
    arrow_u4.set_data(x=(u0.real+u3.real)/scaleu, y=(u0.imag+u3.imag)/scaleu, dx=u4.real/scaleu,dy=u4.imag/scaleu)
    
    arrow_ud.set_data(x=(u0.real+u1.real)/scaleu, y=(u0.imag+u1.imag)/scaleu, dx=ud.real/scaleu,dy=ud.imag/scaleu)
    arrow_ud2.set_data(x=0, y=0, dx=ud.real/scaleu,dy=ud.imag/scaleu)
       
    arrow_i0.set_data(x=0, y=0, dx=i0.real/scalei,dy=i0.imag/scalei)
    arrow_i12.set_data(x=0, y=0, dx=i12.real/scalei,dy=i12.imag/scalei)
    arrow_i34.set_data(x=i12.real/scalei, y=i12.imag/scalei, dx=i34.real/scalei,dy=i34.imag/scalei)
    
    annotate_u.set(  x=u.real*0.9/scaleu + 0,   y=u.imag*0.9/scaleu-0.6  )
    annotate_u0.set(  x=u0.real/2/scaleu -0.4,   y=u0.imag/2/scaleu+0.2  )
    annotate_u1.set(  x=(u0.real+u1.real/2)/scaleu + 0,   y=(u0.imag+u1.imag/2)/scaleu+0.4  )
    annotate_u2.set(  x=(u0.real+u1.real+u2.real/2)/scaleu - 0.6,   y=(u0.imag+u1.imag+u2.imag/2)/scaleu-0.2  )
    annotate_u3.set(  x=(u0.real+u3.real/2)/scaleu + 0,   y=(u0.imag+u3.imag/2)/scaleu-0.6  )
    annotate_u4.set(  x=(u0.real+u3.real+u4.real/2)/scaleu + 0,   y=(u0.imag+u3.imag+u4.imag/2)/scaleu+0.2  )
    annotate_ud.set(  x=(u0.real+u1.real+ud.real/2)/scaleu + 0,   y=(u0.imag+u1.imag+ud.imag/2)/scaleu+0.2  )
    annotate_i0.set(  x=i0.real/2/scalei - 0.4,   y=i0.imag/2/scalei - 0.8  )
    annotate_i12.set(  x=i12.real/2/scalei - 0.4,   y=i12.imag/2/scalei - 0.6  )
    annotate_i34.set(  x=(i12.real+i34.real/2)/scalei -0.2,   y=(i12.imag+i34.imag/2)/scalei - 0.8  )
    
    u0_r2,u1_r2,u2_r2,u3_r2,u4_r2,uBr_r2,ud_r2,i0_r2,i12_r2,i34_r2 = phasors(r2_loc,R4)
    u0_r4,u1_r4,u2_r4,u3_r4,u4_r4,uBr_r4,ud_r4,i0_r4,i12_r4,i34_r4 = phasors(R2,r4_loc)
    
    line_loc_ud_r2.set_xdata(ud_r2.real/scaleu  );
    line_loc_ud_r2.set_ydata(ud_r2.imag/scaleu  );
    
    line_loc_ud_r4.set_xdata(ud_r4.real/scaleu  );
    line_loc_ud_r4.set_ydata(ud_r4.imag/scaleu  );
    
    line_loc_u1_r2.set_xdata((u0_r2+u1_r2).real/scaleu  );
    line_loc_u1_r2.set_ydata((u0_r2+u1_r2).imag/scaleu  );    
    
    line_loc_u1_r4.set_xdata((u0_r4+u1_r4).real/scaleu  );
    line_loc_u1_r4.set_ydata((u0_r4+u1_r4).imag/scaleu  );
    
    line_loc_u3_r2.set_xdata((u0_r2+u3_r2).real/scaleu  );
    line_loc_u3_r2.set_ydata((u0_r2+u3_r2).imag/scaleu  );    
    
    line_loc_u3_r4.set_xdata((u0_r4+u3_r4).real/scaleu  );
    line_loc_u3_r4.set_ydata((u0_r4+u3_r4).imag/scaleu  );
    
      

fig_widgets = plt.figure()

ax_f = fig_widgets.add_axes([0.075, 0.4, 0.8, 0.03])
f_slider = Slider(
    ax=ax_f,
    label=r'$f/\mathrm{Hz}$',
    valmin=100,
    valmax=1000,
    valinit=500,
)


ax_R2 = fig_widgets.add_axes([0.075, 0.2, 0.8, 0.03])
R2_slider = Slider(
    ax=ax_R2,
    label=r'$R_\mathrm{2}$',
    valmin=15,
    valmax=40,
    valinit=R2,
)


ax_R4 = fig_widgets.add_axes([0.075, 0.1, 0.8, 0.03])
R4_slider = Slider(
    ax=ax_R4,
    label=r'$R_\mathrm{4}$',
    valmin=30.0,
    valmax=55.0,
    valinit=R4,
)


       
def slider_upd(val):
    global f, R2, R4
    
    f = f_slider.val
    R2 = R2_slider.val
    R4 = R4_slider.val
    
    update_phasors()
   
    fig_phasor.canvas.draw_idle()
    

def on_close(event):
    #print('Closed Figure!')
    
    plt.close('all')
    #sys.exit()
    

fig_phasor.canvas.mpl_connect('close_event', on_close)
fig_widgets.canvas.mpl_connect('close_event', on_close)

   

# register the update functions for each widget
f_slider.on_changed(slider_upd)
R2_slider.on_changed(slider_upd)
R4_slider.on_changed(slider_upd)


#initial update
slider_upd(0)


plt.show()