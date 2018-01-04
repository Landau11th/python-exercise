# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:41:40 2018

@author: e0008730
"""

import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('input could only be int or float')
    delta = b**2 - 4*a*c
    
    if delta >= 0:
        x = math.sqrt(delta)
        p = (-b + x)/2/a
        m = (-b - x)/2/a
        return p , m
    else:
        return 'No real solution'

def product(*args):
    result = 1
    for i in args:
        result = i*result
    return result

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


if __name__ == "__main__":
    d = {'a':1, 3:'2'}
    print(d)
    
    city = 'SG' 
    #must by aa = bb
    print(person('Jim', 30, kk = city))
    #following is wrong syntax
    #print(person('Jim', 30, city))
    some= 1
    list= 2
    of= 3
    vars= 4
    dict_of_vars = dict((name,eval(name)) for name in ['some','list','of','vars'] )
    print(dict_of_vars)
    
    print(quadratic(2.0,3,1))
    
    print(product(3,6,5))