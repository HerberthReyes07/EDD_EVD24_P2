from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog
from PyQt5 import uic
from pathlib import Path

from src.utils.CargarDatos import CargarDatos

class Entrada(QMainWindow):
    def __init__(self):
        super(Entrada, self).__init__()
        ruta_ui = Path(__file__).parent / 'entrada.ui'
        uic.loadUi(ruta_ui, self)

        self.btn_clientes = self.findChild(QPushButton, 'clientes_btn')
        self.btn_clientes.clicked.connect(lambda: self.open_dialog(1))
        
        self.btn_vehiculos = self.findChild(QPushButton, 'vehiculos_btn')
        self.btn_vehiculos.clicked.connect(lambda: self.open_dialog(2))

        self.btn_rutas = self.findChild(QPushButton, 'rutas_btn')
        self.btn_rutas.clicked.connect(lambda: self.open_dialog(3))
        
        self.show()
    
    def open_dialog(self, opcion:int = 0):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '/home/herberthreyes/Escritorio/', 'All files(*);;Python files(*.py)')
        if filename[0]:
            lc = CargarDatos()
            if opcion == 1:
                lc.cargar_clientes(filename[0])
            elif opcion == 2:
                lc.cargar_vehiculos(filename[0])
            elif opcion == 3:
                lc.cargar_rutas(filename[0])
