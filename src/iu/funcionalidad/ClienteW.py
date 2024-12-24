from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox
from PyQt5 import uic
from pathlib import Path

from src.iu.funcionalidad.MensajeD import MensajeD
from src.modelo.Cliente import Cliente
from src.estructura_datos.lista_circular_doblemente_enlazada.ListaCircularDoble import ListaCircularDoble

class ClienteW(QMainWindow):
    
    def __init__(self, lista: ListaCircularDoble , opcion:int = 0):
        super(ClienteW, self).__init__()
        self.lista = lista
        self.opcion = opcion
        ruta_ui = Path(__file__).parent / '../modelo/cliente.ui'
        uic.loadUi(ruta_ui, self)
        
        self.buscar_cb = self.findChild(QComboBox, 'comboBox_buscar')
        self.accion_btn = self.findChild(QPushButton, 'pushButton_accion')
        self.buscar_cb.activated.connect(self.buscar_cliente)
        self.accion_btn.clicked.connect(self.accion_cliente)
        
        self.dpi_le = self.findChild(QLineEdit, 'lineEdit_dpi')
        self.nombres_le = self.findChild(QLineEdit, 'lineEdit_nombres')
        self.apellidos_le = self.findChild(QLineEdit, 'lineEdit_apellidos')
        self.genero_cb = self.findChild(QComboBox, 'comboBox_genero')
        self.telefono_le = self.findChild(QLineEdit, 'lineEdit_telefono')
        self.direccion_le = self.findChild(QLineEdit, 'lineEdit_direccion')
        
        self.llenar_combo_box()
        self.genero_cb.addItems(["Seleccione un genero", "Masculino", "Femenino"])
        
        if opcion == 1:
            self.setWindowTitle('Crear Cliente')
            self.buscar_cb.hide()
            self.accion_btn.setText('Crear')
        elif opcion == 2:
            self.setWindowTitle('Modificar Cliente')
            self.desactivar_campos(True)   
            self.accion_btn.setText('Modificar')
            self.accion_btn.setDisabled(True)
        elif opcion == 3:
            self.setWindowTitle('Eliminar Cliente')
            self.desactivar_campos(True)
            self.accion_btn.setText('Eliminar')
            self.accion_btn.setDisabled(True)
        elif opcion == 4:
            self.setWindowTitle('Información Cliente')
            self.desactivar_campos(True)
            self.accion_btn.hide()
        
        self.show()
        
    def buscar_cliente(self):
        
        if not self.es_numero(self.buscar_cb.currentText()):
            self.desactivar_campos(True)
            self.accion_btn.setDisabled(True)
            self.limpiar_campos()
            return
        
        self.cliente_buscado: Cliente = self.lista.buscar(int(self.buscar_cb.currentText()))
        
        if self.cliente_buscado is None:
            print('Cliente no encontrado')
            return
        
        self.mostrar_datos()
        self.accion_btn.setDisabled(False)
        
        if self.opcion == 2:
            self.desactivar_campos(False)
        
        self.dpi_le.setDisabled(True)
    
    def accion_cliente(self):
        
        if not self.es_numero(self.dpi_le.text()) or not self.es_numero(self.telefono_le.text()):
            self.window = MensajeD('Error', 'Datos no validos', 'El DPI y el telefono deben ser \nnumeros')
            return
        
        if self.dpi_le.text() == '' or self.nombres_le.text() == '' or self.apellidos_le.text() == '' or self.genero_cb.currentIndex() == 0 or self.telefono_le.text() == '' or self.direccion_le.text() == '':
            self.window = MensajeD('Error', 'Datos incompletos', 'Todos los campos son obligatorios')
            return
        
        if self.opcion == 1:
            self.lista.insertar(Cliente(int(self.dpi_le.text()), self.nombres_le.text(), self.apellidos_le.text(), self.genero_cb.currentText()[0], int(self.telefono_le.text()), self.direccion_le.text()))
            self.limpiar_campos()
            self.window = MensajeD('Exito', 'Cliente creado', 'El cliente ha sido creado \ncon éxito')
        
        elif self.opcion == 2:
            self.cliente_buscado.set_nombres(self.nombres_le.text())
            self.cliente_buscado.set_apellidos(self.apellidos_le.text())
            self.cliente_buscado.set_genero(self.genero_cb.currentText()[0])
            self.cliente_buscado.set_telefono(int(self.telefono_le.text()))
            self.cliente_buscado.set_direccion(self.direccion_le.text())
            self.window = MensajeD('Exito', 'Cliente modificado', 'El cliente ha sido modificado \ncon éxito')
            
        elif self.opcion == 3:
            self.lista.eliminar(int(self.dpi_le.text()))
            self.limpiar_campos()
            self.llenar_combo_box()
            self.buscar_cb.setCurrentIndex(0)
            self.accion_btn.setDisabled(True)
            self.window = MensajeD('Exito', 'Cliente eliminado', 'El cliente ha sido eliminado \ncon éxito')
        
   
    def llenar_combo_box(self):
        self.buscar_cb.clear()
        self.buscar_cb.addItem('Seleccione un DPI')
        
        if not self.lista.esta_vacia():
        
            recorrer = self.lista.get_cabeza()
            
            while True:
                self.buscar_cb.addItem(recorrer.get_cliente().get_dpi().__str__())
                recorrer = recorrer.get_siguiente()
                if recorrer == self.lista.get_cabeza():
                    break
   
    def es_numero(self, dato:str) -> bool:
        if not dato.isdigit():
            return False
        return True
       
    def mostrar_datos(self):
        self.dpi_le.setText(self.cliente_buscado.get_dpi().__str__())
        self.nombres_le.setText(self.cliente_buscado.get_nombres())
        self.apellidos_le.setText(self.cliente_buscado.get_apellidos())
        self.genero_cb.setCurrentIndex(1 if self.cliente_buscado.get_genero() == "M" else 2)
        self.telefono_le.setText(self.cliente_buscado.get_telefono().__str__())
        self.direccion_le.setText(self.cliente_buscado.get_direccion()) 
        
    def desactivar_campos(self, opcion:bool = True):
        self.dpi_le.setDisabled(opcion)
        self.nombres_le.setDisabled(opcion)
        self.apellidos_le.setDisabled(opcion)
        self.genero_cb.setDisabled(opcion)
        self.telefono_le.setDisabled(opcion)
        self.direccion_le.setDisabled(opcion)
        
    def limpiar_campos(self):
        self.dpi_le.clear()
        self.nombres_le.clear()
        self.apellidos_le.clear()
        self.genero_cb.setCurrentIndex(0)
        self.telefono_le.clear()
        self.direccion_le.clear()