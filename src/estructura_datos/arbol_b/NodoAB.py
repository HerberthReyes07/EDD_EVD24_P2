from src.modelo.Vehiculo import Vehiculo


class NodoAB:
    def __init__(self, hoja: bool = False):
        self.__hoja: bool = hoja
        self.__claves: list[Vehiculo] = []
        self.__hijos: list[NodoAB] = []
    
    def get_hoja(self) -> bool:
        return self.__hoja
    
    def set_hoja(self, hoja: bool):
        self.__hoja = hoja
        
    def get_claves(self) -> list[Vehiculo]:
        return self.__claves
    
    def set_claves(self, claves: list[Vehiculo]):
        self.__claves = claves
        
    def get_hijos(self) -> list['NodoAB']:
        return self.__hijos
    
    def set_hijos(self, hijos: list['NodoAB']):
        self.__hijos = hijos