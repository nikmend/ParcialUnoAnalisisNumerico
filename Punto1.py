#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:33:03 2017

@author: 
"""
import math
import sympy


def f(x):
    a=4
    b=2
    c=1
    return a*x**2 + b*x + c
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
    while( f(x) > error and k < ciclos):
        k = k + 1
        
        if(df(x) != 0):
            x = xant - ((f(xant)*df(xant))/((df(xant)**2)-(f(xant)*df(df(xant)))))
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

    x = 0
    error = 0.0001
    ciclos = 30
    resultado = raiz(x,error, ciclos)
    print "la raiz es: ", resultado

main()