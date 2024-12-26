from src.estructura_datos.lista_simple.ListaSimple import ListaSimple


class Vertice:
    def __init__(self, ciudad: str, peso: int = 0):
        self.__ciudad = ciudad
        self.__peso = peso
        self.__vecinos = ListaSimple()
    
    def get_ciudad(self):
        return self.__ciudad
    
    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad
        
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso
        
    def get_vecinos(self):
        return self.__vecinos
    
    def set_vecinos(self, vecinos):
        self.__vecinos = vecinos