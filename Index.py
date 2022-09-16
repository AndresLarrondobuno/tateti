from Partida import *
from Jugador import *
import time


###

partida = Partida(Jugador(1), Jugador(2))

partida.abrirVentanaDePedidoDeNombres()
partida.chequearVentanaDePedidoDeNombres()#chequeo que los atributos 'nombre' hayan sido seteados previo a pasar a la siguiente ventana
time.sleep(1)
partida.abrirVentanaDePedidoDeColores()
partida.chequearVentanaDePedidoDeColores()#chequeo que los atributos 'color' hayan sido seteados previo a pasar a la siguiente ventana
time.sleep(1)
partida.abrirVentanaDeTablero()










