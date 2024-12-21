from src.modelo.Cliente import Cliente


class NodoLCDE:
    def __init__(self, cliente: Cliente):
        self.__cliente = cliente
        self.__siguiente = None
        self.__anterior = None

    # Getters
    def get_cliente(self):
        return self.__cliente

    def get_siguiente(self):
        return self.__siguiente

    def get_anterior(self):
        return self.__anterior

    # Setters
    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def set_anterior(self, anterior):
        self.__anterior = anterior