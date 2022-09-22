from os import link
from threading import Thread, Semaphore
import pytube
semaforo = Semaphore(1)

def critico(id):
    #print(id)
    links = ['https://youtu.be/fMLGmcv7ALI','https://youtu.be/xv8iT_D1y9s','https://youtu.be/FjmaCW7cA08']
    global x;
    print("Hilo = "+str(id)+" => "+ links[id])
    SAVE_PATH = "C:/Users/marco/Documents/PRUEBAAA"
    yt = pytube.YouTube(links[id])
    stream = yt.streams.first()
    stream.download(SAVE_PATH)
    print("Video descargado")
    x=0

class Hilo(Thread):
    def __init__(self,id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        semaforo.acquire()
        critico(self.id)
        semaforo.release()

thread_semaforo = [Hilo(0),Hilo(1),Hilo(2)]
x=0;
for t in thread_semaforo:
    t.start()