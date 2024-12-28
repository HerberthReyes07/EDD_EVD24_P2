from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox
from PyQt5 import uic
from pathlib import Path

from src.iu.funcionalidad.MensajeD import MensajeD
from src.estructura_datos.grafo.ListaAdyacencia import ListaAdyacencia
from src.estructura_datos.lista_simple.ListaSimple import ListaSimple
from src.estructura_datos.arbol_b.ArbolB import ArbolB
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble
from src.modelo.Viaje import Viaje


class ViajeW(QMainWindow):
    
    def __init__(self, opcion: int, viajes: ListaSimple, rutas: ListaAdyacencia, vehiculos: ArbolB, clientes: ListaCircularDoble):
        super(ViajeW, self).__init__()
        self.opcion = opcion
        self.viajes = viajes
        self.rutas = rutas
        self.vehiculos = vehiculos
        self.clientes = clientes
        
        ruta_ui = Path(__file__).parent / '../modelo/viaje.ui'
        uic.loadUi(ruta_ui, self)
        
        self.accion_btn = self.findChild(QPushButton, 'pushButton_iniciar')
        
        self.buscar_cb = self.findChild(QComboBox, 'comboBox_buscar')
        self.origen_cb = self.findChild(QComboBox, 'comboBox_origen')
        self.destino_cb = self.findChild(QComboBox, 'comboBox_destino')
        self.cliente_cb = self.findChild(QComboBox, 'comboBox_cliente')
        self.vehiculo_cb = self.findChild(QComboBox, 'comboBox_vehiculo')
        
        self.nombre_cliente_le = self.findChild(QLineEdit, 'lineEdit_nombre_cliente')
        self.nombre_vehiculo_le = self.findChild(QLineEdit, 'lineEdit_nombre_vehiculo')
        
        self.cliente_cb.activated.connect(self.buscar_cliente)
        self.vehiculo_cb.activated.connect(self.buscar_vehiculo)
        self.buscar_cb.activated.connect(self.buscar_viaje)
        
        self.accion_btn.clicked.connect(self.accion_viaje)
        
        self.llenar_cb_ciudades()
        self.llenar_cb_clientes()
        self.llenar_cb_vehiculos()
        
        if self.opcion == 1:
            self.setWindowTitle('Iniciar Viaje')
            self.buscar_cb.hide()
            
        else:
            self.setWindowTitle('Graficar Ruta')
            self.accion_btn.setText('Graficar')
            self.accion_btn.setDisabled(True)
            self.origen_cb.setDisabled(True)
            self.destino_cb.setDisabled(True)
            self.cliente_cb.setDisabled(True)
            self.vehiculo_cb.setDisabled(True)
            self.llenar_cb_buscar()
        
        self.show()
        
    def accion_viaje(self):
        
        if self.opcion == 1:
        
            if self.origen_cb.currentIndex() == 0 or self.destino_cb.currentIndex() == 0 or self.cliente_cb.currentIndex() == 0 or self.vehiculo_cb.currentIndex() == 0:
                self.window = MensajeD('Error', 'Datos incompletos', 'Todos los campos son obligatorios')
                return
            
            dt = datetime.now()
            fecha:str =  f'{dt.day}/{dt.month}/{dt.year}'
            hora:str = dt.strftime("%H") + ':' + dt.strftime("%M")
            
            viaje = Viaje(self.origen_cb.currentText(), self.destino_cb.currentText(), fecha, hora, self.cliente_seleccionado, self.vehiculo_seleccionado)
            #camino mas corto
            self.viajes.insertar_viaje(viaje)
            
            self.window = MensajeD('Exito', 'Viaje iniciado', 'El viaje ha sido iniciado con éxito')
            self.limpiar_campos()
        
        else:
            #graficar ruta del viaje
            pass
        
    def buscar_viaje(self):
        
        if self.buscar_cb.currentIndex() == 0:
            self.limpiar_campos()
            self.accion_btn.setDisabled(True)
            return
        
        self.viaje_buscado = self.viajes.buscar_viaje(int(self.buscar_cb.currentText()))
        
        if self.viaje_buscado is None:
            print('Viaje no encontrado')
            return
        
        self.mostrar_datos()
        self.accion_btn.setDisabled(False)
        
    def buscar_cliente(self):
        
        if self.cliente_cb.currentIndex() == 0:
            self.nombre_cliente_le.clear()
            return
        
        self.cliente_seleccionado = self.clientes.buscar(int(self.cliente_cb.currentText()))
        
        if self.cliente_seleccionado is None:
            print('Cliente no encontrado')
            return
        
        self.nombre_cliente_le.setText(self.cliente_seleccionado.get_nombres() + ' ' + self.cliente_seleccionado.get_apellidos())
        
    def buscar_vehiculo(self):
        
        if self.vehiculo_cb.currentIndex() == 0:
            self.nombre_vehiculo_le.clear()
            return
        
        self.vehiculo_seleccionado = self.vehiculos.buscar_vehiculo(self.vehiculo_cb.currentText())
        
        if self.vehiculo_seleccionado is None:
            print('Vehiculo no encontrado')
            return
        
        self.nombre_vehiculo_le.setText(self.vehiculo_seleccionado.get_marca() + ' ' + self.vehiculo_seleccionado.get_modelo())    
    
    def llenar_cb_buscar(self):
        self.buscar_cb.clear()
        self.buscar_cb.addItem('Seleccione un ID')
        
        if not self.viajes.esta_vacia():
        
            recorrer = self.viajes.get_cabeza()
            
            while recorrer is not None:
                self.buscar_cb.addItem(recorrer.get_valor().get_id().__str__())
                recorrer = recorrer.get_siguiente()
    
    def llenar_cb_ciudades(self):
        self.origen_cb.clear()
        self.destino_cb.clear()
        
        self.origen_cb.addItem("Seleccione una ciudad origen")
        self.destino_cb.addItem("Seleccione una ciudad destino")
        
        recorrer = self.rutas.get_vertices().get_cabeza()
        
        while recorrer is not None:
            self.origen_cb.addItem(recorrer.get_valor().get_ciudad())
            self.destino_cb.addItem(recorrer.get_valor().get_ciudad())
            recorrer = recorrer.get_siguiente()
        
    def llenar_cb_clientes(self):
        self.cliente_cb.clear()
        self.cliente_cb.addItem('Seleccione un DPI')
        
        if not self.clientes.esta_vacia():
        
            recorrer = self.clientes.get_cabeza()
            
            while True:
                self.cliente_cb.addItem(recorrer.get_cliente().get_dpi().__str__())
                recorrer = recorrer.get_siguiente()
                if recorrer == self.clientes.get_cabeza():
                    break
        
    def llenar_cb_vehiculos(self):
        self.vehiculo_cb.clear()
        self.vehiculo_cb.addItem('Seleccione una Placa')
        self.vehiculo_cb.addItems(self.vehiculos.obtener_placas())
        
    def mostrar_datos(self):
        
        self.origen_cb.setCurrentText(self.viaje_buscado.get_origen())
        self.destino_cb.setCurrentText(self.viaje_buscado.get_destino())
        self.cliente_cb.setCurrentText(self.viaje_buscado.get_cliente().get_dpi().__str__())
        self.nombre_cliente_le.setText(self.viaje_buscado.get_cliente().get_nombres() + ' ' + self.viaje_buscado.get_cliente().get_apellidos())
        self.vehiculo_cb.setCurrentText(self.viaje_buscado.get_vehiculo().get_placa())
        self.nombre_vehiculo_le.setText(self.viaje_buscado.get_vehiculo().get_marca() + ' ' + self.viaje_buscado.get_vehiculo().get_modelo())
    
    def limpiar_campos(self):
        self.origen_cb.setCurrentIndex(0)
        self.destino_cb.setCurrentIndex(0)
        self.cliente_cb.setCurrentIndex(0)
        self.vehiculo_cb.setCurrentIndex(0)
        self.nombre_cliente_le.clear()
        self.nombre_vehiculo_le.clear()  
    