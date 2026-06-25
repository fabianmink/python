# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:15:27 2026

@author: Fabian Mink
"""

import schemdraw
import schemdraw.elements as elm

schemdraw.config(inches_per_unit=0.8/2.54, lw = 1.0, fontsize=11)
elm.style(elm.STYLE_IEC)

    
with schemdraw.Drawing(file='b2_rectifier_circuit.png', dpi=300) as d:
    
    #src = elm.SourceSin().up().label(r'$u_\mathrm{in}$')
    src = elm.SourceSin().up()
        
    elm.Arrow().at( src.end + schemdraw.util.Point((-0.8,-0.5)) ).to(src.start + schemdraw.util.Point((-0.8,0.5))).label(r'$u_\mathrm{in}$', ofst=[0,0])
   
      
    elm.Line().right().at(src.end)
    
    uin_pos = elm.Dot()
    
    D1 = elm.Diode().up().label(r'$D_1$')
    elm.Line().right()
    elm.Dot()
    elm.Line().right()
    urect_pos = elm.Dot()
    elm.Line().down().at(uin_pos.start)
    D2 = elm.Diode().reverse().label(r'$D_3$')
    
    elm.Line().right()
    elm.Dot()
    elm.Line().right()
    uout_neg = elm.Dot()
    
    elm.Line().right().at(src.start)
    elm.Line().right()
    
    urect_neg = elm.Dot()
    
    elm.Line().up()  
    D3 = elm.Diode().up().label(r'$D_2$')
    D4 = elm.Diode().reverse().down().at(urect_neg.start).label(r'$D_4$')
    
    elm.Line().down().at(urect_pos.start)
    elm.Capacitor().down().label(r'$C$')
    elm.Line().down()
    
    elm.Line().right().at(urect_pos.start)
    uout_pos = elm.Dot(open=True)
    
    elm.Line().right()
        
    elm.Line().down()
    elm.Resistor().down().label(r'$R_\mathrm{L}$', loc='bottom')
    elm.Line().down()
    
    elm.Line().left()
    
    uout_neg = elm.Dot(open=True)
    
    elm.Line().left()
    
    elm.Arrow().at(uout_pos.start + schemdraw.util.Point((0,-0.3))).to(uout_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{out}$', ofst=[0,1.25])
    
