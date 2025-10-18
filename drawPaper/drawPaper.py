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
import numpy as np 
import math
import matplotlib as mpl
from matplotlib import pyplot as plt 

def drawPaper(fh="none", **kwargs):
    
    if fh == "none":
        #create a new empty figure, if none is given
        fh = plt.figure()
    
    
    if isinstance(fh, mpl.figure.Figure) == False:
        raise TypeError("first argument must be a figure")
    
    #print(type(fig))
    #print(kwargs)
    #print(type(kwargs))
    #print(kwargs.items())
    
    #for key, value in kwargs.items():
    #    print(key + '=' + str(value))
    
    #grid resolution (currently fixed to .5cm)
    x_res = 0.5;
    y_res = 0.5;
                
    x_cm = kwargs.get('x_cm',10) #default value 10
    y_cm = kwargs.get('y_cm',10) 
    
    x_scale = kwargs.get('x_scale',1) 
    y_scale = kwargs.get('y_scale',1) 
    
    #position of "0"-Point
    x_cm_zero = kwargs.get('x_cm_zero',1)
    y_cm_zero = kwargs.get('y_cm_zero',1)
    
    #position of coordinate system origin
    x_cm_orig = kwargs.get('x_cm_orig',x_cm_zero)
    y_cm_orig = kwargs.get('y_cm_orig',y_cm_zero)
    
    x_cm_min = kwargs.get('x_cm_min', 0.875)
    y_cm_min = kwargs.get('y_cm_min', 0.875)
    
    x_cm_max = kwargs.get('x_cm_max', x_cm-1.5)
    y_cm_max = kwargs.get('y_cm_max', y_cm-1.5)
    
    x_width = x_cm*x_scale;
    y_height = y_cm*y_scale;
    
    x_zero = x_cm_zero*x_scale;
    y_zero = y_cm_zero*y_scale;
    
    x_cm_tick = kwargs.get('x_cm_tick', 1)
    y_cm_tick = kwargs.get('y_cm_tick', 1)
    
    x_label = kwargs.get('x_label', '$x$')
    y_label = kwargs.get('y_label', '$y$')
    
    
    #position of "0"-Point
    fg_axes = kwargs.get('fg_axes',False)
    
    
    #x_tickres = x_scale  #default
    
    
    #x_orig = x_cm_orig*x_scale;
    #y_orig = y_cm_orig*y_scale;
    
    #Scale axes already defined in figure before this function is called
    for axi in fh.axes:
        #print(axi)
        axi.set_position([0,0,1,1])
        axi.patch.set_alpha(0)
        
        axi.set_xlim((0-x_zero, x_width-x_zero)) #adapted according to scaling
        axi.set_ylim((0-y_zero, y_height-y_zero))
        
        #todo:get max zorder for axTicksx/y.zorder
        #print(axi)
    
    
    #axes for grid to background
    axGrid = fh.add_axes([0,0,1,1])
    axGrid.xaxis.set_ticks(np.arange(0, x_cm, x_res))
    axGrid.yaxis.set_ticks(np.arange(0, y_cm, y_res))
    axGrid.axes.set_xlim((0, x_cm)) 
    axGrid.axes.set_ylim((0, y_cm))
    axGrid.axes.grid(axis='both', linewidth=0.5, color = 'lightgrey')
    #axGrid.axes.grid(axis='both', linewidth=0.5, color = 'darkgrey')
    axGrid.zorder = -2
    if fg_axes:
        axGrid.patch.set_alpha(0)
        axGrid.zorder = 0
        
    axGrid.set_axisbelow(True)
    plt.arrow(x_cm_min,y_cm_orig,(x_cm_max+0.2-x_cm_min),0,width=0.02,head_width=0.2,head_length=0.3,length_includes_head=False,fc='black')
    plt.arrow(x_cm_orig,y_cm_min,0,(y_cm_max+0.2-y_cm_min),width=0.02,head_width=0.2,head_length=0.3,length_includes_head=False,fc='black')
    axGrid.annotate(x_label, xy=(0, 0), xytext=(x_cm_max-0.1+0.5, y_cm_orig-0.4))
    axGrid.annotate(y_label, xy=(0, 0), xytext=(x_cm_orig-0.4, y_cm_max+0.15+0.5))
    
    
    #axes for x-y-tick lables
    ticks_offs_x = (x_cm_zero-x_cm_min)*x_scale
    ticks_offs_y = (y_cm_zero-y_cm_min)*y_scale
    ticks_width = (x_cm_max-x_cm_min)*x_scale
    ticks_height = (y_cm_max-y_cm_min)*y_scale
    
    axTicksx = fh.add_axes([x_cm_min/x_cm,y_cm_orig/y_cm,(x_cm_max-x_cm_min)/x_cm,(y_cm_max-y_cm_orig)/y_cm])
    axTicksy = fh.add_axes([x_cm_orig/x_cm,y_cm_min/y_cm,(x_cm_max-x_cm_orig)/x_cm,(y_cm_max-y_cm_min)/y_cm])
    #axTicksx.zorder = -1 #background
    #axTicksy.zorder = -1
    axTicksx.zorder = 100  #most likely to foreground
    axTicksy.zorder = 100
    axTicksx.patch.set_alpha(0)
    axTicksy.patch.set_alpha(0)
    
    if x_cm_tick > 0:
        x_tick_range = (math.floor(x_cm_min-x_cm_zero)*x_cm_tick*x_scale, (math.ceil(x_cm_max-x_cm_zero)+0.1)*x_cm_tick*x_scale) 
        axTicksx.xaxis.set_ticks(np.arange(x_tick_range[0], x_tick_range[1], x_cm_tick*x_scale))
    else:
        axTicksx.xaxis.set_ticks(np.array([]))
    
    axTicksx.yaxis.set_ticks(np.array([]))
    
    axTicksy.xaxis.set_ticks(np.array([]))
    if y_cm_tick > 0:
        y_tick_range = (math.floor(y_cm_min-y_cm_zero)*y_cm_tick*y_scale, (math.ceil(y_cm_max-y_cm_zero)+0.1)*y_cm_tick*y_scale)
        axTicksy.yaxis.set_ticks(np.arange(y_tick_range[0], y_tick_range[1], y_cm_tick*y_scale))
    else:
        axTicksy.yaxis.set_ticks(np.array([]))
    
    
    
    
    axTicksx.axes.set_xlim((-ticks_offs_x, ticks_width-ticks_offs_x)) 
    axTicksx.axes.set_ylim((-ticks_offs_y, ticks_height-ticks_offs_y))
    axTicksy.axes.set_xlim((-ticks_offs_x, ticks_width-ticks_offs_x)) 
    axTicksy.axes.set_ylim((-ticks_offs_y, ticks_height-ticks_offs_y))
    axTicksx.set_frame_on(False)
    axTicksy.set_frame_on(False)
    
    
    inch_per_cm = 1/2.54
    fh.set_size_inches(x_cm*inch_per_cm,y_cm*inch_per_cm)
      
   
    return(fh)
    
    
