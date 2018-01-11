# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:40:40 2018

@author: e0008730
"""

from pandas_datareader import data   # Package and modules for importing data; this code may change depending on pandas version
import datetime


# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

ticker_symbol = "^DJI"
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
data = data.DataReader(ticker_symbol, "yahoo", start, end)

data.to_csv(ticker_symbol+'.csv')
