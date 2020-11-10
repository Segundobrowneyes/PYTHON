# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:40:47 2020
Fácil Ordenar palabras
Std input:
n palabras separadas por espacios
Output deseado:

Una lista de palabras ordenadas alfabeticamente separadas por newlines.
Recomendación: Investigar el método sort para ordenar y split para separar 
un string y convertirlo a una lista.

Ejemplo:
Input:

saludos al gran rey
@author: Madmax
"""
txt = input('Ingrese palabras separadas por espacios : ') 
x= txt.split() #split para separar un string y convertirlo a una lista
x.sort()    #una lista de palabras ordenadas alfabeticamente  método sort para ordenarla.
print(*x, sep = "\n") #salida con  newline