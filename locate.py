# -*- coding: utf-8 -*-
"""
Spyder Editor
This temporary script file is located here:
locate.py
"""

import pygmaps

mymap = pygmaps.maps(23.7805916667,90.4038666667, 7)
mymap.addpoint(23.7805916667,90.4038666667, "ff0000")
mymap.addpoint(23.7755333333,90.4160861111,"ff0000")
mymap.addpoint(21.4112944444, 91.9870555556, "ff0000")
path = [(23.7805916667,90.4038666667),(23.775533333,90.4160861111),(21.4112944444,91.9870555556)]

mymap.addpath(path,"#ff0000")
mymap.draw('./mymap.html')
