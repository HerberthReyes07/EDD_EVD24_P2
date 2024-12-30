from PyQt5.QtWidgets import QMainWindow, QTableWidget, QLabel, QTableWidgetItem
from PyQt5 import uic
from pathlib import Path

from src.modelo.Cliente import Cliente
from src.modelo.Vehiculo import Vehiculo
from src.estructura_datos.lista_simple.ListaSimple import ListaSimple
from collections import Counter

class ReportesW(QMainWindow):
    
    def __init__(self, viajes: ListaSimple, opcion: int):
        super(ReportesW, self).__init__()
        ruta_ui = Path(__file__).parent / '../modelo/reporte.ui'
        uic.loadUi(ruta_ui, self)
        
        self.viajes = viajes
        
        self.reporte_tbl = self.findChild(QTableWidget, 'tableWidget_top')
        self.tipo_reporte_lbl = self.findChild(QLabel, 'label_tipo_reporte')
        
        self.reporte_tbl.setRowCount(5)
        
        if opcion == 1:
            self.tipo_reporte_lbl.setText('Top Viajes')
            self.reporte_tbl.setColumnCount(8)
            self.reporte_tbl.setHorizontalHeaderLabels(['ID', 'Origen', 'Destino', 'Cliente', 'Vehiculo', 'Fecha', 'Hora', 'No. Destinos'])
            self.llenar_tabla_top_viajes()
            
        elif opcion == 2:
            self.tipo_reporte_lbl.setText('Top Ganancia')
            self.reporte_tbl.setColumnCount(10)
            self.reporte_tbl.setHorizontalHeaderLabels(['ID', 'Origen', 'Destino', 'Cliente', 'Vehiculo', 'Fecha', 'Hora', 'Precio (Q)', 'Tiempo', 'Recaudado (Q)'])
            self.llenar_tabla_top_ganancia()
        
        elif opcion == 3:
            self.tipo_reporte_lbl.setText('Top Clientes')
            self.reporte_tbl.setColumnCount(7)
            self.reporte_tbl.setHorizontalHeaderLabels(['DPI', 'Nombres', 'Apellidos', 'Genero', 'Telefono', 'Direccion', 'No. Viajes'])
            self.llenar_tabla_top_clientes()
            
        elif opcion == 4:
            self.tipo_reporte_lbl.setText('Top Vehiculos')
            self.reporte_tbl.setColumnCount(5)
            self.reporte_tbl.setHorizontalHeaderLabels(['Placa', 'Marca', 'Modelo', 'Precio (Q)', 'No. Viajes'])
            self.llenar_tabla_top_vehiculos()
        
        self.show()
        
    def llenar_tabla_top_viajes(self):
        
        top_viajes: list[dict] = []
        
        recorrer_viajes = self.viajes.get_cabeza()
        
        while recorrer_viajes != None:
            
            viaje = recorrer_viajes.get_valor()
            
            top_viajes.append({
                'viaje': viaje,
                'no_destinos': viaje.obtener_tam_lista()
            })    
            recorrer_viajes = recorrer_viajes.get_siguiente()
        
        top_viajes.sort(key=lambda x: x['no_destinos'], reverse=True)
        
        for i in range(len(top_viajes)):
            
            if i == 5:
                break
            
            viaje = top_viajes[i]['viaje']
            self.reporte_tbl.setItem(i, 0, QTableWidgetItem(str(viaje.get_id())))
            self.reporte_tbl.setItem(i, 1, QTableWidgetItem(viaje.get_origen()))
            self.reporte_tbl.setItem(i, 2, QTableWidgetItem(viaje.get_destino()))
            self.reporte_tbl.setItem(i, 3, QTableWidgetItem(str(viaje.get_cliente().get_dpi())))
            self.reporte_tbl.setItem(i, 4, QTableWidgetItem(viaje.get_vehiculo().get_placa()))
            self.reporte_tbl.setItem(i, 5, QTableWidgetItem(viaje.get_fecha()))
            self.reporte_tbl.setItem(i, 6, QTableWidgetItem(viaje.get_hora()))
            self.reporte_tbl.setItem(i, 7, QTableWidgetItem(str(viaje.obtener_tam_lista()))
        )
    
    def llenar_tabla_top_ganancia(self):
        
        top_ganancia: list[dict] = []
        
        recorrer_viajes = self.viajes.get_cabeza()
        
        while recorrer_viajes != None:
            
            viaje = recorrer_viajes.get_valor()
            
            top_ganancia.append({
                'viaje': viaje,
                'ganancia': round(viaje.obtener_tiempo_total() * viaje.get_vehiculo().get_precio(), 2)
            })    
            recorrer_viajes = recorrer_viajes.get_siguiente()
        
        top_ganancia.sort(key=lambda x: x['ganancia'], reverse=True)
        
        for i in range(len(top_ganancia)):
            
            if i == 5:
                break
            
            viaje = top_ganancia[i]['viaje']
            self.reporte_tbl.setItem(i, 0, QTableWidgetItem(str(viaje.get_id())))
            self.reporte_tbl.setItem(i, 1, QTableWidgetItem(viaje.get_origen()))
            self.reporte_tbl.setItem(i, 2, QTableWidgetItem(viaje.get_destino()))
            self.reporte_tbl.setItem(i, 3, QTableWidgetItem(str(viaje.get_cliente().get_dpi())))
            self.reporte_tbl.setItem(i, 4, QTableWidgetItem(viaje.get_vehiculo().get_placa()))
            self.reporte_tbl.setItem(i, 5, QTableWidgetItem(viaje.get_fecha()))
            self.reporte_tbl.setItem(i, 6, QTableWidgetItem(viaje.get_hora()))
            self.reporte_tbl.setItem(i, 7, QTableWidgetItem(str(viaje.get_vehiculo().get_precio())))
            self.reporte_tbl.setItem(i, 8, QTableWidgetItem(str(viaje.obtener_tiempo_total())))
            self.reporte_tbl.setItem(i, 9, QTableWidgetItem(str(top_ganancia[i]['ganancia'])))
 
        
    def llenar_tabla_top_clientes(self):
        
        clientes: list[Cliente] = []
        
        recorrer_clientes = self.viajes.get_cabeza()
        
        while recorrer_clientes != None:
            clientes.append(recorrer_clientes.get_valor().get_cliente())
            recorrer_clientes = recorrer_clientes.get_siguiente()
            
        cliente_counter = Counter(clientes)
        clientes_ordenados = [{'cliente': cliente, 'no_viajes': count} for cliente, count in cliente_counter.items()]
        clientes_ordenados.sort(key=lambda x: x['no_viajes'], reverse=True)
        
        for i in range(len(clientes_ordenados)):
            
            if i == 5:
                break
            
            cliente = clientes_ordenados[i]
            self.reporte_tbl.setItem(i, 0, QTableWidgetItem(str(cliente['cliente'].get_dpi())))
            self.reporte_tbl.setItem(i, 1, QTableWidgetItem(cliente['cliente'].get_nombres()))
            self.reporte_tbl.setItem(i, 2, QTableWidgetItem(cliente['cliente'].get_apellidos()))
            self.reporte_tbl.setItem(i, 3, QTableWidgetItem("Masculino" if cliente['cliente'].get_genero() == 'M' else "Femenino"))
            self.reporte_tbl.setItem(i, 4, QTableWidgetItem(str(cliente['cliente'].get_telefono())))
            self.reporte_tbl.setItem(i, 5, QTableWidgetItem(cliente['cliente'].get_direccion()))
            self.reporte_tbl.setItem(i, 6, QTableWidgetItem(str(cliente['no_viajes'])))
    
    def llenar_tabla_top_vehiculos(self):
        
        vehiculos: list[Vehiculo] = []
        
        recorrer_vehiculos = self.viajes.get_cabeza()
        
        while recorrer_vehiculos != None:
            vehiculos.append(recorrer_vehiculos.get_valor().get_vehiculo())
            recorrer_vehiculos = recorrer_vehiculos.get_siguiente()
    
        # Count occurrences of each vehicle
        vehiculo_counter = Counter(vehiculos)
        # Create a list of dictionaries with vehicle and number of trips
        vehiculos_ordenados = [{'vehiculo': vehiculo, 'no_viajes': count} for vehiculo, count in vehiculo_counter.items()]
        vehiculos_ordenados.sort(key=lambda x: x['no_viajes'], reverse=True)
        
        for i in range(len(vehiculos_ordenados)):
            
            if i == 5:
                break
            
            vehiculo = vehiculos_ordenados[i]
            self.reporte_tbl.setItem(i, 0, QTableWidgetItem(vehiculo['vehiculo'].get_placa()))
            self.reporte_tbl.setItem(i, 1, QTableWidgetItem(vehiculo['vehiculo'].get_marca()))
            self.reporte_tbl.setItem(i, 2, QTableWidgetItem(str(vehiculo['vehiculo'].get_modelo())))
            self.reporte_tbl.setItem(i, 3, QTableWidgetItem(str(vehiculo['vehiculo'].get_precio())))
            self.reporte_tbl.setItem(i, 4, QTableWidgetItem(str(vehiculo['no_viajes'])))  