from src.estructura_datos.lista_simple.NodoLS import NodoLS
from src.estructura_datos.cola.Cola import Cola
from src.estructura_datos.grafo.Vertice import Vertice
from src.modelo.Ruta import Ruta
from src.estructura_datos.lista_simple.ListaSimple import ListaSimple
from copy import copy


class ListaAdyacencia:
    def __init__(self):
        self.__vertices = ListaSimple()
        
    def get_vertices(self):
        return self.__vertices
    
    def set_vertices(self, vertices):
        self.__vertices = vertices
        
    def insertar_ruta(self, ruta: Ruta):
        origen = ruta.get_origen()
        #destino = ruta.get_destino()
        
        vertice_origen = self.__vertices.buscar_ciudad(origen)
        #vertice_destino = self.__vertices.buscar_ciudad(destino)
        
        if vertice_origen is None:
            vertice_origen = Vertice(origen)
            self.__vertices.insertar(vertice_origen)
        
        """ if vertice_destino is None:
            vertice_destino = Vertice(destino)
            self.__vertices.insertar(vertice_destino) """
        
        vecino = Vertice(ruta.get_destino(), ruta.get_tiempo())
        vecino.set_peso_acumulado(ruta.get_tiempo())    
        vertice_origen.get_vecinos().insertar(vecino)
        #vertice_destino.get_vecinos().insertar(Vertice(origen, ruta.get_tiempo()))
        
    def obtener_ruta(self, origen: str, destino: str) -> ListaSimple:
        ruta: ListaSimple[Vertice] = ListaSimple()
        nodos_visitados: Cola[Vertice] = Cola()
        nodos: Cola[Vertice] = Cola()
    
        origen:Vertice = copy(self.__vertices.buscar_ciudad(origen))
        
        if origen is None:
            print('No se encontro el origen')
            return None
        
        nodos.encolar(origen)
        
        resultado: Vertice = self.obtener_ruta_corta(destino, nodos_visitados, nodos)
        
        while resultado is not None:
            ruta.insertar_frente(resultado)
            resultado = resultado.get_padre()
            
        return ruta
        
    def obtener_ruta_corta(self, destino: str, nodo_visitados: Cola, nodos:Cola) -> Vertice:
        
        origen: Vertice = nodos.desencolar().get_valor()
        
        if origen.get_ciudad() == destino:
            nodo_visitados.encolar(origen)
            return origen
        
        aux: NodoLS[Vertice] = origen.get_vecinos().get_cabeza()
        
        while aux is not None:
            
            if not self.esta_visitado(aux.get_valor(), nodo_visitados):
                peso: int = aux.get_valor().get_peso()
                vecino: Vertice = copy(self.__vertices.buscar_ciudad(aux.get_valor().get_ciudad()))
                vecino.set_peso(peso)
                vecino.set_peso_acumulado(origen.get_peso_acumulado() + peso)
                vecino.set_padre(origen)
                
                nodos.encolar(vecino)
        
            aux = aux.get_siguiente()
            
        nodos.ordenar()
        nodo_visitados.encolar(origen)
        
        return self.obtener_ruta_corta(destino, nodo_visitados, nodos)
    
    def esta_visitado(self, vertice: Vertice, nodos_visitados: Cola) -> bool:
        
        result = nodos_visitados.buscar(vertice.get_ciudad())
        return result is not None
    
    def esta_vacia(self) -> bool:
        return self.__vertices.esta_vacia()
        
    def graficar(self) -> str:
        
        dot = 'graph G {\n\t'
        dot += 'layout="neato";\n\t'
        dot += 'overlap="false";\n\t'
        dot += 'splines="true";\n\t'
        
        config: str = (
                        'bgcolor="#F5F5F5";\n\t'
                        'fontcolor=black;\n\t'
                        'label="Rutas";\n\t'
                        'labelloc="t";\n\t'
                        'fontsize=25;\n\t'
                        'node [style=filled fillcolor="#004488" '
                        'fontcolor="#F5F5F5" color=transparent];\n\t'
                        'edge [fontcolor=black color="#ff5722"];\n\t'
                    )
        dot+= config
        
        ciudades = []
        recorrer = self.__vertices.get_cabeza()
        cont: int = 0
        
        while recorrer is not None:
            ciudades.append(recorrer.get_valor().get_ciudad())
            dot += f'n{cont}[label="{recorrer.get_valor().get_ciudad()}"];\n\t'
            cont += 1
            recorrer = recorrer.get_siguiente()
        
        
        recorrer_vertices = self.__vertices.get_cabeza()
        
        while recorrer_vertices is not None:
            
            recorrer_vecinos = recorrer_vertices.get_valor().get_vecinos().get_cabeza()
            
            while recorrer_vecinos is not None:
                
                index_p = ciudades.index(recorrer_vertices.get_valor().get_ciudad())
                index_h = ciudades.index(recorrer_vecinos.get_valor().get_ciudad())
                
                if index_p < index_h:
                    dot += f'n{index_p} -- n{index_h}'
                    dot += f'[label="{recorrer_vecinos.get_valor().get_peso()}", len="2"];\n\t'    
                
                recorrer_vecinos = recorrer_vecinos.get_siguiente() 
            
            recorrer_vertices = recorrer_vertices.get_siguiente()
        
        return dot + '\n}'