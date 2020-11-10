# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:40:41 2020

@author: Madmax
"""
"""
### Mini-desafío funciones
Escribir una función que chequee los siguientes usuarios y contraseñas:
*  Usuario: Juan  -  Contraseña: 12345_
*  Usuario: Pablo - Contraseña: xDcFvGbHn

La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.
"""
def main ():
                usuario (input("Ingrese su usuario: "))
                if usuario == "Juan" or  usuario== "Pablo" :
                login(usuario, contraseña)

def login(usuario, contraseña):
  if (usuario == 'Juan' and contraseña == '12345_') or \
  (usuario == 'Pablo' and contraseña == 'xDcFvGbHn'):
    return True
  else:
    return False

