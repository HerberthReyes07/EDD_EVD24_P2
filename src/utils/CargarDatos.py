from src.estructura_datos.arbol_b.ArbolB import ArbolB
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble
from src.modelo.Ruta import Ruta
from src.modelo.Vehiculo import Vehiculo
from src.modelo.Cliente import Cliente


class CargarDatos:

    def cargar_clientes(self, ruta: str, lista: ListaCircularDoble):

        archivo = open(ruta, 'r')
        clientes = archivo.read().split(';')
        clientes.pop(-1)
        cont: int = 0

        #lista: ListaCircularDoble = ListaCircularDoble()

        for cliente_aux in clientes:
            cont += 1
            #print(f'\n------ Cliente #{cont} ------')
            dato = cliente_aux.split(',')

            if len(dato) != 6:
                print(f'Error en la estructura del cliente {cont}')
                continue

            cliente = Cliente(int(dato[0]), dato[1][1:], dato[2][1:], dato[3][1], int(dato[4][1:]), dato[5][1:])
            #print(cliente)
            lista.insertar(cliente)
        
        archivo.close()

        #print(lista.mostrar_estructura())


    def cargar_vehiculos(self, ruta: str, arbolB: ArbolB):
        archivo = open(ruta, 'r')
        vehiculos = archivo.read().split(';')
        vehiculos.pop(-1)
        cont: int = 0

        for vehiculo_aux in vehiculos:
            cont += 1
            #print(f'\n------ Vehiculo #{cont} ------')
            dato = vehiculo_aux.split(':')

            if len(dato) != 4:
                print(f'Error en la estructura del vehiculo {cont}')
                continue

            vehiculo = Vehiculo(dato[0][:-1].replace("\n", ""), dato[1][1:-1], dato[2][1:-1], float(dato[3][1:]))
            #print(vehiculo)
            arbolB.insertar_vehiculo(vehiculo)

        archivo.close()

    def cargar_rutas(self, ruta_a: str):
        archivo = open(ruta_a, 'r')
        rutas = archivo.read().split('%')
        rutas.pop(-1)
        cont: int = 0

        for ruta_aux in rutas:
            cont += 1
            print(f'\n------ Ruta #{cont} ------')
            dato = ruta_aux.split('/')

            if len(dato) != 3:
                print(f'Error en la estructura de la ruta {cont}')
                continue

            ruta = Ruta(dato[0][:-1].replace("\n", ""), dato[1][1:-1], int(dato[2][1:-1]))
            print(ruta)

        archivo.close()
        
