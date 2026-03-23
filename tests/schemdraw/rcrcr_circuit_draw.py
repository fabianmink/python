# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:15:27 2026

@author: Fabian Mink
"""

import schemdraw
import schemdraw.elements as elm

schemdraw.config(inches_per_unit=0.8/2.54, lw = 1.0, fontsize=11)
elm.style(elm.STYLE_IEC)

    
with schemdraw.Drawing(file='rcrcr_circuit.png', dpi=300) as d:
    
    Uin_pos = elm.Dot(open=True)
    d.add(Uin_pos)
    #print(d.here)
    d.add(elm.Resistor().right().label(r'$R_1$'))
    d.add(elm.Dot())
    d.push()
    C1 = elm.Capacitor().down().label(r'$C_1$')
    d.add(C1)
    d.pop()
    d.add(elm.Resistor().right().label(r'$R_2$'))
    d.add(elm.Dot())
    d.push()
    d.add(elm.Capacitor().down().label(r'$C_2$'))
    d.pop()
    d.add(elm.Line().right().length(1))
    d.push()
    d.add(elm.Dot())
    d.add(elm.Resistor().down().label(r'$R_3$',loc='bottom'))
    d.pop()
    d.add(elm.Line().right().length(2))
    Uout_pos = elm.Dot(open=True)
    d.add(Uout_pos)
    d.move(0,-3)
    Uout_neg = elm.Dot(open=True)
    d.add(Uout_neg)
    d.add(elm.Line().left().length(2))
    d.add(elm.Dot())
    d.add(elm.Line().left().length(1))
    d.add(elm.Dot())
    d.add(elm.Line().left())
    d.add(elm.Dot())
    d.add(elm.Line().left())
    Uin_neg = elm.Dot(open=True)
    d.add(Uin_neg)
    
    
    d.add(elm.Arrow().at(C1.start + schemdraw.util.Point((0.5,-1))).to(C1.end + schemdraw.util.Point((0.5,1))).label(r'$u_\mathrm{C1}$', loc='bottom'))
    
    #d.add(elm.Arrow().at(Uin_pos.start + schemdraw.util.Point((0,-0.3))).to(Uin_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{in}$', ofst=[0,0]))
    d.add(elm.Arrow().at(Uin_pos.start + schemdraw.util.Point((0,-0.3))).to(Uin_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{in}$'))
    #d.add(elm.Arrow().at(Uout_pos.start + schemdraw.util.Point((0,-0.3))).to(Uout_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{out}$', ofst=[0,1.25]))
    d.add(elm.Arrow().at(Uout_pos.start + schemdraw.util.Point((0,-0.3))).to(Uout_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{out}$', loc='bottom'))
    
    print(d.get_bbox())
    
 