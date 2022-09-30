import threading
from xml.dom.expatbuilder import theDOMImplementation
import pytube

mutex=threading.Lock()
def crito(id):
    links = ['https://youtu.be/fMLGmcv7ALI','https://youtu.be/xv8iT_D1y9s','https://youtu.be/FjmaCW7cA08']
    global x;
    print("Hilo = "+str(id)+" => "+ links[id])
    SAVE_PATH = "C:/Users/marco/Documents/PRUEBAAA/otro"
    yt = pytube.YouTube(links[id])
    stream = yt.streams.first()
    stream.download(SAVE_PATH)
    print("Video descargado")
    x=0

class Hilo(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        crito(self.id)
        mutex.release()


hilos = [Hilo(0),Hilo(1),Hilo(2)]
x=0
for h in hilos: 
    h.start()