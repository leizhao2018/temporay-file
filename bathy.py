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
depth,distance=get_depth(loni=lon,lati=lat)
print('depth:  '+str(depth))
print('distance:  '+str(distance)+' km')
