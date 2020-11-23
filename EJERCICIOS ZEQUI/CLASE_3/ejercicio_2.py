# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 08:34:47 2020
2. Una empresa de RRHH desea contar con un programa en
una terminal para que el Agente encargado de la
selección pueda comenzar a cargar los potenciales
candidatos a un puesto. El usuario deberá contestar
algunas preguntas sobre el postulante, y el programa
deberá entregar un resultado final: “Sí, [nombre] es apto”
o bien “No, [nombre] no es apto”. Para quedar
1preseleccionado, un candidato deberá ser mayor de 21
años. Además, deberá ser graduado de Ingeniería en
Sistemas, o bien ser estudiante en el área con dos años
de experiencia en puestos similares. Es importante, para
ahorrar tiempo al Agente, que se le pida ingresar el
mínimo posible de datos sobre el candidato, evitando
tener que cargar más detalles cuando el postulante ya
quedaría descartado para esta búsqueda.

@author: Madmax
"""
nombre= input(" por favor ingresar el nombre del candidato: ")
print ("cuantos años tiene ", nombre, "?")
edad = int(input())
if edad >=21:
    print ("presiona a si es estudiante o graduado de Ingeniería en Sistemas", nombre)
    que = input ()  
    que == "a"
    print ("si,", nombre , "es apto")  #se asume que no miente  
else:
        print ("NO,", nombre , "no es apto")