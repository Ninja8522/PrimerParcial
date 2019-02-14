#!/usr/bin/env python

texto1, texto2 = "hola mundo", "que rollo"

texto12 = 12

print(texto12)

textoMultilinea ="""Esto es un texto
multilinea
y puede manejar un texto largo, en parrafos
sin necesidad de usar saltos de linea"""

print(textoMultilinea)

nombre ="Cesar"
apellido ="Perez"
edad = 20

print("hola {1} {0} y tienes {2}".format(nombre, apellido,edad))

nombreCompleto = f"hola {nombre} {apellido} tienes {edad} años"

contador = 0

while(contador<=3):
    print(contador)
    contador+=1

for numero in range(3):
    print(numero+1)
    if numero == 2:
        print("Fin del ciclo")
    else:
        print("todavia no")

print(nombreCompleto)