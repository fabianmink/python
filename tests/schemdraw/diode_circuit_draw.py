# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:15:27 2026

@author: Fabian Mink
"""

import schemdraw
import schemdraw.elements as elm

import sources_en60617 as mysrcs



elm.style(elm.STYLE_IEC)

    
with schemdraw.Drawing(file='diode_circuit.png') as d:
    #src = d.add(elm.SourceV().up())
    src = d.add(mysrcs.SourceU().up())
    #src = d.add(mysrcs.SourceI().up())
    d.add(elm.Line().up())
    I = d.add(elm.Line().right())
    d.add(elm.Resistor().down().label('200 Ω'))
    D = d.add(elm.Diode().down().label('1N4148'))
    d.add(elm.Line().left())
    
    d.add(elm.Arrow().at( src.end + schemdraw.util.Point((-0.8,-0.5)) ).to(src.start + schemdraw.util.Point((-0.8,0.5))).label('2 V', ofst=[0,0]))
    d.add(elm.Arrow().at(I.start).to(I.end + schemdraw.util.Point((-0.2,0.0))).label('I', ofst=[1,0]))
    d.add(elm.Arrow().at( D.start + schemdraw.util.Point((+0.6,-1)) ).to(D.end + schemdraw.util.Point((+0.6,1))).label(r'$U_\mathrm{d}$', ofst=[0.,0.8]))
    
    