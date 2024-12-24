from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox
from PyQt5 import uic
from pathlib import Path

from src.iu.MensajeD import MensajeD
from src.estructura_datos.arbol_b.ArbolB import ArbolB
from src.modelo.Vehiculo import Vehiculo

class VehiculoW(QMainWindow):
    
    def __init__(self, arbolB: ArbolB , opcion:int = 0):
        super(VehiculoW, self).__init__()
        self.arbolB = arbolB
        self.opcion = opcion
        ruta_ui = Path(__file__).parent / 'vehiculo.ui'
        uic.loadUi(ruta_ui, self)
        
        self.buscar_cb = self.findChild(QComboBox, 'comboBox_buscar')
        self.accion_btn = self.findChild(QPushButton, 'pushButton_accion')
        self.buscar_cb.activated.connect(self.buscar_vehiculo)
        self.accion_btn.clicked.connect(self.accion_vehiculo)
        
        self.placa_le = self.findChild(QLineEdit, 'lineEdit_placa')
        self.marca_le = self.findChild(QLineEdit, 'lineEdit_marca')
        self.modelo_le = self.findChild(QLineEdit, 'lineEdit_modelo')
        self.precio_le = self.findChild(QLineEdit, 'lineEdit_precio')
        
        self.llenar_combo_box()
        
        if opcion == 1:
            self.setWindowTitle('Crear Vehiculo')
            self.buscar_cb.hide()
            self.accion_btn.setText('Crear')
        elif opcion == 2:
            self.setWindowTitle('Modificar Vehiculo')
            self.desactivar_campos(True)   
            self.accion_btn.setText('Modificar')
            self.accion_btn.setDisabled(True)
        elif opcion == 3:
            self.setWindowTitle('Eliminar Vehiculo')
            self.desactivar_campos(True)
            self.accion_btn.setText('Eliminar')
            self.accion_btn.setDisabled(True)
        elif opcion == 4:
            self.setWindowTitle('Información Vehiculo')
            self.desactivar_campos(True)
            self.accion_btn.hide()
        
        self.show()
        
    def buscar_vehiculo(self):
        
        if self.buscar_cb.currentIndex() == 0:
            self.desactivar_campos(True)
            self.accion_btn.setDisabled(True)
            self.limpiar_campos()
            return
        
        self.vehiculo_buscado: Vehiculo = self.arbolB.buscar_vehiculo(self.buscar_cb.currentText())
        
        if self.vehiculo_buscado is None:
            print('Vehiculo no encontrado')
            return
        
        self.mostrar_datos()
        self.accion_btn.setDisabled(False)
        
        if self.opcion == 2:
            self.desactivar_campos(False)
        
        self.placa_le.setDisabled(True)
        
    def accion_vehiculo(self):
        
        try:
            float(self.precio_le.text())
        except:
            self.window = MensajeD('Error', 'Datos no validos', 'El precio debe ser númerico (Q)')
            return    
        
        if self.placa_le.text() == '' or self.marca_le.text() == '' or self.modelo_le.text() == '' or self.precio_le.text() == '':
            self.window = MensajeD('Error', 'Datos incompletos', 'Todos los campos son obligatorios')
            return
        
        if self.opcion == 1:
            self.arbolB.insertar_vehiculo(Vehiculo(self.placa_le.text(), self.marca_le.text(), self.modelo_le.text(), float(self.precio_le.text())))
            self.limpiar_campos()
            self.window = MensajeD('Exito', 'Vehículo creado', 'El vehículo ha sido creado \ncon éxito')
        
        elif self.opcion == 2:
            self.vehiculo_buscado.set_marca(self.marca_le.text())
            self.vehiculo_buscado.set_modelo(self.modelo_le.text())
            self.vehiculo_buscado.set_precio(float(self.precio_le.text()))
            self.window = MensajeD('Exito', 'Vehículo modificado', 'El vehículo ha sido modificado \ncon éxito')
            
        elif self.opcion == 3:
            #eliminar vehiculo
            pass

    def mostrar_datos(self):
        self.placa_le.setText(self.vehiculo_buscado.get_placa())
        self.marca_le.setText(self.vehiculo_buscado.get_marca())
        self.modelo_le.setText(self.vehiculo_buscado.get_modelo())
        self.precio_le.setText(str(self.vehiculo_buscado.get_precio()))
    
    def llenar_combo_box(self):
        self.buscar_cb.clear()
        self.buscar_cb.addItem('Seleccione una Placa')
        self.buscar_cb.addItems(self.arbolB.obtener_placas())
        
    def desactivar_campos(self, opcion:bool = True):
        self.placa_le.setDisabled(opcion)
        self.marca_le.setDisabled(opcion)
        self.modelo_le.setDisabled(opcion)
        self.precio_le.setDisabled(opcion)
        
    def limpiar_campos(self):
        self.placa_le.clear()
        self.marca_le.clear()
        self.modelo_le.clear()
        self.precio_le.clear()
    