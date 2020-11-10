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
contar = int (0)
L= int( input('Ingrese un número: ') )
def aumenta(L):
    while L>1 :
     contar = contar + 1      
    if L % 2 :
                L = L*3+1
    else:
                    L  = L//2
                    return  L 
print ("Resultado =", contar)    

