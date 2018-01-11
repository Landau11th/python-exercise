# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:58:55 2018

@author: e0008730
"""

from scipy import stats
import numpy as np
import time

pts = 1000
np.random.seed(seed = int(time.time()))
a = np.random.normal(0, 1, size=pts)
#b = np.random.normal(2, 1, size=pts)
#x = np.concatenate((a, b))
print(stats.normaltest(a))
