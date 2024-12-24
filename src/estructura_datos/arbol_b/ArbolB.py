from src.modelo.Vehiculo import Vehiculo
from src.estructura_datos.arbol_b.NodoAB import NodoAB


class ArbolB:
    
    def __init__(self, orden: int):
        self.raiz: NodoAB = NodoAB(True)
        self.orden: int = orden    
    
    def insertar_vehiculo(self, vehiculo: Vehiculo):
        
        raiz: NodoAB = self.raiz
        self.insertar_vehiculo_no_completo(raiz, vehiculo)
        
        if len(raiz.get_claves()) > self.orden - 1:
            nueva_raiz: NodoAB = NodoAB(False)
            self.raiz = nueva_raiz
            nueva_raiz.get_hijos().insert(0, raiz)
            self.dividir_pagina(nueva_raiz, 0)
            
    
    def insertar_vehiculo_no_completo(self, raiz: NodoAB, vehiculo: Vehiculo):
        
        posicion: int = len(raiz.get_claves()) - 1
        
        if raiz.get_hoja():
            
            raiz.get_claves().append(None)
            
            while posicion >= 0 and vehiculo.get_placa() < raiz.get_claves()[posicion].get_placa():
                raiz.get_claves()[posicion + 1] = raiz.get_claves()[posicion]
                #raiz.get_claves().insert(posicion + 1, raiz.get_claves()[posicion])
                posicion -= 1
            
            raiz.get_claves()[posicion + 1] = vehiculo
        
        else:
            while posicion >= 0 and vehiculo.get_placa() < raiz.get_claves()[posicion].get_placa():
                posicion -= 1
            
            posicion += 1
            self.insertar_vehiculo_no_completo(raiz.get_hijos()[posicion], vehiculo)
            
            if len(raiz.get_hijos()[posicion].get_claves()) > self.orden - 1:
                self.dividir_pagina(raiz, posicion)
                
    def dividir_pagina(self, raiz: NodoAB, posicion: int):
        
        posicion_media: int = int((self.orden - 1) / 2)
        
        hijo: NodoAB = raiz.get_hijos()[posicion]
        nodo: NodoAB = NodoAB(hijo.get_hoja())
        
        raiz.get_hijos().insert(posicion + 1, nodo)
        
        raiz.get_claves().insert(posicion, hijo.get_claves()[posicion_media])
        
        nodo.set_claves(hijo.get_claves()[posicion_media + 1:])
        hijo.set_claves(hijo.get_claves()[:posicion_media])
        
        if not hijo.get_hoja():
            nodo.set_hijos(hijo.get_hijos()[posicion_media + 1:])
            hijo.set_hijos(hijo.get_hijos()[:posicion_media + 1])
            
    def buscar_vehiculo(self, placa: str):
        return self.buscar(placa, self.raiz)
            
    def buscar(self, placa: str, raiz: NodoAB) -> Vehiculo:
        
        if raiz is None:
            return None
        
        for vehiculo in raiz.get_claves():
            if vehiculo.get_placa() == placa:
                return vehiculo
        
        if raiz.get_hoja():
            return None
        
        posicion: int = len(raiz.get_claves()) - 1
        
        while posicion >= 0 and placa < raiz.get_claves()[posicion].get_placa():
            posicion -= 1
            
        posicion += 1
        
        return self.buscar(placa, raiz.get_hijos()[posicion])
    
    def recorrer_arbol(self, raiz: NodoAB, placas: list[str]):
        
        if raiz is not None:
            for vehiculo in raiz.get_claves():
                #print(vehiculo)
                placas.append(vehiculo.get_placa())
            
            if not raiz.get_hoja():
                for hijo in raiz.get_hijos():
                    self.recorrer_arbol(hijo, placas)
                    
    def obtener_placas(self) -> list[str]:
        
        placas: list[str] = []
        self.recorrer_arbol(self.raiz, placas)
        return placas
    
    def graficar_arbol(self):
        
        dot: str = 'digraph G {\n\tbgcolor="#F5F5F5";\n\t'
        dot += 'fontcolor=black;\n\tnodesep=0.5;\n\tsplines=false;\n\t'
        dot += 'label="Vehículos";\n\tlabelloc="t";\n\tfontsize=25;\n\t'
        dot += 'node [shape=record style=filled fillcolor="#004488" fontcolor="#F5F5F5" color=transparent];\n\t'
        dot += 'edge [fontcolor=white color="#ff5722"];\n\t'
        dot += self.graficar(self.raiz)
        dot += '\n}'
        
        return dot
    
    def graficar(self, nodo: NodoAB, id: list[int] = [0]) -> str:
        raiz: NodoAB = nodo
        
        arbol = f'n{id[0]} [label="'
        contador: int = 0
        
        for vehiculo in raiz.get_claves():
            
            if contador == len(raiz.get_claves()) - 1:
                arbol += f'<f{contador}> |{vehiculo.get_placa()}|<f{contador + 1}>'
                break
            
            arbol += f'<f{contador}> |{vehiculo.get_placa()}|'
            contador += 1
        
        arbol += '"];\n\t'
        
        contador: int = 0
        id_padre: int = id[0]
        
        for vehiculos in raiz.get_hijos():
            arbol += f'n{id_padre}:f{contador} -> n{id[0] + 1};\n\t'
            id[0] += 1
            arbol += self.graficar(vehiculos, id)
            contador += 1
            
        return arbol
    
    def esta_vacio(self):
        return self.raiz is None