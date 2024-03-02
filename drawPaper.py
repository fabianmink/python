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
    
    #x_label_range = (x_cm_min*x_scale, x_cm_max*x_scale) 
    
    #x_orig = x_cm_orig*x_scale;
    #y_orig = y_cm_orig*y_scale;
    
    
    for axi in fh.axes:
        #print(axi)
        axi.set_position([0,0,1,1])
        axi.patch.set_alpha(0)
        
        
        axi.set_xlim((0-x_zero, x_width-x_zero)) #must be adapted acc to scaling
        axi.set_ylim((0-y_zero, y_height-y_zero))
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
    axGrid.annotate('$t/\mathrm{s}$', xy=(0, 0), xytext=(x_cm_max-0.1+0.5, y_cm_orig-0.4))
    axGrid.annotate('$u_\mathrm{x}/\mathrm{V}$', xy=(0, 0), xytext=(x_cm_orig-0.4, y_cm_max+0.15+0.5))
    
    
    
    #axes for x-y-tick lables
    label_offs_x = (x_cm_zero-x_cm_min)*x_scale
    label_offs_y = (y_cm_zero-y_cm_min)*y_scale
    label_width = (x_cm_max-x_cm_min)*x_scale
    label_height = (y_cm_max-y_cm_min)*y_scale
    
    #axLabels = fh.add_axes([x_cm_min/x_cm,y_cm_min/y_cm,(x_cm_max-x_cm_min)/x_cm,(y_cm_max-y_cm_min)/y_cm])
    axLabelsx = fh.add_axes([x_cm_min/x_cm,y_cm_orig/y_cm,(x_cm_max-x_cm_min)/x_cm,(y_cm_max-y_cm_orig)/y_cm])
    axLabelsy = fh.add_axes([x_cm_orig/x_cm,y_cm_min/y_cm,(x_cm_max-x_cm_orig)/x_cm,(y_cm_max-y_cm_min)/y_cm])
    axLabelsx.zorder = -1
    axLabelsy.zorder = -1
    axLabelsx.patch.set_alpha(0)
    axLabelsy.patch.set_alpha(0)
    #axLabelsx.xaxis.set_ticks(np.arange(x_label_range[0], x_label_range[1], 0.25))
    axLabelsx.xaxis.set_ticks(np.arange(-2, 2, 0.5))
    axLabelsx.yaxis.set_ticks(np.array([]))
    axLabelsy.xaxis.set_ticks(np.array([]))
    axLabelsy.yaxis.set_ticks(np.arange(-2, 2, 0.5))
    axLabelsx.axes.set_xlim((-label_offs_x, label_width-label_offs_x)) 
    axLabelsx.axes.set_ylim((-label_offs_y, label_height-label_offs_y))
    axLabelsy.axes.set_xlim((-label_offs_x, label_width-label_offs_x)) 
    axLabelsy.axes.set_ylim((-label_offs_y, label_height-label_offs_y))
    axLabelsx.set_frame_on(False)
    axLabelsy.set_frame_on(False)
    
    
    
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

