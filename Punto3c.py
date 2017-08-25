#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:33:03 2017

@author: 
"""
import math
import sympy
def f(x):
    return x**4 - x
def df(x):
    from sympy import Symbol
    from scipy.misc import derivative
    return derivative(f,x,dx=1e-6)

def errorf(act,ant):
     return ((abs(act-ant))/act)

def raiz(x, error,ciclos): # x ininical,  error permitido, numero de ciclos maximo
    k = 0
    xant = 1
    err = 0
    print("iteracion\traiz\terror ")
    x = x-f(x)/df(x)
    print k, '\t', x, '\t', err
    while( f(x) > error and k < ciclos):
        k = k + 1
        
        if(df(x) != 0):
            x = x-f(x)/df(x)
            err = errorf(x,xant)
            print k, '\t', x, '\t', err, ' | ',f(x)
            xant = x

        else:
            xant = x
            x += error

    
    if (k == ciclos):
        print("No converge")
    else:
        return x

def main():

    x = 1
    error = 0.0001
    ciclos = 10
    resultado = raiz(x,error, ciclos)
    print "la raiz es: ", resultado

main()