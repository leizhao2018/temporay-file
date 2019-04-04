#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:03:48 2019

@author: jmanning
"""


import numpy as np
import netCDF4



def nearlonlat(lon,lat,lonp,latp): # needed for the next function get_FVCOM_bottom_temp 
    """ 
    i,min_dist=nearlonlat(lon,lat,lonp,latp) change 
    find the closest node in the array (lon,lat) to a point (lonp,latp) 
    input: 
        lon,lat - np.arrays of the grid nodes, spherical coordinates, degrees 
        lonp,latp - point on a sphere 
        output: 
            i - index of the closest node 
            min_dist - the distance to the closest node, degrees 
            For coordinates on a plane use function nearxy 
    """ 
    # approximation for small distance 
    cp=np.cos(latp*np.pi/180.) 
    dx=(lon-lonp)*cp
    dy=lat-latp 
    xi=np.argmin(abs(dx)) 
    yi=np.argmin(abs(dy))
#    print(xi,yi)
    min_dist=111*np.sqrt(dx[xi]**2+dy[yi]**2)
    return xi,yi,min_dist 


def get_depth(loni,lati):
    url='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol1.nc'
    nc = netCDF4.Dataset(url).variables 
    lon=nc['x'][:]
    lat=nc['y'][:]
    xi,yi,min_dist= nearlonlat(lon,lat,loni,lati) 
    return nc['z'][yi,xi],min_dist



#hardcode
lon,lat=-69.55500,42.40503
print(get_depth(loni=lon,lati=lat))
