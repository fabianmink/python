#see: https://matplotlib.org/stable/gallery/widgets/index.html
import matplotlib.pyplot as plt
import numpy as np
#import math
from matplotlib.widgets import Button, Slider


# The parametrized function to be plotted
def fun(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)


f = 1;
#t = np.arange(0, 1, 0.005);
t = np.linspace(0.00, 2.0, 500)

fading = np.linspace(0.00, 1.0, 10)

N = 30;
A = 1;

k = np.arange(0, N+1)

#Rechteckfunktion
#ak = 0*k.astype(np.float64);
#bk = A * 4/np.pi *( (k%2) == 1) * (k>0) * 1/k;
#bk[0] = 0;

#Rechteckpuls, Tastgrad d
#d = 0.4
#ak = 2/np.pi/k * np.sin(k*np.pi*d)
#ak[0] = d
#bk = 0*k.astype(np.float64);

#Symmetrischer Rechteckpuls
ak = 0*k.astype(np.float64);
alpha = 30 * np.pi /180 
bk = A * 4/np.pi * np.cos(k*alpha) * ( (k%2) == 1) * (k>0) * 1/k;
bk[0] = 0;


#Betrag
#ck = np.sqrt(np.square(ak) + np.square(bk))


fig, (ax_x, ax_bar) = plt.subplots(2, 1)

line_fade, = ax_x.plot(t, 0*t ,'k-', linewidth=2);
line_cos, = ax_x.plot(t, 0*t ,'r-', linewidth=1);
line_sin, = ax_x.plot(t, 0*t ,'b-', linewidth=1);
ax_x.set_axisbelow(True)
ax_x.grid(1)
ax_x.set_xlim(0, 2)
ax_x.set_ylim(-1.5, 1.5)
ax_x.set_xlabel("$t  /  T$")
ax_x.set_ylabel("$x  /  \hat{x}$")
ax_x.set_position([0.125,0.6,0.8,0.35])


bar_coeff_cos =  ax_bar.bar(k-0.1, k*0, 0.2, color='red'); 
bar_coeff_sin = ax_bar.bar(k+0.1, k*0, 0.2, color='blue'); 
#bar_coeff_abs = ax_bar.bar(k, k*0, 0.2, color='black'); 
ax_bar.set_axisbelow(True)
ax_bar.grid(1)


ax_bar.set_xlim(-1, N+1)
#ax_bar.set_ylim(0, 1.3)
ax_bar.set_ylim(-1.3, 1.3)

ax_bar.set_xticks(k)

ax_bar.set_xlabel("$k$")
ax_bar.set_ylabel("$x_k$")
ax_bar.set_position([0.125,0.25,0.8,0.25])

# adjust the main plot to make room for the sliders
#fig.subplots_adjust(left=0.125, bottom=0.3)

# Make a horizontal slider to control the frequency.
axharmonic = fig.add_axes([0.125, 0.025, 0.75, 0.03])
harmonic_slider = Slider(
    ax=axharmonic,
    label='N',
    valmin=0,
    valmax=N,
    valinit=N,
    valstep=1,
)

axfade = fig.add_axes([0.125, 0.075, 0.75, 0.03])
fade_slider = Slider(
    ax=axfade,
    label='Fade',
    valmin=0,
    valmax=1,
    valinit=1,
)

axshift = fig.add_axes([0.125, 0.125, 0.75, 0.03])
shift_slider = Slider(
    ax=axshift,
    label='Shift',
    valmin=0,
    valmax=360,
    valinit=0,
)

# Make a vertically oriented slider to control the amplitude
# axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
# amp_slider = Slider(
#     ax=axamp,
#     label="Amplitude",
#     valmin=0,
#     valmax=10,
#     valinit=init_amplitude,
#     orientation="vertical"
# )


# The function to be called anytime a slider's value changes
def update(val):
    kpl = int(harmonic_slider.val)
    fade = fade_slider.val
    
    #fade, kpl = math.modf(harmonic_slider.val)#
    #kpl = int(kpl) +1
    #if(kpl == N):
    #    kpl = N-1
    #    fade = 1
    
    alpha_shift = 2*np.pi*k*shift_slider.val/360
    
    ak_shift =  np.cos(alpha_shift) * ak - np.sin(alpha_shift) * bk    
    bk_shift =  np.sin(alpha_shift) * ak + np.cos(alpha_shift) * bk

    [mt, mk] = np.meshgrid(t,k);
    [mt, mak] = np.meshgrid(t,ak_shift);
    [mt, mbk] = np.meshgrid(t,bk_shift);

    x_cos = mak * np.cos(2*np.pi*mk*f*mt)
    x_sin = mbk * np.sin(2*np.pi*mk*f*mt)
    x = mak * np.cos(2*np.pi*mk*f*mt) + mbk * np.sin(2*np.pi*mk*f*mt)
    y = np.cumsum(x, axis=0);
    
    if (kpl >= 1):
        line_fade.set_ydata( (y[kpl-1, :])*(1-fade) + (y[kpl, : ])*fade   );
    else :
        line_fade.set_ydata( (y[kpl, : ])*fade   );
    line_cos.set_ydata( (x_cos[kpl, : ])*fade   );
    line_sin.set_ydata( (x_sin[kpl, : ])*fade   );
    
    
    bk_fade = np.append(bk_shift[0:kpl], bk_shift[kpl]*fade);
    bk_fade = np.append(bk_fade, bk_shift[kpl+1:] * 0);
    
    ak_fade = np.append(ak_shift[0:kpl], ak_shift[kpl]*fade);
    ak_fade = np.append(ak_fade, ak_shift[kpl+1:] * 0);
    
    #ck_fade = np.append(ck[0:kpl], ck[kpl]*fade);
    #ck_fade = np.append(ck_fade, ck[kpl+1:] * 0);
    
    
    for rect,h in zip(bar_coeff_cos,ak_fade):
        rect.set_height(h)
    
    for rect,h in zip(bar_coeff_sin,bk_fade):
        rect.set_height(h)
 
    fig.canvas.draw_idle()


def reset(event):
    harmonic_slider.reset()
#    amp_slider.reset()

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
#resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
#button = Button(resetax, 'Reset', hovercolor='0.975')

# register the update function with each slider
harmonic_slider.on_changed(update)
shift_slider.on_changed(update)
fade_slider.on_changed(update)
#button.on_clicked(reset)

update(0)


plt.show()