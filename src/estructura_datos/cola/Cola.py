from src.estructura_datos.cola.NodoC import NodoC
from src.estructura_datos.grafo.Vertice import Vertice

class Cola:
    
    def __init__(self):
        self.__cabeza = None

    def get_cabeza(self):
        return self.__cabeza
    
    def set_cabeza(self, cabeza):
        self.__cabeza = cabeza
        
        
    def encolar(self, valor):
        nuevo = NodoC(valor)
        if self.__cabeza is None:
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            while aux.get_siguiente() is not None:
                aux = aux.get_siguiente()
            aux.set_siguiente(nuevo)    
    
    
    def desencolar(self) -> NodoC:
        if self.__cabeza is None:
            return None
        else:
            aux = self.__cabeza
            self.__cabeza = aux.get_siguiente()
            return aux
        
    def ordenar(self):
        
        if self.__cabeza is None:
            print("La cola esta vacia")
            return
        
        current: NodoC[Vertice] = self.__cabeza
        
        while current is not None:
            next: NodoC[Vertice] = current.get_siguiente()
            
            while next is not None:
                if current.get_valor().get_peso_acumulado() > next.get_valor().get_peso_acumulado():
                    temp = current.get_valor()
                    current.set_valor(next.get_valor())
                    next.set_valor(temp)
                next = next.get_siguiente()
            
            current = current.get_siguiente()
        
    def buscar(self, valor) -> NodoC:
        if self.__cabeza is None:
            return None
        else:
            aux = self.__cabeza
            while aux is not None:
                if aux.get_valor() == valor:
                    return aux
                aux = aux.get_siguiente()
            return None 
     
        
    def esta_vacia(self):
        return self.__cabeza is None