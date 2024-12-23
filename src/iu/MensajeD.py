from PyQt5 import QtWidgets, uic
from pathlib import Path

class MensajeD(QtWidgets.QDialog):
    def __init__(self, titulo_ventana: str, titulo: str, mensaje: str):
        super(MensajeD, self).__init__()
        
        ruta_ui = Path(__file__).parent / 'mensaje.ui'
        uic.loadUi(ruta_ui, self)
        
        self.setWindowTitle(titulo_ventana)
        self.label_titulo.setText(titulo)
        self.label_mensaje.setText(mensaje)
        
        self.aceptar_btn = self.findChild(QtWidgets.QPushButton, 'pushButton_aceptar')
        self.aceptar_btn.clicked.connect(self.aceptar)
        
        self.show()

    def aceptar(self):
        self.close()