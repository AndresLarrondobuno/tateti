from tkinter import *

class VentanaDePedidoDeColores(Tk):
    def __init__(self, partida):
        super().__init__()
        self.partida = partida

        self.marcoDeBotonesJugadorUno = Frame(self, pady=15)

        self.etiquetaEleccionDeColorJugadorUno = Label(self.marcoDeBotonesJugadorUno, text= self.partida.jugadorUno.nombre + ",elegi tu color:")
        self.etiquetaEleccionDeColorJugadorUno.grid(row=0, column=0)
        self.botonAzulJugadorUno = Button(self.marcoDeBotonesJugadorUno, bg="blue", padx=45, command=self.elegirColorAzulJugadorUno)
        self.botonAzulJugadorUno.grid(row=0, column=1)
        self.botonRojoJugadorUno = Button(self.marcoDeBotonesJugadorUno, bg="red", padx=45, command=self.elegirColorRojoJugadorUno)
        self.botonRojoJugadorUno.grid(row=0, column=2)

        self.marcoDeBotonesJugadorUno.pack()

        self.marcoDeBotonesJugadorDos = Frame(self, pady=15)

        self.etiquetaEleccionDeColorJugadorDos = Label(self.marcoDeBotonesJugadorDos, text= self.partida.jugadorDos.nombre + ",elegi tu color:")
        self.etiquetaEleccionDeColorJugadorDos.grid(row=1, column=0)
        self.botonAzulJugadorDos = Button(self.marcoDeBotonesJugadorDos, bg="blue", padx=45, command=self.elegirColorAzulJugadorDos)
        self.botonAzulJugadorDos.grid(row=1, column=1)
        self.botonRojoJugadorDos = Button(self.marcoDeBotonesJugadorDos, bg="red", padx=45, command=self.elegirColorRojoJugadorDos)
        self.botonRojoJugadorDos.grid(row=1, column=2)
        
        self.marcoDeBotonesJugadorDos.pack()


        self.mainloop()
    

    def elegirColorRojoJugadorUno(self):
        self.partida.jugadorUno.color = 'red'
        self.botonRojoJugadorUno['state'], self.botonRojoJugadorUno['bg'] = 'disabled', 'white'
        self.botonAzulJugadorUno['state'], self.botonAzulJugadorUno['bg'] = 'disabled', 'white'
        self.botonRojoJugadorDos['state'], self.botonRojoJugadorDos['bg'] = 'disabled', 'white'
        if self.partida.jugadorUno.color != None and self.partida.jugadorDos.color != None:
            self.destroy()

    def elegirColorAzulJugadorUno(self):
        self.partida.jugadorUno.color = 'blue'
        self.botonAzulJugadorUno['state'], self.botonAzulJugadorUno['bg'] = 'disabled', 'white'
        self.botonRojoJugadorUno['state'], self.botonRojoJugadorUno['bg'] = 'disabled', 'white'
        self.botonAzulJugadorDos['state'], self.botonAzulJugadorDos['bg'] = 'disabled', 'white'
        if self.partida.jugadorUno.color != None and self.partida.jugadorDos.color != None:
            self.destroy()

    def elegirColorRojoJugadorDos(self):
        self.partida.jugadorDos.color = 'red'
        self.botonRojoJugadorDos['state'], self.botonRojoJugadorDos['bg'] = 'disabled', 'white'
        self.botonAzulJugadorDos['state'], self.botonAzulJugadorDos['bg'] = 'disabled', 'white'
        self.botonRojoJugadorUno['state'], self.botonRojoJugadorUno['bg'] = 'disabled', 'white'
        if self.partida.jugadorUno.color != None and self.partida.jugadorDos.color != None:
            self.destroy()

    def elegirColorAzulJugadorDos(self):
        self.partida.jugadorDos.color = 'blue'
        self.botonAzulJugadorDos['state'], self.botonAzulJugadorDos['bg'] = 'disabled', 'white'
        self.botonRojoJugadorDos['state'], self.botonRojoJugadorDos['bg'] = 'disabled', 'white'
        self.botonAzulJugadorUno['state'], self.botonAzulJugadorUno['bg'] = 'disabled', 'white'
        if self.partida.jugadorUno.color != None and self.partida.jugadorDos.color != None:
            self.destroy()

    
        


