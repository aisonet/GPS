# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:15:19 2015

@author: sonet
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/sonet/.spyder2/.temp.py
"""


def pic_lonlat (filename):
    
    import exifread
    # Open image file for reading (binary mode)
    f = open(filename, 'rb')
    
    s=[]   
    tags = exifread.process_file(f)
    for tag in tags.keys():  
        if tag in ('GPS GPSLatitude','GPS GPSLongitude'):
            s.append(str(tags[tag]))
    # remove others 
    if (s):
        lon=s[0].replace('[',' ').replace(']',' ').replace(',',' ').replace('/',' ').split( )
        lat=s[1].replace('[',' ').replace(']',' ').replace(',',' ').replace('/',' ').split( ) 
    #print 'no gps'
    #conversion lon lat 
        longi=float(lon[0])+(float(lon[1]))/60 + float((float(lon[2])/float(lon[3]))/3600)
        lati=float(lat[0])+(float(lat[1]))/60 + float((float(lat[2])/float(lat[3]))/3600)
        return filename, longi, lati
    else: 
        return filename,'No GPS', ''
    
    
