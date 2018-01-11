# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:22:58 2018

@author: e0008730
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

from pandas_stock_data import grab_data
import datetime

stockdata = grab_data('NVDA', datetime.datetime(2017,1,1))
stock_return = np.log(stockdata['Close'] / stockdata['Open'])

stock_return = stock_return[220:]

#plt.plot(stockdata['Open'])
plt.hist(stock_return)
print(stats.describe(stock_return))


print(stats.normaltest(stock_return))

#print(stock_return)
#print(price)

#print(apple)