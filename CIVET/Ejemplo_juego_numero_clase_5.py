# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:04:53 2020
ejemplo final clase 5
@author: Madmax
"""

import random
def generaNumeroAleatorio(minimo, maximo):
    return random.randint (minimo, maximo)
numero_buscado=generaNumeroAleatorio(1,10)
encontrado=False
intentos=0
while not encontrado:
    numero_usuario=int(input("Introduce el numero buscado: "))
    if numero_usuario>numero_buscado:
        print("El numero que buscas es menor")
        intentos=intentos+1
    elif numero_usuario<numero_buscado:
        print("El numero que buscas es mayor")
        intentos=intentos+1
    else:
        encontrado=True
print("Has acertado, el numero correcto es ", numero_usuario, "te ha llevado",
intentos, "intentos")
