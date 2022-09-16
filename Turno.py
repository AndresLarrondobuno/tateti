class Turno:
    def __init__(self, partida):
        self.numeroDeTurno = len(partida.turnos) + 1
        partida.agregarTurno(self)

