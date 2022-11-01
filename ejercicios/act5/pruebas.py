from threading import Thread, Condition
import time

items = []
condition = Condition()

class Consumer(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def consume(self):
        global condition
        global items
        
        condition.acquire()
        
        # if not items:
        #     print("No hay items para consumir")
        #     condition.wait()
        #     print("Se agregó un item")
        # items.pop()
        # condition.notify()
        # condition.release()
        
        while len(items) == 0:
            condition.wait()
            print("Notificación de consumo: No hay items para consumir")
        items.pop()
        
        print('Notificación de consumo: Se consumió un item')
        print('Notificación de consumo: Items consumibles: ', len(items))
        
        condition.notify()
        condition.release()
    
    def run(self):
        for i in range(20):
            time.sleep(10)
            self.consume()
            
class Producer(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def produce(self):
        global condition
        global items
        
        condition.acquire()
        
        while len(items) == 10:
            condition.wait()
            print("Notificación de producción: Los items producidos son", len(items))
            print('Notificación de producción: Producción detenida')
        items.append(1)
        
        print('Notificación de producción: Items restantes: ', len(items))
        
        condition.notify()
        condition.release()
        
    def run(self):
        for i in range(20):
            time.sleep(5)
            self.produce()

if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    
    producer.start()
    consumer.start()
    
    producer.join()
    consumer.join()