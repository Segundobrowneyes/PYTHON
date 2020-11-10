# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:46:04 2020
Created on Tue Oct 20 21:04:42 2020
OTRA FORMA DE HACERLO  Fácil La secuencia de Filius Bonacci
Imprimir los primeros 100 números de la sucesión de Fibonacci separados por newlines.
ki+1=ki+ki−1

donde k0=0,k1=1
@author: Madmax
"""
k1 = 0
k2 = 1
k3 = int()
for k in range(10):
        k3 = k2 + k1
        k1 = k2
        k2 = k3
        print (k1)  
      
