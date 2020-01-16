# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:15:24 2020
@author: 98212
"""

def get_centerpoint(lis):
    area = 0.0
    x,y = 0.0,0.0
 
    a = len(lis)
    for i in range(a):
        lat = lis[i][0] #x
        lng = lis[i][1] #y
 
        if i == 0:
            lat1 = lis[-1][0]
            lng1 = lis[-1][1]
 
        else:
            lat1 = lis[i-1][0]
            lng1 = lis[i-1][1]
 
        fg = (lat*lng1 - lng*lat1)/2.0
 
        area += fg
        x += fg*(lat+lat1)/3.0
        y += fg*(lng+lng1)/3.0
 
    x = x/area
    y = y/area
    return x,y

lis=[(0,2),(0,6),(4,6),(7,3),(11,3),(11,0),(3,0),(3,2)]# list for the x,y of points
print(get_centerpoint(lis))#get the G point

















