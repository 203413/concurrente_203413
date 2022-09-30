import os
import threading
import time
mutex = threading.Lock()

personas = [1,2,3,4,5,6,7,8]
estado=["en espera","en espera","en espera","en espera","en espera","en espera","en espera","en espera"]
palitos =  [1,2,3,4,5,6,7,8]

def Mesa(id):
    mutex.acquire()
    print("Persona numero: "+str(personas[id])+" esta usando los palillos: "+str(palitos[id])+" y "+str(palitos[id-1]))
    estado[id]="Comiendo..."
    for k in range(0,8):
        print("El estado de la persona número: "+str(personas[k])+" es: "+estado[k])
    estado[i]="Ya comio"
    mutex.release()
    
for i in range(0,8):
    os.system ("cls")
    #time.sleep(2)
    print("\n")
    print("=Mesa=")

    th1 = threading.Thread(target=Mesa,args=[i])
    th1.start()
    time.sleep(4)
   
os.system ("cls")
print("\n=Estado final=")
for k in range(0,8):
    print("El estado de la persona número: "+str(personas[k])+" es: "+estado[k])

