#!/usr/bin/env python

class Perro():
    def caminar(self):
        print("Camina en 4 patas")

class Pato():
    def caminar(self):
        print("Camino en 2 patas o vuelo!")

class Caracol():
    def arrastrar(self):
        print("yo me arrasssstro")

def mover(animal):
    animal.caminar()

firulais =Perro()

donald =Pato()

gary =Caracol()

firulais.caminar()
donald.caminar()
gary.arrastrar()

mover(firulais)
mover(donald)
mover(gary)