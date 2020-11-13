# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:42:45 2020
Mini-desafío: floats
Crear:

Una función que convierta grados Celsius a grados Farenheit (https://es.wikipedia.org/wiki/Grado_Fahrenheit)
Una función que convierta grados Celsius a grados Kelvin (https://es.wikipedia.org/wiki/Kelvin)
El usuario debe ingresar una temperatura en grados Celsius y el programa debe mostrar
 las conversiones a Farenheit y Kelvin utilizando las funciones. 
Si la temperatura ingresada es inferior al cero absoluto, el programa debe mostrar un mensaje de 
advertencia.
cero absoluto:  0K = −273,15 °C o −459,67 °F.

Pueden leer aqui sobre como hacer las conversiones.
                    desde Celsius	              a Celsius
Fahrenheit	    [°F] = [°C] × ​9⁄5 + 32	       [°C] = ([°F] − 32) × ​5⁄9
Kelvin	        [K] = [°C] + 273.15	           [°C] = [K] − 273.15

@author: Madmax
"""

C= float( input("Ingrese temperatura en grados celsius: ") )

       
def Farenheit (F):
        F = C * 1.8 + 32
        return F

def Kelvin(K):
        K = C + 273.15
        return K

            if K<0 
print ("la temperatura ingresada es inferior al cero absoluto")


print (Farenheit(C))

print (Kelvin(C)) 
    