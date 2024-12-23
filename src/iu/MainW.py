import subprocess
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
from pathlib import Path

from src.iu.MensajeD import MensajeD
from src.iu.GraficoW import GraficoW
from src.iu.ClienteW import ClienteW
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble
from src.utils.CargarDatos import CargarDatos
from src.utils.Graficar import Graficar

class MainW(QMainWindow):
    def __init__(self, lista: ListaCircularDoble):
        super(MainW, self).__init__()
        self.lista = lista
        
        ruta_ui = Path(__file__).parent / 'MainW.ui'
        uic.loadUi(ruta_ui, self)
        
        self.action_crear_clt.triggered.connect(lambda: self.accion_cliente(1))
        self.action_modificar_clt.triggered.connect(lambda: self.accion_cliente(2))
        self.action_eliminar_clt.triggered.connect(lambda: self.accion_cliente(3))
        self.action_info_clt.triggered.connect(lambda: self.accion_cliente(4))
        self.action_graficar_clt.triggered.connect(lambda: self.accion_cliente(5))
        
        self.action_cargar_clientes.triggered.connect(lambda: self.abrir_archivo(1))
        self.action_cargar_vehiculos.triggered.connect(lambda: self.abrir_archivo(2))
        self.action_cargar_rutas.triggered.connect(lambda: self.abrir_archivo(3))
        
        self.show()
    
    def abrir_archivo(self, opcion:int = 0):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '/home/herberthreyes/Escritorio/', 'All files(*);;Python files(*.py)')
        if filename[0]:
            lc = CargarDatos()
            if opcion == 1:
                lc.cargar_clientes(filename[0], self.lista)
                self.window = MensajeD('Exito', 'Clientes importados', 'Los clientes han sido \nimportados con exito')
            elif opcion == 2:
                lc.cargar_vehiculos(filename[0])
            elif opcion == 3:
                lc.cargar_rutas(filename[0])

    def accion_cliente(self, opcion:int = 0):
        
        if opcion == 5:
            if not self.lista.esta_vacia():
                graficar_aux = Graficar()
                graficar_aux.graficar("clientes.svg", self.lista.graficar())    
            
            subprocess.run(["xdg-open", "clientes.svg"])
            #self.window = GraficoW("clientes.svg", "Reporte de Clientes")
        else:
            self.window = ClienteW(self.lista, opcion)
        #self.window.show()