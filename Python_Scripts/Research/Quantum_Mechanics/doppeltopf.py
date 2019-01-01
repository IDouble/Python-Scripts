#!/usr/bin/env python

#/*==========================================================================*\
#|* Filename:    2well.py
#|* Description: Gives energy levels of double well inside an infinite well by 
#|*              solving transedent equations. 
#|*              
#|* Date:        14-10-2014
#|* Copyright:   Huber group @ ETH (c) 2014
#|* Author(s):   Murad Tovmasyan
#\*==========================================================================*/

from __future__ import division
import numpy as np
#import scipy
import sys
import math
import matplotlib.pyplot as plt

########################################################################
#### This part finds the roots of a function in a given interval [a,b]
########################################################################
def rootsearch(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b:
            return None,None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    return x1,x2

def bisect(f,x1,x2,switch=0,epsilon=1.0e-6):
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 0.0:
        return x2
    if f1*f2 > 0.0:
        print('Root is not bracketed')
        return None
    n = math.ceil(math.log(abs(x2 - x1)/epsilon)/math.log(2.0))
    for i in range(int(n)):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        if (switch == 1) and (abs(f3) >abs(f1)) and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0:
            return x3
        if f2*f3 < 0.0:
            x1 = x3
            f1 = f3
        else:
            x2 =x3
            f2 = f3
    return (x1 + x2)/2.0

def roots(f, a, b, eps=1e-3):
    Roots=[]
    #print ('The roots on the interval [%f, %f] are:' % (a,b))
    while 1:
        x1,x2 = rootsearch(f,a,b,eps)
        if x1 != None:
            a = x2
            root = bisect(f,x1,x2,1)
            if root != None:
                pass
                Roots.append((round(root,-int(math.log(eps, 10)))))
        else:
            return Roots
            break

########################################################################
########################################################################

## Parameters

emax = 100
vmax = 200
beta = 0.2

#emax = int(sys.argv[1])
#vmax = int(sys.argv[2])
#beta = float(sys.argv[3])

delta = 0.01

All_down = {}
All_up = {}


for v in range(vmax):
    ### e < v
    def down_levels(e,v=v,beta=beta):
        return math.sin(math.pi*(1-beta)*math.sqrt(e))+math.tanh(math.pi*beta*math.sqrt(v-e))*(0.5*(math.sqrt((v-e)/e)+math.sqrt(e/(v-e)))-0.5*(math.sqrt((v-e)/e)-math.sqrt(e/(v-e)))*math.cos(math.pi*(1-beta)*math.sqrt(e)))

    ### e > v
    def up_levels(e,v=v,beta=beta):
        return 0.5*(math.sqrt(e/(e-v))+math.sqrt((e-v)/e))*math.sin(math.pi*beta*math.sqrt(e-v))*math.cos(math.pi*(1-beta)*math.sqrt(e)) + 0.5*(math.sqrt(e/(e-v))-math.sqrt((e-v)/e))*math.sin(math.pi*beta*math.sqrt(e-v)) + math.cos(math.pi*beta*math.sqrt(e-v))*math.sin(math.pi*(1-beta)*math.sqrt(e))

    if v+delta < emax:
        All_up[v]=roots(up_levels,v+delta,emax)
    if v-delta > 0:
        All_down[v]=roots(down_levels,delta,min(emax,v-delta))


### Saving dictionaries into a file
import cPickle as pickle

pickle.dump( All_up, open( "Up-emax-%.d-vmax-%.d-beta-%.2f.p"%(emax,vmax,beta), "wb" ))
pickle.dump( All_down, open( "Down-emax-%.d-vmax-%.d-beta-%.2f.p"%(emax,vmax,beta), "wb" ))
