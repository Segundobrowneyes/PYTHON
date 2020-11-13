# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:14:47 2020
La conjetura del Dr. Lothar
Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:
Si el numero es par, se debe dividir por  2 .
Si el numero es impar, se debe multiplicar por  3  y sumar  1 .
Este proceso se repite hasta llegar al numero  1  y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

Ejemplo para  n=6 :

6,3,10,5,16,8,4,2,1 

Resultado = 8
@author: Madmax
"""

def Lothar (number):
          if (number % 2 == 0) :
            return number // 2  
          elif (number % 2 == 1) :
            return  number * 3 + 1 
          else:
           print ("falla")
           return None
 
number= int (input('Ingrese un número: '))

while number> 1 :
           number  = Lothar (number)   
print (number)

