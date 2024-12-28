import subprocess
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMenuBar, QPushButton, QComboBox
from PyQt5 import uic
from pathlib import Path

from src.iu.funcionalidad.ReportesW import ReportesW
from src.iu.funcionalidad.ViajeW import ViajeW
from src.estructura_datos.lista_simple.ListaSimple import ListaSimple
from src.estructura_datos.grafo.ListaAdyacencia import ListaAdyacencia
from src.iu.funcionalidad.VehiculoW import VehiculoW
from src.estructura_datos.arbol_b.ArbolB import ArbolB
from src.iu.funcionalidad.MensajeD import MensajeD
from src.iu.funcionalidad.GraficoW import GraficoW
from src.iu.funcionalidad.ClienteW import ClienteW
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble
from src.utils.CargarDatos import CargarDatos
from src.utils.Graficar import Graficar

class MainW(QMainWindow):
    def __init__(self, clientes: ListaCircularDoble, vehiculos: ArbolB, rutas: ListaAdyacencia, viajes: ListaSimple):
        super(MainW, self).__init__()
        self.clientes = clientes
        self.vehiculos = vehiculos
        self.rutas = rutas
        self.viajes = viajes
        
        ruta_ui = Path(__file__).parent / 'main.ui'
        uic.loadUi(ruta_ui, self)
        
        self.menu_bar = self.findChild(QMenuBar, 'menubar')
        self.reportes_cb = self.findChild(QComboBox, 'comboBox_reportes')
        self.ver_reporte_btn = self.findChild(QPushButton, 'pushButton_ver_reporte')
        
        self.reportes_cb.addItems(['Seleccionar un reporte', 'Top viajes', 'Top ganancia', 'Top clientes', 'Top vehículos', 'Ruta de un viaje'])
        self.ver_reporte_btn.clicked.connect(self.ver_reporte)
        
        self.menu_bar.hide()
        self.reportes_cb.hide()
        self.ver_reporte_btn.hide()
        
        self.cargar_rutas_btn = self.findChild(QPushButton, 'pushButton_cargar_rutas')
        self.cargar_rutas_btn.clicked.connect(self.cargar_rutas)
        
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
        
        self.action_graficar_rts.triggered.connect(self.graficar_rutas)
        
        self.action_crear_vj.triggered.connect(lambda: self.accion_viaje(1))
        self.action_graficar_vj.triggered.connect(lambda: self.accion_viaje(3))
        
        self.action_cargar_clientes.triggered.connect(lambda: self.abrir_archivo(1))
        self.action_cargar_vehiculos.triggered.connect(lambda: self.abrir_archivo(2))
        #self.action_cargar_rutas.triggered.connect(lambda: self.abrir_archivo(3))
        
        self.show()
    
    def abrir_archivo(self, opcion:int = 0):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '/home/herberthreyes/Escritorio/', 'All files(*);;Python files(*.py)')
        if filename[0]:
            lc = CargarDatos()
            if opcion == 1:
                lc.cargar_clientes(filename[0], self.clientes)
                self.window = MensajeD('Exito', 'Clientes importados', 'Los clientes han sido \nimportados con éxito')
            elif opcion == 2:
                lc.cargar_vehiculos(filename[0], self.vehiculos)
                self.window = MensajeD('Exito', 'Vehiculos importados', 'Los vehiculos han sido \nimportados con éxito')
            elif opcion == 3:
                lc.cargar_rutas(filename[0], self.rutas)
                self.window = MensajeD('Exito', 'Rutas importadas', 'Las rutas han sido \nimportadas con éxito')
                
    def cargar_rutas(self):
        self.abrir_archivo(3)
        self.menu_bar.show()
        self.reportes_cb.show()
        self.ver_reporte_btn.show()
        self.cargar_rutas_btn.hide()
        
    def ver_reporte(self):
        opcion = self.reportes_cb.currentIndex()
        
        if opcion == 0:
            self.window = MensajeD('Error', 'Reporte no seleccionado', 'Por favor seleccione un reporte')
            return
        
        if opcion == 5:
            self.accion_viaje(2)
        else:
            self.window = ReportesW(self.viajes, opcion)

    def accion_cliente(self, opcion:int = 0):
        
        if opcion == 5:
            if not self.clientes.esta_vacia():
                graficar_aux = Graficar()
                graficar_aux.graficar("graficas_edd/clientes.svg", self.clientes.graficar())    
            
            subprocess.run(["xdg-open", "graficas_edd/clientes.svg"])
            #self.window = GraficoW("clientes.svg", "Reporte de Clientes")
        else:
            self.window = ClienteW(self.clientes, opcion)
        
    def accion_vehiculo(self, opcion:int = 0):
        
        if opcion == 5:
            if not self.vehiculos.esta_vacio():
                graficar_aux = Graficar()
                graficar_aux.graficar("graficas_edd/vehiculos.svg", self.vehiculos.graficar_arbol())    
            
            subprocess.run(["xdg-open", "graficas_edd/vehiculos.svg"])
        
        else:
            self.window = VehiculoW(self.vehiculos, opcion)
            
    def accion_viaje(self, opcion:int = 0):
        
        if opcion == 3:
            if not self.viajes.esta_vacia():
                graficar_aux = Graficar()
                graficar_aux.graficar("graficas_edd/viajes.svg", self.viajes.graficar_viajes())
            
            subprocess.run(["xdg-open", "graficas_edd/viajes.svg"])
        else:
            self.window = ViajeW(opcion, self.viajes, self.rutas, self.vehiculos, self.clientes)
                    
    def graficar_rutas(self):
        
        if not self.rutas.esta_vacia():
            graficar_aux = Graficar()
            graficar_aux.graficar("graficas_edd/rutas.svg", self.rutas.graficar())    
        
        subprocess.run(["xdg-open", "graficas_edd/rutas.svg"])