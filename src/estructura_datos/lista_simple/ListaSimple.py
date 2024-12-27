#from src.estructura_datos.grafo.Vertice import Vertice
from src.estructura_datos.lista_simple.NodoLS import NodoLS


class ListaSimple:
    
    def __init__(self):
        self.__cabeza = None
        
    def get_cabeza(self):
        return self.__cabeza
    
    def set_cabeza(self, cabeza):
        self.__cabeza = cabeza
    
    def insertar(self, valor):
        
        nuevo = NodoLS(valor)
        
        if self.__cabeza is None:
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            while aux.get_siguiente() is not None:
                aux = aux.get_siguiente()
            aux.set_siguiente(nuevo)
            
    def insertar_viaje(self, valor):
        nuevo = NodoLS(valor)
        
        if self.__cabeza is None:
            valor.set_id(1)
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            while aux.get_siguiente() is not None:
                aux = aux.get_siguiente()
                
            valor.set_id(aux.get_valor().get_id() + 1)
            aux.set_siguiente(nuevo)
            
    def buscar_ciudad(self, valor: str):
        aux = self.__cabeza
        while aux is not None:
            if aux.get_valor().get_ciudad() == valor:
                return aux.get_valor()
            aux = aux.get_siguiente()
        return None
    
    def esta_vacia(self) -> bool:
        return self.__cabeza is None
    
    def graficar_viajes(self) -> str:
        
        config: str = (
                        'graph[rankdir="LR"]\n\t'
                        'bgcolor="#F5F5F5";\n\t'
                        'fontcolor=black;\n\t'
                        'label="Viajes";\n\t'
                        'labelloc="t";\n\t'
                        'nodesep=0.5;\n\t'
                        'node [fontsize = 4.5 shape=box style=filled fillcolor="#004488" '
                        'fontcolor="#F5F5F5" color=transparent];\n\t'
                        'edge [fontcolor=white color="#ff5722"];\n\t'
                    )
        
        def_nodo: str =''
        rel_nodo: str = ''
        
        recorrer = self.__cabeza
        
        while recorrer is not None:
            def_nodo += 'n' + recorrer.get_valor().get_id().__str__() + '[label="'
            def_nodo += 'ID: ' + recorrer.get_valor().get_id().__str__() + '\\n'
            def_nodo += 'Cliente: ' + recorrer.get_valor().get_cliente().get_nombres() + ' ' + recorrer.get_valor().get_cliente().get_apellidos() + '\\n'
            def_nodo += 'Vehiculo: ' + recorrer.get_valor().get_vehiculo().get_marca() + ' ' + recorrer.get_valor().get_vehiculo().get_modelo() + '\\n'
            def_nodo += 'Fecha: ' + recorrer.get_valor().get_fecha() + '\\n'
            def_nodo += 'Hora: ' + recorrer.get_valor().get_hora() + '"];\n\t'
            
            
            if recorrer.get_siguiente() is not None:
                rel_nodo += 'n' + recorrer.get_valor().get_id().__str__() + ' -> n' + recorrer.get_siguiente().get_valor().get_id().__str__() + ';\n\t'
            
            recorrer = recorrer.get_siguiente()
        
        return 'digraph G {\n\t' + config + def_nodo + rel_nodo + '\n}'    
        
    def imprimir(self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.get_valor())
            aux = aux.get_siguiente()