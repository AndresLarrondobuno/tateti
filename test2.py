from tkinter import *

class Rectangulo:
    def __init__(self, largo, ancho, nombre):
        self.largo = largo
        self.ancho = ancho
        self.nombre = nombre

    def mostrarDimensiones(self):
        print("largo:", str(self.largo), "/ ancho:", str(self.ancho))
    
    def mostrarArea(self): 
        print("El area del", self.nombre, "es:", str(self.largo*self.ancho))


class Cuadrado(Rectangulo):
    def __init__(self, largo, ancho, nombre):
        super().__init__(largo, ancho, nombre)


class Cubo(Rectangulo):
    def __init__(self, largo, ancho, alto, nombre):
        super().__init__(largo, ancho, nombre)
        self.alto = alto
    
    def mostrarVolumen(self):
        print("El volumen del",self.nombre, "es:" , self.largo*self.ancho*self.alto)




rectangulo = Rectangulo(4, 2, 'rectangulito')
rectangulo.mostrarArea()

cuadrado = Cuadrado(5, 3, 'cuadradito')
cuadrado.mostrarArea()

cubo = Cubo(3, 3, 3, 'cubito')
cubo.mostrarVolumen()