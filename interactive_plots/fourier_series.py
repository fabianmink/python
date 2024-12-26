#   Copyright (c) 2024 Fabian Mink <fabian.mink@gmx.de>
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


f = 1; #frequency
N = 30;  #Number of Harmonics


t = np.linspace(0.00, 2.0, 500)
k = np.arange(0, N+1)

signal_types = ['Rectangle', 'Pulse', 'Symm. Pulse']
type_selector = 0


#Rechteckfunktion
def rectangle(k, A=1):
    ak = 0*k.astype(np.float64);
    bk = np.append(0, (A * 4/np.pi * ((k[1:]%2) == 1) * 1/k[1:]));    
    return ak,bk

#Rechteckpuls, Tastgrad d
def pulse(k, d=0.5, A=1):
    ak = 2*d*np.sinc(k*d)
    ak[0]=d
    bk = 0*k.astype(np.float64);
    bk = A*bk
    return ak,bk

#Symmetrischer Rechteckpuls
def symmPulse(k, alpha=30, A=1):
    ak = 0*k.astype(np.float64);
    alpha = alpha * np.pi /180 
    bk = np.append(0, (A * 4/np.pi * np.cos(k[1:]*alpha) * ((k[1:]%2) == 1) * 1/k[1:]));
    return ak,bk

fig, (ax_x, ax_bar) = plt.subplots(2, 1)

line_fade, = ax_x.plot(t, 0*t ,'k-', linewidth=2);
#line_cos, = ax_x.plot(t, 0*t ,'r-', linewidth=1);
#line_sin, = ax_x.plot(t, 0*t ,'b-', linewidth=1);

line_harmonics_cos = []
line_harmonics_sin = []
for ik in k:
    line_harmonics_cos.append(  ax_x.plot(t, 0*t, linewidth=1)[0]  ) 
    line_harmonics_sin.append(  ax_x.plot(t, 0*t, linewidth=1)[0]  ) 

ax_x.set_axisbelow(True)
ax_x.grid(1)
ax_x.set_xlim(0, 2)
ax_x.set_ylim(-1.5, 1.5)
ax_x.set_xlabel("$t  /  T$")
ax_x.set_ylabel("$x  /  \hat{x}$")
ax_x.set_position([0.125,0.6,0.8,0.35])



bar_coeff_cos = ax_bar.bar(k-0.15, 0*k.astype(np.float64), 0.2, color='red'); 
bar_coeff_sin = ax_bar.bar(k+0.15, 0*k.astype(np.float64), 0.2, color='blue'); 
bar_coeff_abs = ax_bar.bar(k,     0*k.astype(np.float64), 0.1, color='grey'); 
ax_bar.set_axisbelow(True)
ax_bar.grid(1)


ax_bar.set_xlim(-1, N+1)
#ax_bar.set_ylim(0, 1.3)
ax_bar.set_ylim(-1.3, 1.3)

ax_bar.set_xticks(k)

ax_bar.set_xlabel("$k$")
ax_bar.set_ylabel("$x_k$")
ax_bar.set_position([0.125,0.25,0.8,0.25])

#Sliders
#see: https://matplotlib.org/stable/gallery/widgets/index.html
axharmonic = fig.add_axes([0.075, 0.025, 0.375, 0.03])
harmonic_slider = Slider(
    ax=axharmonic,
    label='N',
    valmin=0,
    valmax=N,
    valinit=N,
    valstep=1,
)

axfade = fig.add_axes([0.075, 0.075, 0.375, 0.03])
fade_slider = Slider(
    ax=axfade,
    label='Fade',
    valmin=0,
    valmax=1,
    valinit=1,
)

axshift = fig.add_axes([0.075, 0.125, 0.375, 0.03])
shift_slider = Slider(
    ax=axshift,
    label='Shift',
    valmin=0,
    valmax=360,
    valinit=0,
)

axpara = fig.add_axes([0.55, 0.125, 0.375, 0.03])
para_slider = Slider(
    ax=axpara,
    label='para',
    valmin=0,
    valmax=1,
    valinit=0.5,
)

#axcheck = ax_x.inset_axes([0.0, 0.0, 0.12, 0.2])
axcheck = fig.add_axes([0.55, 0.025, 0.17, 0.08])
para_check = CheckButtons(
    ax=axcheck,
    labels=['Harmonics', 'all', 'as abs'],
    actives=[False, False, False],
    #labels=['all harmonics', 'test'],
    #actives=[False, True],
    #label_props={'color': 'black'},
    #frame_props={'edgecolor': 'black'},
    #check_props={'facecolor': 'red'},
)

axselectsignal = fig.add_axes([0.75, 0.025, 0.1, 0.05])
selectsignal_button = Button(axselectsignal, signal_types[type_selector])

