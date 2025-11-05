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


import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import drawPaper as dp

#Earth radius
r = 6371000 #m


#Map data
datafile = 'Friedberg.png' #This has been generated using http://printmaps-osm.de/
map_size_x = 2000  #m width 
map_size_y = 3000  #m height
map_x0 = -522      #m x-offset
map_y0 = -1347     #m y-offset
#FB, Kaiserstraße Ecke Ockstaedter Straße
pos0_lat = 50.33405  #° Must fit to map_x0
pos0_lon = 8.75242   #° Must fit to map_y0


#FB THM A2.0.09 (only if not read from file)
pos_lat = 50.32990
pos_lon = 8.75939

#Get lat/lon data from csv-file
with open('gnss_data_fb.csv') as csv_file:
#with open('gnss_data_bu_fb.csv') as csv_file:
    home_lat = []
    home_lon = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            home_lat.append(float(row[1]))
            home_lon.append(float(row[2]))
            line_count += 1
            
    
    pos_lat = np.array(home_lat)
    pos_lon = np.array(home_lon)



delta_lat = pos_lat - pos0_lat
delta_lon = pos_lon - pos0_lon

dx_dlon = r * 2*math.pi/360 * math.cos(pos0_lat * 2.0*math.pi/360)
dy_dlat = r * 2*math.pi/360


delta_x = dx_dlon * delta_lon 
delta_y = dy_dlat * delta_lat


img = plt.imread(datafile)
plt.imshow(img, extent=[map_x0, map_x0+map_size_x, map_y0, map_y0+map_size_y], zorder = -100 )


plt.plot(delta_x, delta_y, 'r-', lw=1, zorder = 2000)
ax = plt.gca()
ax.grid()
ax.set_xlabel(r"$x / \mathrm{m}$")
ax.set_ylabel(r"$y / \mathrm{m}$")

fig = ax.get_figure()

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

#fig = plt.gcf()
dp.drawPaper(fig, **myDim);

plt.savefig("map_fb.png", dpi=300)

plt.show()

