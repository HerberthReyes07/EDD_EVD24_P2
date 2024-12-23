from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from pathlib import Path

class GraficoW(QMainWindow):
    def __init__(self, path_grafico:str, titulo:str):
        super(GraficoW, self).__init__()
        ruta_ui = Path(__file__).parent / 'grafico.ui'
        uic.loadUi(ruta_ui, self)
        
        self.setWindowTitle(titulo)
        self.titulo_lbl = self.findChild(QLabel, 'label_titulo')
        self.imagen_lbl = self.findChild(QLabel, 'label_imagen')
        
        self.titulo_lbl.setText(titulo)
        self.pixMap = QPixmap(path_grafico)
        
        width = self.pixMap.width() * 3
        height = self.pixMap.height() * 3
        resized_pixmap = self.pixMap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.imagen_lbl.setPixmap(resized_pixmap)
        self.imagen_lbl.resize(resized_pixmap.width(), resized_pixmap.height())
        #self.imagen_lbl.setPixmap(self.pixMap)
        
        #self.adjustSize()
        
        self.show()
    pass