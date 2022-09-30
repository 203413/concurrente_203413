import threading

mutex = threading.Lock()
def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(threading.Thread):
     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        mutex.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id)
        mutex.release() #Libera un semáforo e incrementa la varibale

hilos = [Hilo(1), Hilo(2)]
x=1;
for h in hilos:
    h.start()