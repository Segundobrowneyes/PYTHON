# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:38:11 2020
CONDICIONALES
1. Crear un programa para la admisión a una conferencia de
“Jóvenes mujeres emprendedoras”. Al iniciar, se deberá
preguntar al usuario su nombre. A partir de ese punto,
todos los mensajes deberán estar “personalizados”,
incluyendo el nombre del usuario en las preguntas o
solicitudes.
Para poder participar de la conferencia se deben cumplir
ciertos requisitos. En primer lugar, se puede participar
como expositor o como asistente. Si el usuario participará
como expositor, se asumirá que no miente, y se le dará la
bienvenida. Si desea participar como asistente, se le
deberá preguntar la edad y el género. Sólo podrán asistir
mujeres de entre 16 y 15 años de edad.
Crear las estructuras condicionales necesarias para que
todos los casos posibles estén contemplados, con sus
repsectivos mensajes al usuario. Es importante evitar
solicitar información que no es estrictamente necesaria
para cada “etapa” del programa.
@author: Madmax
"""

nombre= input(" ingresa tu nombre por favor: ")
print ("presiona a si sos asistente  o e si sos Expositor", nombre)
que = input ()
if  que == "e":
    print ("bienvenido a la conferencia", nombre , "")  #se asume que no miente
elif que == "a":
    print ("cuantos años tenes", nombre , "?")
    edad = int(input())
if edad == 16 or edad == 15 :
    print ("con que genero te identifcas", nombre , "?")
    gnero= input("presiona f para fememino o m para masculino:") 
    if gnero == "f":
         print ("", nombre, "podes ingresar")
    elif gnero == "m":
         print("Lo siento", nombre , "no podes entrar")
else:
    print("Lo siento", nombre , "no podes entrar")
    
    