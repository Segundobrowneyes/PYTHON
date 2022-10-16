# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:12:53 2020
3. Crear una versión del típico juego infantil “Juguemos en el bosque,
mientras el Lobo no está. ¿Lobo está?” El usuario deberá
contestar simplemente “SI/NO”. Al estar listo el programa deberá
informarle: “¡A cazar!
CANCION:
Jugemos en el bosque
Mientras el lobo no está
Jugemos en el bosque
Mientras el lobo no está
¿Lobo estás?
Me estoy poniendo los pantalones!
Jugemos en el bosque
Mientras el lobo no está
Jugemos en el bosque
Mientras el lobo no está
¿Lobo estás?
Me estoy poniendo el chaleco!
Jugemos en el bosque
Mientras el lobo no está
Jugemos en el bosque
Mientras el lobo no está
¿Lobo estás?
Me estoy poniendo el saco!
Jugemos en el bosque
Mientras el lobo no está
Jugemos en el bosque
Mientras el lobo no está
¿Lobo estás?
Me estoy poniendo el sombrerito!
Jugemos en el bosque
Mientras el lobo no está
Jugemos en el bosque
Mientras el lobo no está
¿Lobo estás?
Si, y ya salgo para comermelos!
@author: Madmax
"""
pregunta = int
esta = int
pregunta = input("Jugemos en el bosque Mientras el lobo no está Jugemos en el bosque Mientras el lobo no está ")
while not esta:
   if pregunta =="NO":
  print("NO, y ya salgo para comermelos!")
       else:
        esta=True
        print("Si, y ya salgo para comermelos!")
