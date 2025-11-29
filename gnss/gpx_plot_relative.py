# -*- coding: utf-8 -*-

#   Copyright (c) 2025 Fabian Mink <fabian.mink@gmx.de>
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

import gpxpy
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime as dt




lat = []
lon = []
time = []
t_since_start = []

#pos correction
offs_lat = 0
offs_lon = 0

#GPS overflow correction
#offs_time = dt.timedelta(days=0)
offs_time = dt.timedelta(days=7168)



#
pos0_lat = 50.33405  #° Must fit to x0
pos0_lon = 8.75242   #° Must fit to y0

gpx_file = open('thm_100km_2025.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    for segment in track.segments:
        print("New segment")
        for point in segment.points:
            #print(f'Point at ({point.latitude},{point.longitude}) h= {point.elevation}')
            
            thisdatetime = point.time + offs_time
            thislat = point.latitude + offs_lat
            thislon = point.longitude + offs_lon
            
            time.append(thisdatetime)
            lat.append(thislat)
            lon.append(thislon)

            
     

lat = np.array(lat)
lon = np.array(lon)

#Earth radius
r = 6371000 #m
dx_dlon = r * 2*math.pi/360 * math.cos(pos0_lat * 2.0*math.pi/360)
dy_dlat = r * 2*math.pi/360


delta_x = dx_dlon * (lon - pos0_lon)
delta_y = dy_dlat * (lat - pos0_lat)


plt.plot(delta_x, delta_y, 'r-', lw=1)
ax = plt.gca()
ax.grid()
ax.set_xlabel(r"$x / \mathrm{m}$")
ax.set_ylabel(r"$y / \mathrm{m}$")


plt.show()