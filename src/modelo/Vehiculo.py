class Vehiculo:
    def __init__(self, placa: str, marca: str, modelo: str, precio: float):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Getters
    def get_placa(self) -> str:
        return self.__placa

    def get_marca(self) -> str:
        return self.__marca

    def get_modelo(self) -> str:
        return self.__modelo

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_placa(self, placa: str):
        self.__placa = placa

    def set_marca(self, marca: str):
        self.__marca = marca

    def set_modelo(self, modelo: str):
        self.__modelo = modelo

    def set_precio(self, precio: float):
        self.__precio = precio

    def __str__(self):
        return f'Placa:{self.__placa}, Marca:{self.__marca}, Modelo:{self.__modelo}, Precio:{self.__precio}'