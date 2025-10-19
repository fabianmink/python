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

lat = []
lon = []
time = []
t_since_start = [0]

import numpy as np
import matplotlib.pyplot as plt
from pynmeagps import NMEAReader
import datetime as dt

with open('output_2025-10-19_14-23-55.log', 'rb') as stream:
  nmr = NMEAReader(stream, nmeaonly=True)
  for raw_data, parsed_data in nmr: 
    #print(parsed_data)
    
    if(parsed_data.identity == 'GNRMC'):
        msg_GNRMC = parsed_data
        lat.append(msg_GNRMC.lat)
        lon.append(msg_GNRMC.lon)
        datetime = dt.datetime.combine(msg_GNRMC.date, msg_GNRMC.time)
        time.append(datetime)
        delta = datetime - time[0];
        t_since_start.append( delta.total_seconds())
        

lat = np.array(lat)
lon = np.array(lon)

m_lat = np.mean(lat)
m_lon = np.mean(lon)

fig, axs = plt.subplots(1, 3, tight_layout=True)


axs[0].plot(lon-m_lon, lat-m_lat, 'r-x', lw=1)
n_bins = 20
axs[1].hist(lat-m_lat, bins=n_bins)
axs[2].hist(lon-m_lon, bins=n_bins)



plt.show()