from tkinter import *
from Casilla import *
from Tablero import *
import time

class VentanaDeTablero(Tk):
    def __init__(self, partida):
        super().__init__()

        self.partida = partida
        self.botones = []
        self.crearCasillas()
        self.vincularBotones()

        
        
        self.mainloop()


    def crearCasillas(self):
        fila = 0
        columna = 0
        casillas = []
        
        for numeroDeCasilla in range(0, 9):
            casilla = Casilla(numeroDeCasilla)
            casilla.fila = fila
            casilla.columna = columna
            casillas.append(casilla)
            
            if numeroDeCasilla in range(0,3):
                columna += 1
                if numeroDeCasilla == 2:
                    columna -= 3
                    fila += 1

            elif numeroDeCasilla in range(3,6):
                columna += 1
                if numeroDeCasilla == 5:
                    columna -= 3
                    fila += 1

            elif numeroDeCasilla in range(6,9):
                columna += 1

        for casilla in casillas:
            boton = Button(self, padx=60, pady=50, bg='white', fg='green', text=casilla.numeroDeCasilla)
            boton.grid(row=casilla.fila, column=casilla.columna)
            self.botones.append(boton) #administrador que comunique casillas de back con casillas visuales, meto un objeto intermediario para comunciarlos

        self.partida.agregarTablero(Tablero(casillas))


    def vincularBoton(self, boton):
        boton['command'] = lambda: self.elegirCasilla(boton)
    '''tuve que separar el bucle de esta funcion, sino la funcion elegirCasilla solo operaba en la 8 (?)
    def vincularBotones(self,boton):
        for boton in self.botones:
            boton['command'] = lambda: self.elegirCasilla(boton)'''

    def vincularBotones(self):
        for boton in self.botones:
            self.vincularBoton(boton)
            

    def elegirCasilla(self, boton):
        jugadorActual = self.partida.jugadorActual()
        numeroDeBoton = int(boton['text'])

        boton['bg'], boton['state'] = jugadorActual.color, 'disabled'
        self.partida.tablero.casillas[numeroDeBoton].seleccionada = jugadorActual.color
        self.partida.nuevoTurno()

        if self.partida.victoriaJugadorUno() or self.partida.victoriaJugadorDos():
            time.sleep(1)
            self.destroy()


        

        

    

    