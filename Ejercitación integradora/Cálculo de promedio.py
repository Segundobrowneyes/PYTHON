# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 07:35:13 2020
Cálcular la nota de un alumno es una tarea cotidiana de un profesor. Esta tarea suele realizarse a mano o en excel muchas veces. En esta ocasión la haremos en python.

Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.
Reescribir la función anterior modificandola para asignar una importancia al primer examen de 20%, 
al segundo de 50% y al tercero de 30%.
Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción if, 
si el alumno aprobó en cada caso (suponga que 4 es la nota de aprobación).

@author: Madmax
"""
"""

nota = int( input('Ingrese un número del 1 al 10: ') )

while nota < 1 or nota > 10:
  print('Fuera de rango!')
  nota = int( input('Ingrese un número del 1 al 10: ') )

print( nota >= 4 )

"""

#Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.

def nota(a,b,c):
    s = (a+b+c)/3
    return s
nota1= int( input('Ingrese primera nota del 1 al 10: ') )
nota2= int( input('Ingrese segunda nota del 1 al 10: ') )
nota3= int( input('Ingrese tercera nota 1 al 10: ') )
z = nota(nota1,nota2,nota3)
print(z)


