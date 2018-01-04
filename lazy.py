# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:20:03 2018

@author: e0008730
"""
import types

def lazy_sum(ls : list):
    def sum():
        ax = 0
        for n in ls:
            ax = ax + n
        return ax
    return sum

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
        i = 8
    return fs

def createCounter():
    ls = [0]
    def counter():
        ls[0] = ls[0] + 1
        return ls[0]
    return counter


if __name__ == "__main__":
    summed_list  = list(range(10))
    f = lazy_sum(summed_list)
    print(f())
    
    #using mutable variables produce wrong results!
    summed_list.append(12)
    print(f())
    #using looping variables produce wrong results!
    f1, f2, f3 = count()
    print(f1(), f2(), f3())

#    #follwing code gives True!!!!!
#    g = createCounter
#    h = createCounter
#    print(g==h)
    
    g = createCounter()
    h = createCounter()
    print(g==h)
    for i in range(3):
        print(g())
        print(h())
    
    
    