class Ruta:
    def __init__(self, origen: str, destino: str, tiempo: int):
        self.__origen = origen
        self.__destino = destino
        self.__tiempo = tiempo

    # Getters
    def get_origen(self) -> str:
        return self.__origen

    def get_destino(self) -> str:
        return self.__destino

    def get_tiempo(self) -> int:
        return self.__tiempo

    # Setters
    def set_origen(self, origen: str):
        self.__origen = origen

    def set_destino(self, destino: str):
        self.__destino = destino

    def set_tiempo(self, tiempo: int):
        self.__tiempo = tiempo

    def __str__(self) -> str:
        return f'Origen:{self.__origen}, Destino:{self.__destino}, Tiempo:{self.__tiempo}'