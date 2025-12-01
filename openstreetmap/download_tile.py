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

import math
import requests
from matplotlib import pyplot as plt

#see: https://wiki.openstreetmap.org/wiki/Raster_tile_providers
#server = "https://tile.openstreetmap.org"  #OpenStreetMap's Standard tile 
#server = "https://tile.openstreetmap.de"  #German variant of the Standard tile layer
server = "https://b.tile.opentopomap.org"
headers = {'user-agent': 'fm-tile-app/0.1'}


def pos2tile(lat, lon):
    #see: https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames
    x = (lon + 180)/360 * 2**zoom
    y = (1   -    1/math.pi*math.log(math.tan(lat/180*math.pi) + 1/math.cos(lat/180*math.pi)   )  ) * 2**(zoom-1)

    x = int(x)
    y = int(y)

    return(x,y)


def download_tile(server, z, x, y):
    url = server + "/" + str(z) + "/" + str(x) + "/" + str(y) + ".png"
    fn = "tile_" + str(z) + "_" + str(x) + "_" + str(y) + ".png"
    
    with requests.get(url, headers=headers) as r:
        with open(fn, 'wb') as f:
            f.write(r.content)
    
    return fn

def get_fn(server, z, x, y):
    fn = "tile_" + str(z) + "_" + str(x) + "_" + str(y) + ".png"
   
    return fn

zoom = 14

tile_size_x = 100
tile_size_y = 100

#FB, Kaiserstraße Ecke Ockstaedter Straße
#lat = 50.33405  
#lon =  8.75242

#Butzbach Hoch-Weisel
lat = 50.400
lon =  8.629

tile_x0, tile_y0 = pos2tile(lat, lon)


tiles_x = range(0,5)
tiles_y = range(-2,3)

for tile_x_offs in tiles_x:
    for tile_y_offs in tiles_y:
        
        #todo: download tile only if not already downloaded before
        
        #filename = download_tile(server, zoom, tile_x0+tile_x_offs, tile_y0+tile_y_offs)
        filename = get_fn(server, zoom, tile_x0+tile_x_offs, tile_y0+tile_y_offs)

        img = plt.imread(filename)
        plt.imshow(img, extent=[tile_size_x*tile_x_offs, tile_size_x*(tile_x_offs+1), -tile_size_y*tile_y_offs, -tile_size_y*(tile_y_offs-1)])
        

ax = plt.gca()
ax.set_xlim([0,500])
ax.set_ylim([-300,300])
plt.show()

        
          
        



