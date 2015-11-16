# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/sonet/.spyder2/.temp.py
"""
import pygmaps
from method import *
import glob


mymap = pygmaps.maps(23.7805916667,90.4038666667, 7)
dirList= glob.glob("./Users/Sonet/Dropbox/Camera Uploads/*.jpg")
#print dirList
for items in dirList:
    # call pic_lonlat method
    image, lon,lat= pic_lonlat(items)
    if (lat):
        print image, lon,lat
        mymap.addpoint(lon,lat, "ff0000")        
    #call google maps

    else: 
        print image,'No GPS data'
mymap.draw('./mymap.html')

