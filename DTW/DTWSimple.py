# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:06:32 2020

@author: Kalmuns
"""
# need dtai distance to work (pip install dtaidistance) -require Pytho 3

from dtaidistance import dtw
s1 = [0, 0, 1, 2, 1, 0, 1, 0, 0,4,7,3]
s2 = [0, 0, 2, 2, 1, 0, 1, 0, 0,2,1,4,2,4,6,7,3]
distance = dtw.distance(s1, s2)
print(distance)
distance=dtw.distance(s1,s2,window=10,max_dist=15,max_step=40,max_length_diff=(20),penalty=1 )