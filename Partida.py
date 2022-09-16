from VentanaDePedidoDeNombres import *
from VentanaDePedidoDeColores import *
from VentanaDeTablero import *
from Jugador import *
from Turno import *
from Tablero import *

class Partida():
    def __init__(self, jugadorUno, jugadorDos):
        self.jugadorUno = jugadorUno
        self.jugadorDos = jugadorDos
        self.turnos = []
        self.nuevoTurno()#inicio la partida en el turno 1
        self.tablero= None


    def abrirVentanaDePedidoDeNombres(self):
        VentanaDePedidoDeNombres(self)
    

    def abrirVentanaDePedidoDeColores(self):
        VentanaDePedidoDeColores(self)


    def abrirVentanaDeTablero(self):
        VentanaDeTablero(self)
    

    def nuevoTurno(self):
        Turno(self)


    def agregarTurno(self, turno):
        self.turnos.append(turno)
    

    def agregarTablero(self, tablero):
        self.tablero = tablero

    
    def turnoActual(self):
        return self.turnos[-1]
        

    def jugadorActual(self):
        if self.turnoActual().numeroDeTurno %2 != 0:
            return self.jugadorUno
        else:
            return self.jugadorDos
    

    def victoriaJugadorUno(self):
        
        if self.tablero.casillas[0].seleccionada == self.jugadorUno.color and self.tablero.casillas[1].seleccionada== self.jugadorUno.color and self.tablero.casillas[2].seleccionada== self.jugadorUno.color:
            return True #fila1
        if self.tablero.casillas[3].seleccionada == self.jugadorUno.color and self.tablero.casillas[4].seleccionada== self.jugadorUno.color and self.tablero.casillas[5].seleccionada== self.jugadorUno.color:
            return True #fila2
        if self.tablero.casillas[6].seleccionada == self.jugadorUno.color and self.tablero.casillas[7].seleccionada== self.jugadorUno.color and self.tablero.casillas[8].seleccionada== self.jugadorUno.color:
            return True #fila3
        if self.tablero.casillas[0].seleccionada == self.jugadorUno.color and self.tablero.casillas[3].seleccionada== self.jugadorUno.color and self.tablero.casillas[6].seleccionada== self.jugadorUno.color:
            return True #columna1
        if self.tablero.casillas[1].seleccionada == self.jugadorUno.color and self.tablero.casillas[4].seleccionada== self.jugadorUno.color and self.tablero.casillas[7].seleccionada== self.jugadorUno.color:
            return True #columna2
        if self.tablero.casillas[2].seleccionada == self.jugadorUno.color and self.tablero.casillas[5].seleccionada== self.jugadorUno.color and self.tablero.casillas[8].seleccionada== self.jugadorUno.color:
            return True #columna3
        if self.tablero.casillas[0].seleccionada == self.jugadorUno.color and self.tablero.casillas[4].seleccionada== self.jugadorUno.color and self.tablero.casillas[8].seleccionada== self.jugadorUno.color:
            return True
        if self.tablero.casillas[2].seleccionada == self.jugadorUno.color and self.tablero.casillas[4].seleccionada== self.jugadorUno.color and self.tablero.casillas[6].seleccionada== self.jugadorUno.color:
            return True
    
    def victoriaJugadorDos(self):
        if self.tablero.casillas[0].seleccionada == self.jugadorDos.color and self.tablero.casillas[1].seleccionada== self.jugadorDos.color and self.tablero.casillas[2].seleccionada== self.jugadorDos.color:
            return True #fila1
        if self.tablero.casillas[3].seleccionada == self.jugadorDos.color and self.tablero.casillas[4].seleccionada== self.jugadorDos.color and self.tablero.casillas[5].seleccionada== self.jugadorDos.color:
            return True #fila2
        if self.tablero.casillas[6].seleccionada == self.jugadorDos.color and self.tablero.casillas[7].seleccionada== self.jugadorDos.color and self.tablero.casillas[8].seleccionada== self.jugadorDos.color:
            return True #fila3
        if self.tablero.casillas[0].seleccionada == self.jugadorDos.color and self.tablero.casillas[3].seleccionada== self.jugadorDos.color and self.tablero.casillas[6].seleccionada== self.jugadorDos.color:
            return True #columna1
        if self.tablero.casillas[1].seleccionada == self.jugadorDos.color and self.tablero.casillas[4].seleccionada== self.jugadorDos.color and self.tablero.casillas[7].seleccionada== self.jugadorDos.color:
            return True #columna2
        if self.tablero.casillas[2].seleccionada == self.jugadorDos.color and self.tablero.casillas[5].seleccionada== self.jugadorDos.color and self.tablero.casillas[8].seleccionada== self.jugadorDos.color:
            return True #columna3
        if self.tablero.casillas[0].seleccionada == self.jugadorDos.color and self.tablero.casillas[4].seleccionada== self.jugadorDos.color and self.tablero.casillas[8].seleccionada== self.jugadorDos.color:
            return True #diagonal1
        if self.tablero.casillas[2].seleccionada == self.jugadorDos.color and self.tablero.casillas[4].seleccionada== self.jugadorDos.color and self.tablero.casillas[6].seleccionada== self.jugadorDos.color:
            return True #diagonal2
    

    def felicitarAlGanador(self):
        if self.victoriaJugadorUno():
            Label(text="Felicitaciones" + self.jugadorUno.nombre + " sos el ganador!")
            Label(text= self.jugadorDos.nombre + ", hay que ser mamerto para perder en el TATETI eh... XD")
        elif self.victoriaJugadorDos():
            Label(text="Felicitaciones" + self.jugadorDos.nombre + " sos el ganador!")
            Label(text= self.jugadorUno.nombre + ", hay que ser mamerto para perder en el TATETI eh... XD")
    

    def chequearVentanaDePedidoDeNombres(self):
        if self.jugadorUno.nombre == None or self.jugadorDos.nombre == None:
            print("No se cargaron correctamente los nombres de los jugadores.")
            time.sleep(1)
            exit()
    

    def chequearVentanaDePedidoDeColores(self):
        if self.jugadorUno.color == None or self.jugadorDos.color == None:
            print("No se cargaron correctamente los colores de los jugadores.")
            time.sleep(1)
            exit()



    
    
    


        