#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 19:58:36 2025

@author: minkfabi
"""

import numpy as np
import matplotlib.pyplot as plt
import drawPaper as dp

pos0_lat = 50.33405201368627
pos0_lon = 8.752422649964268

home_lat = 50.3299013596345
home_lon = 8.759395926306713

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
         'x_label' : '$x / \mathrm{m}$',
         'y_label' : '$y / \mathrm{m}$',
         'fg_axes' : True,
}


plt.plot(delta_x, delta_y, 'rx', lw=1, zorder = 100)

fig = plt.gcf()
dp.drawPaper(fig, **myDim);
plt.savefig("map_fb.png", dpi=300)

plt.show()

