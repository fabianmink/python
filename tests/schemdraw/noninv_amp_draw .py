# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:15:27 2026

@author: Fabian Mink
"""

import schemdraw
import schemdraw.elements as elm

schemdraw.config(inches_per_unit=0.8/2.54, lw = 1.0, fontsize=11)
elm.style(elm.STYLE_IEC)

    
with schemdraw.Drawing(file='noninv_amp_circuit.png', dpi=300) as d:
   
    op = elm.Opamp(leads=True).flip()
    
    
    elm.Line().at(op.in1).down(d.unit*2/3)
    elm.Line().tox(op.out)
    
    
    R2 = elm.Resistor().toy(op.out).idot().label(r'$R_{2}$', loc='bot')
    elm.Dot()
    R1 = elm.Resistor().down().at(R2.start).label(r'$R_{1}$', loc='bot')
    elm.Vss()
    
    d.push()
    elm.Dot()
    gndline = elm.Line().left(d.unit*5/3)
    
    
    Uin_neg = elm.Dot(open=True)
    
    elm.Line().tox(gndline.end).at(op.in2)
    
    Uin_pos = elm.Dot(open=True)
    
    d.pop()
    
    gndline = elm.Line().right(d.unit*2/3)
    
    Uout_neg = elm.Dot(open=True)
    
    elm.Line().tox(gndline.end).at(op.out)
    
    Uout_pos = elm.Dot(open=True)       
    
    d.add(elm.Arrow().at(Uin_pos.start + schemdraw.util.Point((0,-0.3))).to(Uin_neg.start + schemdraw.util.Point((0,0.3))).label(r'$U_\mathrm{e}$'))
    d.add(elm.Arrow().at(Uout_pos.start + schemdraw.util.Point((0,-0.3))).to(Uout_neg.start + schemdraw.util.Point((0,0.3))).label(r'$U_\mathrm{a}$', loc='bottom'))
 