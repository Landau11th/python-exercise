# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:22:58 2018

@author: e0008730
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

stockdata = pd.read_csv('^DJI.csv')
stock_return = np.log(stockdata['Adj Close'] / stockdata['Open'])


#plt.plot(stockdata['Open'])
plt.hist(stock_return)

stock_return_mean = np.mean(stock_return)
stock_return_sigma = np.std(stock_return)

print(stats.describe(stock_return))

print(stats.normaltest((stock_return - stock_return_mean)/stock_return_sigma))

#print(stock_return)
#print(price)

#print(apple)