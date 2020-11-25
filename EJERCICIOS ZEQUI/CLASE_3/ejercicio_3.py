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
