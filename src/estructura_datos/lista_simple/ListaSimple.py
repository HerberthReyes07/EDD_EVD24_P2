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
            
    def buscar_ciudad(self, valor: str):
        aux = self.__cabeza
        while aux is not None:
            if aux.get_valor().get_ciudad() == valor:
                return aux.get_valor()
            aux = aux.get_siguiente()
        return None
    
    def esta_vacia(self) -> bool:
        return self.__cabeza is None
        
    def imprimir(self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.get_valor())
            aux = aux.get_siguiente()