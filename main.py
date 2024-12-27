# main.py
import sys
from PyQt5.QtWidgets import QApplication
from src.estructura_datos.lista_simple.ListaSimple import ListaSimple
from src.estructura_datos.grafo.ListaAdyacencia import ListaAdyacencia
from src.estructura_datos.arbol_b.ArbolB import ArbolB
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble
from src.iu.MainW import MainW

class main:
    def __init__(self):
        
        clientes: ListaCircularDoble = ListaCircularDoble()
        vehiculos: ArbolB = ArbolB(5)
        rutas = ListaAdyacencia()
        viajes = ListaSimple()
        
        app = QApplication(sys.argv)
        window = MainW(clientes, vehiculos, rutas, viajes)
        app.exec_()
        
          

if __name__ == "__main__":
    main()