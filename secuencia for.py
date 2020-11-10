# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:53:34 2020

Mostrar la siguiente secuencia de datos utilizando la instrucción for y la instrucción if:

0, 1, 4, 9, 16, 25, 6, 7, 8, 9
@author: Madmax
"""
for x in range(0, 10, 1):
  if x<=5:
   print(x*x, end="  ")#hago el multiplo end= sirve para que quede en la misma linea
  else:
      print(x, end="  ")#arriba de cinco vuelve a hacer X+=
