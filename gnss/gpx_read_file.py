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

import gpxpy
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import csv



lat = []
lon = []
time = []
t_since_start = []

#pos correction
offs_lat = 0
offs_lon = 0


gpx_file = open('2025-10-22_bu_fb_thm.gpx', 'r')

gpx = gpxpy.parse(gpx_file)


#csvfile = open('gnss_data_bu_fb.csv', 'w', newline='')
csvfile = open('gnss_data_bu_fb_notime.csv', 'w', newline='')

#fieldnames = ['time', 'lat', 'lon']
fieldnames = ['lat', 'lon']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


for track in gpx.tracks:
    for segment in track.segments:
        print("New segment")
        for point in segment.points:
            #print(f'Point at ({point.latitude},{point.longitude}) h= {point.elevation}')
            
            thisdatetime = point.time
            thislat = point.latitude + offs_lat
            thislon = point.longitude + offs_lon
            
            time.append(thisdatetime)
            lat.append(thislat)
            lon.append(thislon)

            #writer.writerow({'time': thisdatetime.isoformat(), 'lat': thislat, 'lon': thislon})
            writer.writerow({'lat': thislat, 'lon': thislon})

            



csvfile.close()




       

lat = np.array(lat)
lon = np.array(lon)

m_lat = np.mean(lat)
m_lon = np.mean(lon)

#fig, axs = plt.subplots(1, 3, tight_layout=True)
#axs[0].plot(lon-m_lon, lat-m_lat, 'r-x', lw=1)
#n_bins = 20
#axs[1].hist(lat-m_lat, bins=n_bins)
#axs[2].hist(lon-m_lon, bins=n_bins)

plt.plot(lon-m_lon, lat-m_lat, 'r-x', lw=1)


#plt.plot(time)

plt.show()