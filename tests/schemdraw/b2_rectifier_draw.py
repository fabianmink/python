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
    
    D1 = elm.Diode().up().label('D1')
    elm.Line().right()
    elm.Dot()
    elm.Line().right()
    uout_pos = elm.Dot()
    elm.Line().down().at(uin_pos.start)
    D2 = elm.Diode().reverse().label('D2')
    
    elm.Line().right()
    elm.Dot()
    elm.Line().right()
    uout_neg = elm.Dot()
    
    elm.Line().right().at(src.start)
    elm.Line().right()
    
    uin_neg = elm.Dot()
    
    elm.Line().up()  
    D3 = elm.Diode().up().label('D3')
    D4 = elm.Diode().reverse().down().at(uin_neg.start).label('D4')
    
    elm.Line().down().at(uout_pos.start)
    elm.Capacitor().down().label(r'$C$')
    elm.Line().down()
    
    elm.Line().right().at(uout_pos.start)
    
    elm.Line().down()
    elm.Resistor().down().label(r'$R$')
    elm.Line().down()
    elm.Line().left()
    
    
    # op = elm.Opamp(leads=True)
    
    # R1 = elm.Resistor().at(op.in1).left().idot().label(r'$R$', loc='bot')
    
    # Uin_pos = elm.Dot(open=True)
    
    # d.move(0,-d.unit)
    # Uin_neg = elm.Dot(open=True)
    
    # gndline = elm.Line().right(d.unit*8/3)
    
    # Uout_neg = elm.Dot(open=True)
    
    
    # elm.Line().toy(gndline.start).at(op.in2)
    # elm.Dot()
    # elm.Vss()
    
    
    # elm.Line().tox(gndline.end).at(op.out)
    # Uout_pos = elm.Dot(open=True)
    
    # elm.Line().up(d.unit/2).at(op.in1)
    # elm.Capacitor().tox(op.out).label(r'$C$')
    # elm.Line().toy(op.out).dot()
       
    
    # d.add(elm.Arrow().at(Uin_pos.start + schemdraw.util.Point((0,-0.3))).to(Uin_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{in}$'))
    # d.add(elm.Arrow().at(Uout_pos.start + schemdraw.util.Point((0,-0.3))).to(Uout_neg.start + schemdraw.util.Point((0,0.3))).label(r'$u_\mathrm{out}$', loc='bottom'))
 