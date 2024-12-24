# main.py
import sys
from PyQt5.QtWidgets import QApplication
from src.estructura_datos.arbol_b.ArbolB import ArbolB
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble
from src.iu.MainW import MainW

class main:
    def __init__(self):
        
        lista: ListaCircularDoble = ListaCircularDoble()
        arbolB: ArbolB = ArbolB(5)
        
        app = QApplication(sys.argv)
        window = MainW(lista, arbolB)
        app.exec_()
        
          

if __name__ == "__main__":
    main()