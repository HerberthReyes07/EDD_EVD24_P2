
from src.estructura_datos.lista_circular_doblemente_enlazada.NodoLCDE import NodoLCDE
from src.modelo.Cliente import Cliente


class ListaCircularDoble:
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
    
    # Getters
    def get_cabeza(self):
        return self.__cabeza
    
    def get_cola(self):
        return self.__cola
    
    # Setters

    def set_cabeza(self, cabeza):
        self.__cabeza = cabeza

    def set_cola(self, cola):
        self.__cola = cola

    
    def insertar(self, cliente: Cliente):
        nuevo = NodoLCDE(cliente)
        if self.__cabeza is None:
            self.__cabeza = nuevo
            self.__cola = nuevo
            self.__cabeza.set_siguiente(self.__cola)
            self.__cola.set_anterior(self.__cabeza)
        else:
            recorrer = self.__cabeza.get_siguiente()
            insertado = False

            while recorrer != self.__cabeza:

                if cliente.get_dpi() < recorrer.get_cliente().get_dpi():
                    
                    if cliente.get_dpi() < self.__cabeza.get_cliente().get_dpi():
                        break
                    
                    nuevo.set_siguiente(recorrer)
                    nuevo.set_anterior(recorrer.get_anterior())
                    recorrer.get_anterior().set_siguiente(nuevo)
                    recorrer.set_anterior(nuevo)
                    insertado = True
                    break

                recorrer = recorrer.get_siguiente()
            
            if not insertado:
                nuevo.set_siguiente(self.__cabeza)
                nuevo.set_anterior(self.__cola)
                self.__cola.set_siguiente(nuevo)
                self.__cabeza.set_anterior(nuevo)

                if cliente.get_dpi() > self.__cola.get_cliente().get_dpi():
                    self.__cola = nuevo
                else:
                    self.__cabeza = nuevo

    def buscar(self, dpi: int) -> Cliente:
        
        if self.__cabeza is None:
            return None
        
        recorrer = self.__cabeza
        while True:
            if recorrer.get_cliente().get_dpi() == dpi:
                return recorrer.get_cliente()
            recorrer = recorrer.get_siguiente()
            if recorrer == self.__cabeza:
                return None

    def eliminar(self, dpi: int) -> bool:
        
        if self.__cabeza is None:
            return False
        
        recorrer = self.__cabeza
        while True:
            if recorrer.get_cliente().get_dpi() == dpi:
                
                if recorrer.get_siguiente() == recorrer:
                    self.__cabeza = None
                    self.__cola = None
                    return True
                
                recorrer.get_anterior().set_siguiente(recorrer.get_siguiente())
                recorrer.get_siguiente().set_anterior(recorrer.get_anterior())

                if recorrer == self.__cabeza:
                    self.__cabeza = recorrer.get_siguiente()
                
                if recorrer == self.__cola:
                    self.__cola = recorrer.get_anterior()
                
                return True
            
            recorrer = recorrer.get_siguiente()
            
            if recorrer == self.__cabeza:
                return False

    def graficar(self) -> str:
        
        if self.__cabeza is None:
            return 'Lista vacia'

        config: str = (
                        'bgcolor="#F5F5F5";\n\t'
                        'fontcolor=black;\n\t'
                        'label="Clientes";\n\t'
                        'labelloc="t";\n\t'
                        'nodesep=0.5;\n\t'
                        'node [fontsize = 4.5 shape=box style=filled fillcolor="#004488" '
                        'fontcolor="#F5F5F5" color=transparent];\n\t'
                        'edge [fontcolor=white color="#ff5722"];\n\t'
                    )
        defNodo: str = ''
        relNodo: str = ''
        encuadre: str = '{ rank=same; '

        recorrer = self.__cabeza
        id: int = 1

        while True:

            nodoActual: str = 'n' + id.__str__()
            contenido: str = (
                  '[label=\"dpi = ' + recorrer.get_cliente().get_dpi().__str__() 
                + '\\nNombres = '+ recorrer.get_cliente().get_nombres() 
                + '\\nApellidos = '+ recorrer.get_cliente().get_apellidos()
                + '\\nGenero = '+ ("Masculino" if recorrer.get_cliente().get_genero() == 'M' else "Femenino")
                + '\\nTelefono = '+ recorrer.get_cliente().get_telefono().__str__()
                + '\"];\n'
            )
            defNodo += nodoActual + contenido

            if recorrer != self.__cola:
                relNodo += nodoActual + "->n" + (id + 1).__str__() + ';\n'

            if recorrer != self.__cabeza:
                relNodo += nodoActual + "->n" + (id - 1).__str__() + ';\n'
            
            encuadre += nodoActual + "; "
            id += 1

            recorrer = recorrer.get_siguiente()
            if recorrer == self.__cabeza:
                break

        relNodo += 'n' + (id - 1).__str__() + '->n1[tailport=n headport=n];\n'
        relNodo += 'n1->n' + (id - 1).__str__() + '[tailport=s headport=s];\n'
        encuadre += '}'

        return 'digraph G {\n' + config + '\n' + defNodo + '\n' + relNodo + '\n' + encuadre + '\n}'  

    def esta_vacia(self) -> bool:
        return self.__cabeza is None

    def __str__(self):
        
        if self.__cabeza is None:
            return 'Lista vacia'
        
        cadena = ''
        recorrer = self.__cabeza

        while recorrer.get_siguiente() != self.__cabeza:
            cadena += recorrer.get_cliente().__str__() + '\n'
            recorrer = recorrer.get_siguiente()
        
        cadena += recorrer.get_cliente().__str__() + '\n'
        return cadena