class Cliente:

    def __init__(self, dpi:int, nombres:str, apellidos:str, genero:chr, telefono:int, direccion:str):
        self.__dpi = dpi
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__genero = genero
        self.__telefono = telefono
        self.__direccion = direccion

    # Getters
    def get_dpi(self) -> int:
        return self.__dpi

    def get_nombres(self) -> str:
        return self.__nombres

    def get_apellidos(self) -> str:
        return self.__apellidos

    def get_genero(self) -> chr:
        return self.__genero

    def get_telefono(self) -> int:
        return self.__telefono

    def get_direccion(self) -> str:
        return self.__direccion

    # Setters
    def set_dpi(self, dpi: int):
        self.__dpi = dpi

    def set_nombres(self, nombres: str):
        self.__nombres = nombres

    def set_apellidos(self, apellidos: str):
        self.__apellidos = apellidos

    def set_genero(self, genero: chr):
        self.__genero = genero

    def set_telefono(self, telefono: int):
        self.__telefono = telefono

    def set_direccion(self, direccion: str):
        self.__direccion = direccion
    
    def __str__(self) -> str:
        return (f'DPI:{self.__dpi}, Nombre:{self.__nombres}, Apellidos:{self.__apellidos}, Genero:{self.__genero}, Tel:{self.__telefono}, Dir:{self.__direccion}')