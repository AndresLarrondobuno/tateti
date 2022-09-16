from tkinter import *

class VentanaDePedidoDeNombres(Tk):
    
    def __init__(self, partida):
        super().__init__()

        self.partida = partida #???
        

        self.bienvenida = Label(self, text="Bienvenido a mi TATETI")
        self.bienvenida.grid(row=0, columnspan=3)

        self.etiquetaNombreJugadorUno = Label(self, text="Ingresa tu nombre (Jugador 1):")
        self.etiquetaNombreJugadorUno.grid(row=1, column=0)
        self.nombreJugadorUno = Entry(self)
        self.nombreJugadorUno.grid(row=1, column=1)
        self.botonAceptarNombreJugadorUno = Button(self, text="Aceptar", command= lambda: self.asignarNombreAJugadorUno(self.partida, self.nombreJugadorUno.get()))
        self.botonAceptarNombreJugadorUno.grid(row=2, column=1)

        self.etiquetaNombreJugadorDos = Label(self, text="Ingresa tu nombre (Jugador 2):")
        self.etiquetaNombreJugadorDos.grid(row=3, column=0)
        self.nombreJugadorDos = Entry(self)
        self.nombreJugadorDos.grid(row=4, column=1)
        self.botonAceptarNombreJugadorDos = Button(self, text="Aceptar", command= lambda: self.asignarNombreAJugadorDos(self.partida, self.nombreJugadorDos.get()))
        self.botonAceptarNombreJugadorDos.grid(row=5, column=1)



        self.mainloop()


    #MÉTODOS
    def asignarNombreAJugadorUno(self, partida, nombreDeJugador):
        if len(nombreDeJugador) == 0 or (nombreDeJugador == partida.jugadorDos.nombre and nombreDeJugador == partida.jugadorDos.nombre != None):
            return
        partida.jugadorUno.nombre = nombreDeJugador
        self.botonAceptarNombreJugadorUno['state'] = 'disabled'
        if self.partida.jugadorDos.nombre != None:
            self.destroy()
        
        
    def asignarNombreAJugadorDos(self, partida, nombreDeJugador):
        if len(nombreDeJugador) == 0 or (nombreDeJugador == partida.jugadorUno.nombre and nombreDeJugador == partida.jugadorUno.nombre != None):
            return
        partida.jugadorDos.nombre = nombreDeJugador
        self.botonAceptarNombreJugadorDos['state'] = 'disabled'
        if self.partida.jugadorUno.nombre != None:
            self.destroy()
        
            

    



    
    




        








