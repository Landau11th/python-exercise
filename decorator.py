# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:07:10 2018

@author: e0008730
"""

import time;
import datetime;
import types

#print(time.time())
#print(datetime.datetime.now())


def log(func : types.FunctionType):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper

def ellapsed_time(func : types.FunctionType):
    def wrapper_t(*args, **kw):
        t = time.time()
        print('start time is %s' % t)
        #print('%s ran for %s ms' % (func.__name__, 1000*(time.time() - t)))
        return func(*args, **kw)
    print('end time is %s' % time.time())
    return wrapper_t

@log
def current_time():
    print("current_time called at " + datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
    #return datetime.datetime.now()
    
@ellapsed_time
def something(n : float):
    time.sleep(n)
        

if __name__ == '__main__':
    
    f = current_time
    #print(f())
    f()
    
    print('declare f as something')
    f = something
    print('call f i.e. something')
    f(0.5)
    
    print(f.__name__)
    print(type([]))
    print(type(current_time))