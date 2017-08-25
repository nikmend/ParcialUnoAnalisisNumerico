#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 07:49:36 2017

@author: nicolas
"""
import math


def aproximacionTaylorMetodoUno( valor, orden ):
    
    valorInicial = 0.0
    
    try:
        for item in xrange( orden ):
            valorSiguiente = float(valor**item)/math.factorial(item)
            valorInicial += valorSiguiente

        return valorInicial
  
    except TypeError:
        print 'Ingrese un numero'

def aproximacionTaylorMetodoDos( x ):
     
    valor = float (1 - x + (x**2/2) - (x**3/6) + (x**4/24) - (x**5/120) + (x**6/720) - (x**7/5040) + (x**8/40320))

    return valor
            
    
if __name__ == "__main__":
    
   e = 0.00673794699085
   aproximacionUno =  aproximacionTaylorMetodoUno( -5, 9)
   print aproximacionUno, "error: ", (aproximacionUno-e)
   
   aproximacionDos =  aproximacionTaylorMetodoDos( 5.0)
   print aproximacionDos, "error: ", (aproximacionDos-e)

