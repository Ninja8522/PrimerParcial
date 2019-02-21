#!/usr/bin/env python

class Persona:

    def __init__ (self,altura=1.82,nombre="juan perez"): 
        self.altura = altura
        self.nombre = nombre
    def saludo(self,mensaje):
        print(mensaje)

max_ =Persona()

max_.saludo("hola, buenos dias")

print(max_.nombre)

print(max_.altura)

max_.nombre ="Daniel"

print(max_.nombre)

max_.apellido ="Perez"

print(max_.apellido)

Persona(1.70,"Cesar")
