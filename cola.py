# -*- coding: utf-8 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def primero(self):
        return self.items[0]

    def unir(self,otro):
          self.items=self.items+otro.items
    
    def ordenar(self):
        self.items=sorted(self.items, key=lambda lib: lib.Autor)

    

    def ordenar_2(self):
        cola=Cola()
        prim=self.primero()
        while ((self.primero().Autor == prim.Autor) and self.es_vacia()==False):
            for v in self.items:
                if prim.Autor == v.Autor:
                    cola.encolar(v)
                    self.desencolar()
            if self.es_vacia()==True:
                break
                
        cola.ordenar_3()
        return cola
    
    def ordenar_3(self):
        self.items=sorted(self.items, key=lambda lib: lib.Titulo)
        
    def imprimir(self):
        for v in self.items:
            print(v.Autor+" "+v.Titulo)

            
        
