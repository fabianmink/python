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
from matplotlib import pyplot as plt 
import matplotlib as mpl
import math

def drawPaper(fh="none", **kwargs):
    #print(fig)
    
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
    
    
    #x_tickres = x_scale  #default
    
    
    #x_orig = x_cm_orig*x_scale;
    #y_orig = y_cm_orig*y_scale;
    
    
    for axi in fh.axes:
        #print(axi)
        axi.set_position([0,0,1,1])
        axi.patch.set_alpha(0)
        
        
        axi.set_xlim((0-x_zero, x_width-x_zero)) #must be adapted acc to scaling
        axi.set_ylim((0-y_zero, y_height-y_zero))
        
        #todo:get max zorder!
        #print(axi)
    
    
    #axes for grid to background
    axGrid = fh.add_axes([0,0,1,1])
    axGrid.zorder = -2;
    axGrid.xaxis.set_ticks(np.arange(0, x_cm, x_res))
    axGrid.yaxis.set_ticks(np.arange(0, y_cm, y_res))
    axGrid.axes.set_xlim((0, x_cm)) 
    axGrid.axes.set_ylim((0, y_cm))
    axGrid.axes.grid(axis='both')
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
    
    #axTicks = fh.add_axes([x_cm_min/x_cm,y_cm_min/y_cm,(x_cm_max-x_cm_min)/x_cm,(y_cm_max-y_cm_min)/y_cm])
    axTicksx = fh.add_axes([x_cm_min/x_cm,y_cm_orig/y_cm,(x_cm_max-x_cm_min)/x_cm,(y_cm_max-y_cm_orig)/y_cm])
    axTicksy = fh.add_axes([x_cm_orig/x_cm,y_cm_min/y_cm,(x_cm_max-x_cm_orig)/x_cm,(y_cm_max-y_cm_min)/y_cm])
    #axTicksx.zorder = -1
    #axTicksy.zorder = -1
    axTicksx.zorder = 100
    axTicksy.zorder = 100
    axTicksx.patch.set_alpha(0)
    axTicksy.patch.set_alpha(0)
    
    x_tick_range = (math.floor(x_cm_min-x_cm_zero)*x_cm_tick*x_scale, (math.ceil(x_cm_max-x_cm_zero)+0.1)*x_cm_tick*x_scale) 
    y_tick_range = (math.floor(y_cm_min-y_cm_zero)*y_cm_tick*y_scale, (math.ceil(y_cm_max-y_cm_zero)+0.1)*y_cm_tick*y_scale)
    #print(x_tick_range)
    #print(y_tick_range)
    
    axTicksx.xaxis.set_ticks(np.arange(x_tick_range[0], x_tick_range[1], x_cm_tick*x_scale))
    #axTicksx.xaxis.set_ticks(np.arange(-2, 2, 0.5))
    axTicksx.yaxis.set_ticks(np.array([]))
    axTicksy.xaxis.set_ticks(np.array([]))
    #axTicksy.yaxis.set_ticks(np.arange(-2, 2, 0.5))
    axTicksy.yaxis.set_ticks(np.arange(y_tick_range[0], y_tick_range[1], y_cm_tick*y_scale))
    axTicksx.axes.set_xlim((-ticks_offs_x, ticks_width-ticks_offs_x)) 
    axTicksx.axes.set_ylim((-ticks_offs_y, ticks_height-ticks_offs_y))
    axTicksy.axes.set_xlim((-ticks_offs_x, ticks_width-ticks_offs_x)) 
    axTicksy.axes.set_ylim((-ticks_offs_y, ticks_height-ticks_offs_y))
    axTicksx.set_frame_on(False)
    axTicksy.set_frame_on(False)
    
    
    
    inch_per_cm = 1/2.54
    fh.set_size_inches(x_cm*inch_per_cm,y_cm*inch_per_cm)
      
    
    #print(x_cm)
    
    return(fh)
    
    

