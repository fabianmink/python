# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 17:37:41 2025

@author: Fabian Mink
"""

import numpy as np
import matplotlib.pyplot as plt


#Kugel -> Kartesisisch
#https://de.wikipedia.org/wiki/Kugelkoordinaten

#lon = phi
#lat = theta

#x = r cos (phi) cos (theta) 
#y = r sin (phi) cos (theta) 
#z = r sin (theta)

def latlon2xyz(lat, lon, r=6370):
    x = r * np.cos(lon / 180*np.pi) * np.cos(lat / 180*np.pi)
    y = r * np.sin(lon / 180*np.pi) * np.cos(lat / 180*np.pi)
    z = r * np.sin(lat / 180*np.pi)
    
    return x,y,z
    

def latlon2dxdydz(lat, lon, r=6370):
    dx_dphi   = r * -np.sin(pos0_lon / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
    dx_dtheta = r * np.cos(pos0_lon / 180*np.pi) * -np.sin(pos0_lat / 180*np.pi)
    #dx_dr =

    dy_dphi   = r * np.cos(pos0_lon / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
    dy_dtheta = r * np.sin(pos0_lon / 180*np.pi) * -np.sin(pos0_lat / 180*np.pi)
    #dy_dr =

    dz_dphi   = 0
    dz_dtheta = r * np.cos(pos0_lat / 180*np.pi)
    #dy_dr =
    
    
    #TODO Jacobi-Matrix definierten und zurückgeben
    return []


def WireframeSphere(centre=[0.,0.,0.], radius=1.,
                    n_meridians=20, n_circles_latitude=8):
    
    
    u, v = np.mgrid[0:2*np.pi:n_meridians*1j, 0:np.pi:n_circles_latitude*1j]
    sphere_x = centre[0] + radius * np.cos(u) * np.sin(v)
    sphere_y = centre[1] + radius * np.sin(u) * np.sin(v)
    sphere_z = centre[2] + radius * np.cos(v)

    return sphere_x, sphere_y, sphere_z



pos0_lat = 50.33405
#pos0_lat = 0
pos0_lon = 8.75242
r = 6370

phi_wire = np.arange(0, 360, 1)

#lon = phi
#lat = theta
posx = r * np.cos(pos0_lon / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
posy = r * np.sin(pos0_lon / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
posz = r * np.sin(pos0_lat / 180*np.pi)

wireLat_x = r * np.cos(phi_wire / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
wireLat_y = r * np.sin(phi_wire / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
wireLat_z = r * np.sin(pos0_lat / 180*np.pi) + 0*phi_wire

wireLon_x = r * np.cos(pos0_lon / 180*np.pi) * np.cos(phi_wire / 180*np.pi)
wireLon_y = r * np.sin(pos0_lon / 180*np.pi) * np.cos(phi_wire / 180*np.pi)
wireLon_z = r * np.sin(phi_wire / 180*np.pi) + 0*phi_wire


dx_dphi   = r * -np.sin(pos0_lon / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
dx_dtheta = r * np.cos(pos0_lon / 180*np.pi) * -np.sin(pos0_lat / 180*np.pi)

dy_dphi   = r * np.cos(pos0_lon / 180*np.pi) * np.cos(pos0_lat / 180*np.pi)
dy_dtheta = r * np.sin(pos0_lon / 180*np.pi) * -np.sin(pos0_lat / 180*np.pi)

dz_dphi   = 0
dz_dtheta = r * np.cos(pos0_lat / 180*np.pi)


local_x_meter = 4000
local_y_meter = 4000

delta_phi =   (local_x_meter/r/np.cos(pos0_lat / 180*np.pi))
delta_theta = (local_y_meter/r)


dphi = np.linspace(-delta_phi/2, delta_phi/2, 11)
dtheta = np.linspace(-delta_theta/2, delta_theta/2, 11)

DPHI, DTHETA = np.meshgrid(dphi, dtheta)

posx_s = posx + dx_dtheta * DTHETA + dx_dphi * DPHI 
posy_s = posy + dy_dtheta * DTHETA + dy_dphi * DPHI
posz_s = posz + dz_dtheta * DTHETA + dz_dphi * DPHI



central_point=[0.,0.,0.]

ax = plt.figure().add_subplot(projection='3d')
ax.view_init(elev=30, azim=-50, roll=0)

#fig = plt.figure()
#ax = fig.gca(projection='3d')
ax.set_aspect("equal")
#draw sphere
ax.plot_wireframe(*WireframeSphere(central_point, r, 25, 19), color="k", alpha=1, lw=0.5)
#ax.plot_wireframe(*WireframeSphere(central_point, r, 13, 7), color="k", alpha=1, lw=0.5)
ax.plot(posx, posy, posz, 'rx')
ax.plot(wireLat_x, wireLat_y, wireLat_z, 'r-')
ax.plot(wireLon_x, wireLon_y, wireLon_z, 'r-')

ax.plot_surface(posx_s, posy_s, posz_s, linewidth=0.5, alpha=0.5, edgecolors='k', facecolor='g')


# Verbindunglinien Ursprung auf Kugel bei Änderung um dphi / dtheta (je 15°)
pos0 = latlon2xyz(pos0_lat, pos0_lon)
pos0_dphi = latlon2xyz(pos0_lat, pos0_lon+15)
pos0_dtheta = latlon2xyz(pos0_lat+15, pos0_lon)
ax.plot([0, pos0[0]], [0, pos0[1]], [0, pos0[2]], 'g-')
ax.plot([0, pos0_dphi[0]], [0, pos0_dphi[1]], [0, pos0_dphi[2]], 'g-')
ax.plot([0, pos0_dtheta[0]], [0, pos0_dtheta[1]], [0, pos0_dtheta[2]], 'g-')


ax.quiver(posx, posy, posz, dx_dphi*delta_phi , dy_dphi*delta_phi , dz_dphi*delta_phi, color='k')
ax.quiver(posx, posy, posz, dx_dtheta*delta_theta, dy_dtheta*delta_theta, dz_dtheta*delta_theta, color='k')

#ax.plot(posx_s, posy_s, posz_s, 'gx-')

#ax.set_xlabel(r"$x / \mathrm{km}$")
#ax.set_ylabel(r"$y / \mathrm{km}$")
#ax.set_zlabel(r"$z / \mathrm{km}$")

ax.set_axis_off()

#ax.get_xaxis().set_ticklabels([])
#ax.get_yaxis().set_ticklabels([])
#ax.get_zaxis().set_ticklabels([])

#ax.get_xaxis().set_ticks([])
#ax.get_yaxis().set_ticks([])
#ax.get_zaxis().set_ticks([])

#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)
#ax.get_zaxis().set_visible(False)




plt.savefig("earth.png", dpi=300)

