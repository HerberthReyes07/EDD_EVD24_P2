


class NodoLS:
    
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None
    
    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor
    
    def get_siguiente(self):
        return self.__siguiente
    
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente