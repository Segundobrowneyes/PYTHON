# -*- coding: utf-8 -*-
"""
Implementar un programa que muestre la siguiente secuencia:

1, 2, 3, 4, 5, 4, 3, 2, 1, 0

Para un desafío mayor: Utilizar un solo while, un solo if y un solo else
"""
x = 0
while x <= 10:
    x += 1
    if x<=5:#si es menos o igual cinco imprime el  numero
            print(x)
    else:
         print (11-x) #si no, 10 menos el numero     

