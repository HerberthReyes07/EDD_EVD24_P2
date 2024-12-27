from src.estructura_datos.lista_simple.ListaSimple import ListaSimple
from src.modelo.Cliente import Cliente
from src.modelo.Vehiculo import Vehiculo


class Viaje:
    
    def __init__(self, origen: str, destino: str, fecha: str, hora: str, cliente: Cliente, vehiculo: Vehiculo):
        self.__id = 0
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__hora = hora
        self.__cliente = cliente
        self.__vehiculo = vehiculo
        self.__ruta_tomada = ListaSimple()

    # Getters
    def get_id(self):
        return self.__id

    def get_origen(self):
        return self.__origen

    def get_destino(self):
        return self.__destino

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora

    def get_cliente(self):
        return self.__cliente

    def get_vehiculo(self):
        return self.__vehiculo
    
    def get_ruta_tomada(self):
        return self.__ruta_tomada

    # Setters
    def set_id(self, id: int):
        self.__id = id

    def set_origen(self, origen: str):
        self.__origen = origen

    def set_destino(self, destino: str):
        self.__destino = destino

    def set_fecha(self, fecha: str):
        self.__fecha = fecha

    def set_hora(self, hora: str):
        self.__hora = hora

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo
    
    def set_ruta_tomada(self, ruta_tomada: ListaSimple):
        self.__ruta_tomada = ruta_tomada
        
    def __str__(self):
        return 'ID:' + str(self.__id) + ', Origen:' + self.__origen + ', Destino:' + self.__destino + ', Fecha:' + self.__fecha + ', Hora:' + self.__hora + ', Cliente:' + self.__cliente.get_dpi() + ', Vehiculo:' + self.__vehiculo.get_placa()