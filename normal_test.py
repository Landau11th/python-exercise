# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:58:55 2018

@author: e0008730
"""

from scipy import stats
import numpy as np

pts = 1000
np.random.seed(28041990)
a = np.random.normal(0, 1, size=pts)
b = np.random.normal(2, 1, size=pts)
x = np.concatenate((a, b))
k2, p = stats.normaltest(np.concatenate((a,b)))
alpha = 1e-3
print("p = {:g}".format(p))