# Existen uno o más productores y uno o más consumidores, todos 
# almacenan y extraen productos de una misma bodega. 
# El productor produce productos cada vez que puede, y el consumidor 
# los consume cada vez que lo necesita.

# Problema:
# coordinar a los productores y consumidores, para que los productores 
# no produzcan más ítems de los que se pueden almacenar en el momento, y 
# los consumidores no adquieran más ítems de los que hay disponibles.

import threading
import time
mutex = threading.Lock()
mutex2= threading.Lock()
import random

PERSONAS = 3
PRODUCTORES = 1
ALMACEN = ['P','P','P','P','P','P','P','P','P','P']

IT = 10

def productores(caso):
    if (caso==0):
        global PRODUCTORES
        global ALMACEN
        PRODUCTORES = PRODUCTORES + 1
        nProductos=PRODUCTORES*10
        #ALMACEN = ALMACEN + nProductos
        for i in range (0,nProductos):
            ALMACEN.append('P')
        print('⚠ Demanda muy alta ⚠  añadiendo nuevo productor. Hay '+str(nProductos)+' productos nuevos en el almacen')
    else:
        return PRODUCTORES

def almacen(caso):
    global ALMACEN
    global PERSONAS
    if (caso==1):
        return len(ALMACEN)
    else:
        #ALMACEN = ALMACEN - PERSONAS
        longitud=0
        for i in range(0,PERSONAS):
            longitud=len(ALMACEN)
            longitud=longitud-1
            numero=random.randint(0,longitud)
            ALMACEN.pop(0)

def consume(caso):
    global PERSONAS
    if(caso==1):
        PERSONAS = PERSONAS + 1
    else:
        return PERSONAS

class Proceso(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id

    def consumir(self):
        mutex.acquire()
        print('   🔴  Hilo #'+str(self.id))
        consume(1)
        consumidores=consume(0)
        consulta=almacen(1)
        aux=consulta-consumidores

        if (aux<=0):
            mutex2.acquire()
            productores(0)
            consulta=almacen(1)
            time.sleep(1)
            mutex2.release()

        almacen(0)
        print('Hay '+str(consumidores)+' consumidores')
        print('Hay '+str(consulta)+' productos en el almacen') 
        
    def estado(self):
        produc=productores(1)
        auxAlmacen=almacen(1)
        print('Hay '+str(produc)+' productores')
        print('==== Los consumidores han consumido los productos, quedan '+str(auxAlmacen)+'\n')
        time.sleep(1)
        mutex.release()
    
    def run(self):
        self.consumir()
        self.estado()


def main():

    for i in range(0,20):
        hilo = Proceso(i)
        hilo.start()


if __name__ == '__main__':
    main()