def drawPaper_tmp1(dim_val, argfile, valha):
 
    #Dimensions
    x_cm = dim_val['x_cm']
    y_cm = dim_val['y_cm']

    #Origin KOS
    x_cm_orig = dim_val['x_cm_orig']; 
    y_cm_orig = dim_val['y_cm_orig'];

    #Minimum KOS
    x_cm_min = dim_val['x_cm_min'];
    y_cm_min = dim_val['y_cm_min'];

    #Maximum KOS
    x_cm_max = dim_val['x_cm_max'];
    y_cm_max = dim_val['y_cm_max'];

    #Scaling
    x_noscale = 1;
    x_scale = 1;
    y_noscale = 1;
    y_scale = 1;

    #Resolution /cm
    x_res = 0.5;
    y_res = 0.5;

    #Axis shift
    x_shift = 0;
    y_shift = 0;

    if 'x_scale' in dim_val:
        x_scale = dim_val['x_scale'];
        x_noscale = 0;


    x_label = '';
    y_label = '';


    #Tick resolution
    x_tickres = 0;
    y_tickres = 0;
    #if(isfield(dim_val,'x_tickres'))
    #    x_tickres = dim_val.x_tickres;
    #   
    #    if(isfield(dim_val,'y_tickres'))
    #    y_tickres = dim_val.y_tickres;
        


    #Calc min/max
    x_min = x_scale * (x_cm_min-x_cm_orig) + x_shift;
    y_min = y_scale * (y_cm_min-y_cm_orig) + y_shift;

    #Maximum values
    x_max = x_scale * (x_cm_max-x_cm_orig) + x_shift;
    y_max = y_scale * (y_cm_max-y_cm_orig) + y_shift;

    fh = plt.figure();

    #v_cm = (v_pos-x_shift) / x_scale + x_cm_orig;
    #h_cm = (h_pos-y_shift) / y_scale + y_cm_orig;
    #plt.plot(np.array([0, 0]), np.array([0, y_cm]))
    plt.plot(np.array([0, x_cm]), np.array([0, y_cm]))

    #Axes for grid and h/v lines
    #plot([0 0],[0 y_cm],"k--");
    #hold on;
    #for iv = 1:length(v_cm)
    #plot([v_cm(iv) v_cm(iv)],[y_cm_min y_cm_max],"k--");
    #end
    #for ih = 1:length(h_cm)
    #plot([x_cm_min x_cm_max],[h_cm(ih) h_cm(ih)],"k--");
    #end


    #axes();
    ha = plt.gca();
    ha.xaxis.set_ticks(np.arange(0, x_cm, x_res))
    ha.yaxis.set_ticks(np.arange(0, y_cm, y_res))
    
    ha.axes.set_xlim((0, x_cm)) 
    ha.axes.set_ylim((0, y_cm))
    ha.axes.grid(axis='both')
    
    ha.set_position([0,0,1,1])
    

    
    #ha.Position = [0 0 1 1];
    #set(ha,'Xcolor','none','Ycolor','none','box','off');

    #x-arrow
    # X = [x_cm_min*1/x_cm  (x_cm_max+0.5)/x_cm];
    # Y = [y_cm_orig*1/y_cm   y_cm_orig*1/y_cm];
    # han = annotation('arrow',X,Y);
    # han.LineWidth = 0.75;
    # %axis label
    # %dim = [X(2)-0.02 Y(1)-0.00 .1 .1];
    # Xanno = (x_cm_max+0.5)/x_cm;
    # Yanno = (y_cm_orig-0.4)*1/y_cm;
    # dim = [Xanno Yanno .2 .2];
    # han = annotation('textbox',dim,'String',x_label,'Margin',0,'VerticalAlignment', 'bottom');
    # han.LineStyle='none';
    # hold off;

    # #y-arrow
    # X = [x_cm_orig*1/x_cm x_cm_orig*1/x_cm];
    # Y = [y_cm_min*1/y_cm   (y_cm_max+0.5)*1/y_cm];
    # han = annotation('arrow',X,Y);
    # han.LineWidth = 0.75;
    # %axis label
    # %dim = [X(1) Y(2)-0.05 .1 .1];
    # Xanno = (x_cm_orig-0.4)*1/x_cm;
    # Yanno = (y_cm_max+0.6)*1/y_cm;
    # dim = [Xanno Yanno .2 .2];
    # han = annotation('textbox',dim,'String',y_label,'Margin',0,'VerticalAlignment', 'bottom');
    # han.LineStyle='none';

    # #x-axis
    # if(~x_noscale)
    # axes()
    # xlim([x_min,x_max])
    # ha = gca();
    # ha.Position = [x_cm_min*1/x_cm y_cm_orig*1/y_cm (x_cm_max-x_cm_min)*1/x_cm 1];
    # set(ha,'ytick',[],'Ycolor','none','box','off')
    # %set(ha,'Color','w')
    # set(ha,'Color','none')
    # if(x_tickres)
    #     set(ha,'xtick',ceil(x_min/x_tickres)*x_tickres:x_tickres:floor(x_max/x_tickres)*x_tickres);
    #     end
    #     end

    # #y-axis
    # if(~y_noscale)
    # axes()
    # ylim([y_min,y_max])
    # ha = gca();
    # ha.Position = [x_cm_orig*1/x_cm y_cm_min*1/y_cm 1 (y_cm_max-y_cm_min)*1/y_cm];
    # set(ha,'xtick',[],'Xcolor','none','box','off')
    # %set(ha,'Color','w')
    # set(ha,'Color','none')
    # if(y_tickres)
    # set(ha,'ytick',ceil(y_min/y_tickres)*y_tickres:y_tickres:floor(y_max/y_tickres)*y_tickres);
    # end
    # end

    # filename = 'test_kos';
    # if(nargin >= 2)
    #     filename = argfile;
    #     end

    # if(nargin >= 3)
    # %Value-Axes
    # valha = copyobj(valha, fh);
    # axes(valha);
    
    # %copyobj(hl,valha);
    
    # xlim(valha,[x_min,x_max]);
    # ylim(valha,[y_min,y_max]);
    # valha.Position = [x_cm_min*1/x_cm y_cm_min*1/y_cm (x_cm_max-x_cm_min)*1/x_cm (y_cm_max-y_cm_min)*1/y_cm];
    # set(valha,'xtick',[],'Xcolor','none','box','off');
    # set(valha,'ytick',[],'Ycolor','none','box','off');
    # set(valha,'Color','none')
    # end
    
    inch_per_cm = 1/2.54

    fig_size = x_cm*inch_per_cm,y_cm*inch_per_cm

    fh.set_size_inches(fig_size[0],fig_size[1])
    fh.dpi = 300


    plt.savefig("test.png", dpi=300)

