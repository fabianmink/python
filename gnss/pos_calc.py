# -*- coding: utf-8 -*-

#   Copyright (c) 2025 Fabian Mink <fabian.mink@iem.thm.de>
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
import matplotlib.pyplot as plt
import drawPaper as dp


#FB, Kaiserstraße Ecke Ockstädter Straße
pos0_lat = 50.33405
pos0_lon = 8.75242

#FB THM A2.0.09
home_lat = 50.32990
home_lon = 8.75939

delta_phi_lat = (home_lat - pos0_lat)/ 360 * 2*np.pi 
delta_phi_lon = (home_lon - pos0_lon)/ 360 * 2*np.pi * np.cos(pos0_lat/ 360 * 2*np.pi)

delta_x = delta_phi_lon * 6371000
delta_y = delta_phi_lat * 6371000

#noise_x = np.random.normal(0, 12, 20)
#noise_y = np.random.normal(0, 12, 20)
#delta_x = delta_x + noise_x
#delta_y = delta_y + noise_y

datafile = 'Friedberg.png'
img = plt.imread(datafile)

map_size_x = 2000  #m
map_size_y = 3000  #m
map_x0 = -522
map_y0 = -1347

plt.imshow(img, extent=[map_x0, map_x0+map_size_x, map_y0, map_y0+map_size_y], zorder = -100 )

# Sine function test example
myDim = {'x_cm_min' : 0.8,
         'x_cm_zero' : 5, 
         'y_cm_zero': 10,
         'x_scale': 100,
         'y_scale': 100,
         'x_cm' : 16,
         'y_cm' : 18,
         'x_label' : r'$x / \mathrm{m}$',
         'y_label' : r'$y / \mathrm{m}$',
         'fg_axes' : True,
}


plt.plot(delta_x, delta_y, 'rx', lw=1, zorder = 100)

fig = plt.gcf()
dp.drawPaper(fig, **myDim);
plt.savefig("map_fb.png", dpi=300)

plt.show()

