from src.estructura_datos.grafo.Vertice import Vertice
from src.modelo.Ruta import Ruta
from src.estructura_datos.lista_simple.ListaSimple import ListaSimple


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
            
        vertice_origen.get_vecinos().insertar(Vertice(ruta.get_destino(), ruta.get_tiempo()))
        #vertice_destino.get_vecinos().insertar(Vertice(origen, ruta.get_tiempo()))
        
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