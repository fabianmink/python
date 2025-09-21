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

import drawPaper as dp
import matplotlib.pyplot as plt
import numpy as np

# Sine function test example
myDim = {'x_cm_min' : 1.375,
         'x_cm_zero' : 1.5, 
         'y_cm_zero': 5,
         'x_scale': 0.1,
         'y_scale': 0.25,
         'x_cm' : 16,
         'y_cm' : 11,
         'x_label' : r'$t/\mathrm{s}$',
         'y_label' : r'$u_\mathrm{x}/\mathrm{V}$'
}


t = np.linspace(-0.05, 1.35, 1000)
f = 2
u = np.sin(2.0*np.pi*f*t)

plt.plot(t, u, 'r-', lw=1)
fig = plt.gcf()

dp.drawPaper(fig, **myDim);
plt.savefig("test_sin.png", dpi=300)

# Arrow test example
myDim = {'x_cm_zero' : 5, 
         'y_cm_zero': 5,
         'x_scale': 1,
         'y_scale': 1,
         'x_cm_tick' : 0,  #no ticks / tick labels
         'y_cm_tick' : 0,
         'x_cm' : 16,
         'y_cm' : 11,
         'x_label' : 'Re',
         'y_label' : 'Im'
}


plt.clf()

plt.arrow(0,0,1,1,width=0.01,head_width=0.15,head_length=0.2,length_includes_head=True,ec='red',fc='red')
plt.arrow(1,1,4,2,width=0.01,head_width=0.15,head_length=0.2,length_includes_head=True,ec='blue',fc='blue')
plt.arrow(5,3,-2,-2.5,width=0.01,head_width=0.15,head_length=0.2,length_includes_head=True,ec='green',fc='green')
dp.drawPaper(fig, **myDim);
plt.savefig("test_arrow.png", dpi=300)


