#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:03:48 2019
update: add the range of every area, decrease the time of loop every file
@author:leizhao
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


def get_depth(loni,lati,mindist_allowed=10):
    
    url1='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol1.nc'
    url2='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol2.nc'
    url3='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol3.nc'
    url4='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol4.nc'
    url5='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol5.nc'
    url6='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol6.nc'
    url7='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol7.nc'
    url8='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol8.nc'
    url9='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol9.nc'
    url10='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol10.nc'
    
    if 230.00000003>=loni>= 170.0 and 66.5 >=lati>=48.5:
        urlak='https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_southak.nc'
        nc = netCDF4.Dataset(urlak).variables 
        lon=nc['lon'][:]
        lat=nc['lat'][:]
        xi,yi,min_dist= nearlonlat(lon,lat,loni,lati) 
        if min_dist<mindist_allowed:
            return float(nc['z'][yi,xi]),min_dist
    elif -64.0>=loni>=-80.0 and 48.0>=lati>=40.0:
        urls=[url1]
    elif -68.0>=loni>=-85.0 and 40.0>=lati>=31.0:
        urls=[url2,url3]
    elif -78.0>=loni>=-87.0 and 35.0>=lati>=24.0:
        urls=[url3]
    elif -87.0>=loni>= -94.0 and 36.0 >=lati>=24.0:
        urls=[url4]
    elif -94.0>=loni>= -108.0 and 38.0>=lati>= 24.0:
        urls=[url5]
    elif -114.0>=loni>= -126.0 and 37.0>=lati>= 32.0:
        urls=[url6]
    elif -117.0>=loni>= -128.0 and 44.0>=lati>= 37.0:
        urls=[url7]
    elif -116.0>=loni>= -128.0 and 49.0 >=lati>=44.0:
        urls=[url8]
    elif -64.0>=loni>= -68.0 and 20.0 >=lati>=16.0:
        urls=[url9]
    elif -152.0>=loni>= -162.0 and 24.0>=lati>= 18.0:
        urls=[url10]  
    else:
        return np.nan,np.nan
    for url in urls:
        nc = netCDF4.Dataset(url).variables 
        lon=nc['x'][:]
        lat=nc['y'][:]
        xi,yi,min_dist= nearlonlat(lon,lat,loni,lati) 
        if min_dist<mindist_allowed:
            return float(nc['z'][yi,xi]),min_dist
    


#hardcode
lon,lat=-126.146,37.46
depth,distance=get_depth(loni=lon,lati=lat)
print('depth:  '+str(depth)+' m')
print('distance:  '+str(distance)+' km')
