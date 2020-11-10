# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:04:42 2020
Fácil La secuencia de Filius Bonacci
Imprimir los primeros 100 números de la sucesión de Fibonacci separados por newlines.
ki+1=ki+ki−1

donde k0=0,k1=1

@author: Madmax
"""
def fibonacci(k):
    if k < 2:
        return k
    else:
        
        return fibonacci(k-1) + fibonacci(k-2) # ki = ki-1 + ki-2

for x in range(10):
 print (fibonacci (x)) #mprimir los primeros 100 números de la sucesión de Fibonacci separados por newlines.

    