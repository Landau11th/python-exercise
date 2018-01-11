# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:40:40 2018

@author: e0008730
"""

from os.path import isfile

import pandas as pd
from pandas_datareader import data   # Package and modules for importing data; this code may change depending on pandas version
from pandas_datareader._utils import RemoteDataError
import datetime

def grab_data(ticker_symbol, start, end = datetime.date.today(), source = 'yahoo', 
              fileformat = '.csv'):

    if isfile(ticker_symbol + fileformat)==False:
        max_trials = 10;
        for i in range(max_trials):
            try:
                stock_data = data.DataReader(ticker_symbol, source, start, end)
                stock_data.to_csv(ticker_symbol + fileformat)
            except RemoteDataError:
                print(RemoteDataError.characters_written)
                if i == max_trials:
                    print('Reach max trials, fail to grab data for ' + ticker_symbol)
                else:
                    print('Try again')
    #below part need modification
    #if the data is old, we can only delete the files manually
    else:
        stock_data = pd.read_csv(ticker_symbol + fileformat)
        
    return stock_data

if __name__ == '__main__':
    stock_data = grab_data('NVDA', datetime.datetime(2016,1,1))
    print(stock_data)
    
    
    
    
    
    
    
