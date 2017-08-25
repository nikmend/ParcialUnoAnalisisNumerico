

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:33:03 2017

@author: 
"""
import math
import sympy
def f(x):
    return 2**x - 1.3

def raiz(x0, error,ciclos,x1): # x ininical,  error permitido, numero de ciclos maximo
    k = 0
    i=2
    q0=f(x0)
    q1=f(x1)

    print("iteracion\traiz\t\terror ")
    while( i <= ciclos):
        k = x1-q1*(x1-x0)/(q1-q0)
        errorf = abs( k - x1 )
        
        if (errorf<error):
            return k
        print i,'\t',k,'\t',errorf 
        i=i+1
        x0=x1
        q0=q1
        x1=k
        q1=f(k)

    
    if (i == ciclos):
        print("no converge")


def main():

    x0 = -1
    x1 = 1
    error = 0.000001
    ciclos = 30
    resultado = raiz(x0,error, ciclos,x1)
    print "la raiz es: ", resultado

main()