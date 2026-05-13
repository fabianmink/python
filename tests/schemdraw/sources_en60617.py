# -*- coding: utf-8 -*-
"""
Created on Wed May 13 08:45:57 2026

@author: Fabian Mink
"""

import schemdraw.elements as elm
import schemdraw.segments as seg
import math

gap = (math.nan, math.nan)  # Put a gap in a path

class SourceU(elm.Element2Term):
    ''' Voltage source element acc. to EN60617-2'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.segments.append(seg.Segment([(0, 0), (1, 0)]))
        self.segments.append(seg.SegmentCircle((0.5, 0), 0.5,))
        self.elmparams['theta'] = 90
        
class SourceI(elm.Element2Term):
    ''' Current source element acc. to EN60617-2 '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.segments.append(seg.Segment([(0, 0), (0, 0), gap, (1, 0), (1, 0)]))
        self.segments.append(seg.Segment([(0.5, 0.5), (0.5, -0.5)]))
        self.segments.append(seg.SegmentCircle((0.5, 0), 0.5,))
        self.elmparams['theta'] = 90