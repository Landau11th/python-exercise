# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:43:01 2018

@author: e0008730
"""
import types
import functools


#something similar to decorator that counts time
def ellapsed_time(func : types.FunctionType, *args, **kw):
    
    
    return