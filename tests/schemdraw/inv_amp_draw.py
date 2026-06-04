# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:15:27 2026

@author: Fabian Mink
"""

import schemdraw
import schemdraw.elements as elm

schemdraw.config(inches_per_unit=0.8/2.54, lw = 1.0, fontsize=11)
elm.style(elm.STYLE_IEC)

    
with schemdraw.Drawing(file='inv_amp_circuit.png', dpi=300) as d:
   
    op = elm.Opamp(leads=True)
    
    R1 = elm.Resistor().at(op.in1).left().idot().label(r'$R_{1}$', loc='bot')
    
    Uin_pos = elm.Dot(open=True)
    
    d.move(0,-d.unit)
    Uin_neg = elm.Dot(open=True)
    
    gndline = elm.Line().right(d.unit*8/3)
    
    Uout_neg = elm.Dot(open=True)
    
    
    elm.Line().toy(gndline.start).at(op.in2)
    elm.Dot()
    elm.Vss()
    
    
    elm.Line().tox(gndline.end).at(op.out)
    Uout_pos = elm.Dot(open=True)
    
    elm.Line().up(d.unit/2).at(op.in1)
    elm.Resistor().tox(op.out).label(r'$R_2$')
    elm.Line().toy(op.out).dot()
       
    
    d.add(elm.Arrow().at(Uin_pos.start + schemdraw.util.Point((0,-0.3))).to(Uin_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{E}$'))
    d.add(elm.Arrow().at(Uout_pos.start + schemdraw.util.Point((0,-0.3))).to(Uout_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{A}$', loc='bottom'))
 