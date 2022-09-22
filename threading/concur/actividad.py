import requests
import time
import pymysql
import concurrent.futures
import threading
import pytube
from dotenv import load_dotenv
import os 

load_dotenv()
MYSQL_DB= os.getenv("MYSQL_DB")
MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_PASS=os.getenv("MYSQL_PASS")

# Servicios
def get_services():
    response = requests.get('https://randomuser.me/api')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
    else:
        get_services()
        

# Videos
def descargar(y):
    links = ['https://youtu.be/fMLGmcv7ALI','https://youtu.be/LC8pjATYoj0','https://youtu.be/FjmaCW7cA08','https://youtu.be/4w4bTJ335QE','https://youtu.be/3WJWEbN1Phk']
    SAVE_PATH = "C:/Users/marco/Desktop/Python/videos"
    yt = pytube.YouTube(links[y])
    stream = yt.streams.first()
    stream.download(SAVE_PATH)


# Datos a DB
try: 
    conexion = pymysql.connect(database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASS)
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
    print('Error')


def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service,url)

def get_service(url):
    r = requests.get(url)
    data = r.json()
    photos = data
    for photo in photos:
        write_db(photo["title"])

def connect_db():
    pass

def close_conexion():
    conexion.close()

def write_db(title):
    try:
        cursor1.execute("insert into pokemons2 (name) values ('"+title+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()




if __name__ == "__main__":
    url_site = ["https://jsonplaceholder.typicode.com/photos"]

    for x in range(0,50):
        th1 = threading.Thread(target=get_services)
        th1.start()
        time.sleep(0.3)

    for y in range(0,5):
        th2 = threading.Thread(target=descargar, args=[y])
        th2.start()

    th3 = threading.Thread(target=service, args=[url_site,])
    th3.start()

    #service(url_site)  