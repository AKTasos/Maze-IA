# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:41:51 2019

@author: tasos
"""

import numpy as np
import matplotlib.pyplot as plt

size=(5,5)
X,Y = size



map_array = np.random.randint(low=0, high = 3 , size=size)




fig, ax = plt.subplots()

ax.set_title('Maze plot')
ax.plot(map_array)


#plt.axes((0, 0, 1, 1), facecolor='w')



