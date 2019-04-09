from pila import *
from libro import *
from cola import *

def leer():
    archivo=open('biblioteca.txt','r')
    g=archivo.read()
    archivo.close()
    f=g.splitlines()    
    return f

def iterar(a):
    cola=Cola()
    while(a!=[]):
        lib=a[0].split()
        libro=Libro(lib[0],lib[1],lib[2],lib[3],lib[4])
        cola.encolar(libro)
        print(a[0])
        a.pop(0)
    return cola

def escribir(cola):
    archivo=open('biblioteca_ordenada.txt','w')
    for v in cola:
        archivo.write(v.Autor+" "+v.Titulo+" "+v.Tematica+" "+v.Paginas+" "+v.Editorial)
    
    archivo.close()


cola_1=Cola()
cola_2=Cola()
coal_3=Cola()
f=leer()
cola_1=iterar(f)
cola_1.ordenar()

while cola_1.es_vacia()==False:
    aux=Cola()
    aux=cola_1.ordenar_2()
    cola_2.unir(aux)
    cola_3=aux
   
cola_2.imprimir()
escribir(cola_2)



    



        
