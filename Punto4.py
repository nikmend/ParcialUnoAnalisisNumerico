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

def aproximacionTaylorMetodoDos( valor, orden ):
     valorInicialDos = 0.0
     
     try:
         for item in xrange( orden ):
            valorSiguiente = float( (((1**item) * math.exp( valor ))/ math.factorial(item))* (valor**item))
            valorInicialDos += valorSiguiente
            
         return valorInicialDos

     except TypeError:
        print 'Ingrese un numero'
            
    
if __name__ == "__main__":
    
   aproximacionUno =  aproximacionTaylorMetodoUno( -5,20 )
   print aproximacionUno
   
   aproximacionDos =  aproximacionTaylorMetodoDos( -5,9 )
   print aproximacionDos
