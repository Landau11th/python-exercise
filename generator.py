# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:43:47 2018

@author: e0008730
"""
from collections import Iterator
from collections import Iterable


def triangles():
    ls = [1]
    while 1:
        yield ls
        ls = [ls[i]+ls[i+1] for i in range(len(ls)-1) ]
        ls = [1]+ls+[1]
    return 'done'

yanghui = triangles()
for i in range(5):
    l = next(yanghui)
    print(l)
    
print(isinstance(yanghui, Iterator))
print(isinstance(yanghui, Iterable))

#not an object
print(isinstance(triangles, Iterator))
print(isinstance(triangles, Iterable))    

