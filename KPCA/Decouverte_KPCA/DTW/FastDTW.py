# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:39:34 2020

@author: Kalmuns
"""

#DTWfast  need pip install fastdtw, numpy and scipy
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
y = np.array([[2,2], [3,3], [4,4], [1,0]])
distance, path = fastdtw(x, y, dist=euclidean)
print(distance)
