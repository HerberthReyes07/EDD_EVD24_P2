import subprocess
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
from pathlib import Path

from src.iu.funcionalidad.VehiculoW import VehiculoW
from src.estructura_datos.arbol_b.ArbolB import ArbolB
from src.iu.funcionalidad.MensajeD import MensajeD
from src.iu.funcionalidad.GraficoW import GraficoW
from src.iu.funcionalidad.ClienteW import ClienteW
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble
from src.utils.CargarDatos import CargarDatos
from src.utils.Graficar import Graficar

class MainW(QMainWindow):
    def __init__(self, lista: ListaCircularDoble, arbolB: ArbolB):
        super(MainW, self).__init__()
        self.lista = lista
        self.arbolB = arbolB
        
        ruta_ui = Path(__file__).parent / 'main.ui'
        uic.loadUi(ruta_ui, self)
        
        self.action_crear_clt.triggered.connect(lambda: self.accion_cliente(1))
        self.action_modificar_clt.triggered.connect(lambda: self.accion_cliente(2))
        self.action_eliminar_clt.triggered.connect(lambda: self.accion_cliente(3))
        self.action_info_clt.triggered.connect(lambda: self.accion_cliente(4))
        self.action_graficar_clt.triggered.connect(lambda: self.accion_cliente(5))
        
        self.action_crear_vhcl.triggered.connect(lambda: self.accion_vehiculo(1))
        self.action_modificar_vhcl.triggered.connect(lambda: self.accion_vehiculo(2))
        self.action_eliminar_vhcl.triggered.connect(lambda: self.accion_vehiculo(3))
        self.action_info_vhcl.triggered.connect(lambda: self.accion_vehiculo(4))
        self.action_graficar_vhcl.triggered.connect(lambda: self.accion_vehiculo(5))
        
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
                self.window = MensajeD('Exito', 'Clientes importados', 'Los clientes han sido \nimportados con éxito')
            elif opcion == 2:
                lc.cargar_vehiculos(filename[0], self.arbolB)
                self.window = MensajeD('Exito', 'Vehiculos importados', 'Los vehiculos han sido \nimportados con éxito')
            elif opcion == 3:
                lc.cargar_rutas(filename[0])

    def accion_cliente(self, opcion:int = 0):
        
        if opcion == 5:
            if not self.lista.esta_vacia():
                graficar_aux = Graficar()
                graficar_aux.graficar("graficas_edd/clientes.svg", self.lista.graficar())    
            
            subprocess.run(["xdg-open", "graficas_edd/clientes.svg"])
            #self.window = GraficoW("clientes.svg", "Reporte de Clientes")
        else:
            self.window = ClienteW(self.lista, opcion)
        
    def accion_vehiculo(self, opcion:int = 0):
        
        if opcion == 5:
            if not self.arbolB.esta_vacio():
                graficar_aux = Graficar()
                graficar_aux.graficar("graficas_edd/vehiculos.svg", self.arbolB.graficar_arbol())    
            
            subprocess.run(["xdg-open", "graficas_edd/vehiculos.svg"])
        
        else:
            self.window = VehiculoW(self.arbolB, opcion)