# The function to be called anytime a slider's value changes
def update(val):
    kpl = int(harmonic_slider.val)
    fade = fade_slider.val
    alpha_shift = 2*np.pi*k*shift_slider.val/360
    para = para_slider.val
    show_harmonics = para_check.get_status()[0]
    show_harmonics_all = para_check.get_status()[1]
    show_harmonics_asabs = para_check.get_status()[2]
    
        
    #select signal    
    ak,bk = rectangle(k)
    if type_selector == 1:
        ak,bk = pulse(k,1*para)

    if type_selector == 2:
        ak,bk = symmPulse(k,90*para)
        
    #abs value (Amplitude)
    ck = np.sqrt(np.square(ak) + np.square(bk))     
    Ck_RMS = ck/np.sqrt(2)
    Ck_RMS[0] = ck[0]
    
    #print(Ck_RMS)
    sig_RMS = np.sqrt(np.sum(np.square(Ck_RMS)))
    
    harmonics_RMS = np.sqrt(np.sum(np.square(Ck_RMS[2:])))
    #if DC: harmonics_RMS = np.sqrt(np.sum(np.square(Ck_RMS[1:])))
    
    
    thd_r = np.nan
    rel_fund = np.nan
    thd_f = np.nan
    if(sig_RMS > 0.0):
        #Klirrfaktor
        thd_r = harmonics_RMS/sig_RMS
        #Grundschwingungsgehalt
        rel_fund = Ck_RMS[1]/sig_RMS
        #if DC: rel_fund = Ck_RMS[0]/sig_RMS
    
    if(Ck_RMS[1] > 0.0):
        #THD, related to fundamental
        thd_f = harmonics_RMS/Ck_RMS[1]
        #if DC: rel_fund = harmonics_RMS/Ck_RMS[0]
        
    
    
    
    print("RMS: %05.2f, RMS of Harmonics: %05.2f, THDr: %05.4f, THDf: %05.4f, Relative Fund.: %05.4f" % (sig_RMS, harmonics_RMS, thd_r, thd_f, rel_fund) )
    
    ak_shift =  np.cos(alpha_shift) * ak - np.sin(alpha_shift) * bk    
    bk_shift =  np.sin(alpha_shift) * ak + np.cos(alpha_shift) * bk

    [mt, mk] = np.meshgrid(t,k);
    [mt, mak] = np.meshgrid(t,ak_shift);
    [mt, mbk] = np.meshgrid(t,bk_shift);

    #x_cos = mak * np.cos(2*np.pi*mk*f*mt)
    #x_sin = mbk * np.sin(2*np.pi*mk*f*mt)
    sig_hrmc_k = mak * np.cos(2*np.pi*mk*f*mt) + mbk * np.sin(2*np.pi*mk*f*mt)
    sig_upto_hrmc_k = np.cumsum(sig_hrmc_k, axis=0);
    
    if (kpl >= 1):
        line_fade.set_ydata( (sig_upto_hrmc_k[kpl-1, :])*(1-fade) + (sig_upto_hrmc_k[kpl, : ])*fade   );
    else :
        line_fade.set_ydata( (sig_upto_hrmc_k[kpl, : ])*fade   );
    #line_cos.set_ydata( (x_cos[kpl, : ])*fade   );
    #line_sin.set_ydata( (x_sin[kpl, : ])*fade   );

    ak_fade = np.append(ak_shift[0:kpl], ak_shift[kpl]*fade);
    ak_fade = np.append(ak_fade, ak_shift[kpl+1:] * 0);    
    
    bk_fade = np.append(bk_shift[0:kpl], bk_shift[kpl]*fade);
    bk_fade = np.append(bk_fade, bk_shift[kpl+1:] * 0);
    
    ck_fade = np.append(ck[0:kpl], ck[kpl]*fade);
    ck_fade = np.append(ck, ck[kpl+1:] * 0);
    
    
    if show_harmonics :
        for ik in k:
            if (ik <= kpl) and (show_harmonics_all or (ik == kpl)):
                harm_x_cos = ak_shift[ik] * np.cos(2*np.pi*ik*f*t) 
                harm_x_sin = bk_shift[ik] * np.sin(2*np.pi*ik*f*t)
                line_harmonics_cos[ik].set_visible(True)
                if not show_harmonics_asabs:
                    line_harmonics_cos[ik].set_ydata( harm_x_cos );
                    line_harmonics_sin[ik].set_ydata( harm_x_sin );
                    line_harmonics_sin[ik].set_visible(True)
                else:
                    line_harmonics_cos[ik].set_ydata( harm_x_cos + harm_x_sin);
                    line_harmonics_sin[ik].set_visible(False)
            else:
                line_harmonics_cos[ik].set_visible(False)
                line_harmonics_sin[ik].set_visible(False)
                

    
    
    for rect,h in zip(bar_coeff_cos,ak_fade):
        rect.set_height(h)
    
    for rect,h in zip(bar_coeff_sin,bk_fade):
        rect.set_height(h)

    for rect,h in zip(bar_coeff_abs,ck_fade):
        rect.set_height(h)
    

    fig.canvas.draw_idle()


def nextSignal(event):
    global type_selector
    if type_selector < len(signal_types)-1:
        type_selector+=1
    else:
        type_selector=0
        
    selectsignal_button.label.set_text(signal_types[type_selector])
    update(0)

def harmonicVisibility(event):
    show_harmonics = para_check.get_status()[0]    
    if not show_harmonics:
        for ik in k:
            line_harmonics_cos[ik].set_visible(False)
            line_harmonics_sin[ik].set_visible(False)
    
    update(0)    


# register the update functions for each widget
harmonic_slider.on_changed(update)
shift_slider.on_changed(update)
fade_slider.on_changed(update)
para_slider.on_changed(update)
para_check.on_clicked(harmonicVisibility)
selectsignal_button.on_clicked(nextSignal)

#initial calculation
harmonicVisibility(0)
#update(0)

plt.show()