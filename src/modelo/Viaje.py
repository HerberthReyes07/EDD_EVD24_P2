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
    
    def obtener_tam_lista(self):
        
        tam: int = 0
        recorrer = self.__ruta_tomada.get_cabeza()
        
        while recorrer.get_siguiente() is not None:
            tam += 1
            recorrer = recorrer.get_siguiente()
        
        return tam + 1
    
    def obtener_tiempo_total(self):
        
        recorrer = self.__ruta_tomada.get_cabeza()
        
        while recorrer.get_siguiente() is not None:
            recorrer = recorrer.get_siguiente()
        
        return recorrer.get_valor().get_peso_acumulado()
    
    def graficar_ruta(self):
        
        config: str = (
                        'graph[rankdir="LR"]\n\t'
                        'bgcolor="#F5F5F5";\n\t'
                        'fontcolor=black;\n\t'
                        f'label="Ruta en el viaje {self.get_id()}";\n\t'
                        'labelloc="t";\n\t'
                        'nodesep=0.5;\n\t'
                        'node [fontsize = 7.5 shape=box style=filled fillcolor="#004488" '
                        'fontcolor="#F5F5F5" color=transparent];\n\t'
                        'edge [fontcolor=black color="#ff5722"];\n\t'
                    )
        
        def_nodo: str =''
        rel_nodo: str = ''
        
        recorrer = self.__ruta_tomada.get_cabeza()
        id: int = 1
        
        
        while recorrer is not None:
            
            def_nodo += 'n' + id.__str__() + '[label="'
            def_nodo += 'Lugar: ' + recorrer.get_valor().get_ciudad() + '\\n'
            
            
            if recorrer.get_valor().get_peso_acumulado() == 0:
                def_nodo += f'Tiempo: {recorrer.get_valor().get_peso()}"];\n\t'
            else:
                def_nodo += f'Tiempo: {peso} + {recorrer.get_valor().get_peso()} = {recorrer.get_valor().get_peso_acumulado()}"];\n\t'

            peso:int = recorrer.get_valor().get_peso_acumulado()
            
            if recorrer.get_siguiente() is not None:
                rel_nodo += f'n{id}-> n{(id + 1)};\n\t'
            
            id += 1
            recorrer = recorrer.get_siguiente()
        
        return 'digraph G {\n\t' + config + def_nodo + rel_nodo + '\n}'
        
    def __str__(self):
        return 'ID:' + str(self.__id) + ', Origen:' + self.__origen + ', Destino:' + self.__destino + ', Fecha:' + self.__fecha + ', Hora:' + self.__hora + ', Cliente:' + self.__cliente.get_dpi() + ', Vehiculo:' + self.__vehiculo.get_placa()