# main.py
import sys
from PyQt5.QtWidgets import QApplication
from src.iu.Entrada import Entrada

class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        window = Entrada()
        app.exec_()  

if __name__ == "__main__":
    Main()