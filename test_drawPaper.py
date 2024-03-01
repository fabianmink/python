#   Copyright (c) 2020 Fabian Mink <fabian.mink@gmx.de>
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

#clear myDim;

import drawPaper as dp
import matplotlib.pyplot as plt
import numpy as np


#Abmaﬂe
# myDim = {'x_cm': 15,
#          'y_cm': 12,
#          'x_cm_orig' : 1,
#          'y_cm_orig': 5,
#          'x_cm_min' : 0.5,
#          'y_cm_min' : 3.5,
#          'x_shift' : 1,
#          'y_shift' : 2,
#          'x_cm_max': 13.5,
#          'y_cm_max': 11,
#          'x_scale': 0.1,
#          'y_scale': 0.25
# }

myDim = {'x_cm_zero' : 1.5,
         'y_cm_zero': 5,
         'x_scale': 0.1,
         'y_scale': 0.25,
         'x_cm' : 16
}


t = np.linspace(-1, 1, 1000)
f = 5
u = np.sin(2.0*np.pi*f*t)

plt.plot(t, u, 'r-', lw=1)
fig = plt.gcf()

dp.drawPaper(fig, **myDim);

#fh = dp.drawPaper(test=2)
#dp.drawPaper("hello", test=2)
#dp.drawPaper("hello", x_cm=1, test=2)

#dp.drawPaper("hello", x_cm=1, test=2, 7) geht nicht


#dp.drawPaper(myDim,"test",0);

plt.savefig("test.png", dpi=300)


