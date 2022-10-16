# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:12:04 2020
Trabajo Práctico Integrador : Python
Realizar un script en Python para simular un juego de dados, según las siguientes
condiciones:
➢ El juego consistirá en lanzar dos dados. Para simularlo, debemos
obtener dos números aleatorios entre 1 y 6.
➢ Si la suma de los dos dados es 4, el participante gana la mano
➢ Si la suma de los dos dados es menor a 4, el participante pierde y se
termina el juego.
Realizar los comentarios pertinentes en el código para que seentienda la lógica
utilizada.
Mostrar la suma de los números por pantalla y pedirle al usuario que toque una tecla
para volver a lanzar los dados.

@author: Madmax
"""

import random
resultado = 0
Inicio = input("presiona enter para comenzar a jugar :" )  #comenzamos el juego dando enter
def Dos_dados():   #funcion dos dados 
     resultado = 1  #le damos un numero para empezar 
     while resultado < 4 :   #Mientras el resultado sea menor a 4 seguir tirando los dados
         dado1 = random.randint(1,6)  #primer dado usando Random de 1 a 6
         dado2 = random.randint(1,6) #segundo dado usando Random de 1 a 6
         resultado = dado1 + dado2  #El resultado consiste en la suma de los dos dados
         print("El dado 1 cayo en el numero: ",dado1) #Muestro en pantalla lo que dio el primer dado
         print("El dado 2 cayo en el numero: ",dado2)#Muestro en pantalla lo que dio el Segundo dado
         if resultado  == 4 : # uso control de flujo if para evaluar si es igual a 4 
            print ("El resultado es:", resultado, "Ganaste!") #En caso que sea igual a 4 informar que el participante gano
         elif resultado < 4: # uso control de flujo if para evaluar si es menor a 4 
            print ("El resultado es:", resultado, "Perdiste!") # En caso que si informar al participante qu perdio
         else: #en caso que sea mayor que 4 
             print("el resultado es: ",resultado)#informar el resultado
             pregunta = input("para lanzar los dados una vez mas presiona la tecla j luego enter :" )#pide presionar j para  poder lanzar de nuevo los dados
             if  pregunta == "j" :#Si es presionada la letra j y enter entonces vuelve a tirar los dados
                     print ("volvemos a tirar los dados:") #avisa que se vuelven a tirar
                     resultado = 1  #se pone a 1 la variable resultado
Dos_dados()
