import urllib3
import certifi
import time
import json

class config_loader():
    def __init__(self):
        try:
            config = open('config.json', encoding='utf-8')
            conf = json.load(config)
            self.login = conf['tsu_ipoe_login']
            self.password = conf['tsu_ipoe_password']
            self.delay = int(conf['delay'])
        except FileNotFoundError:
            print("no config file found")
            self.login = 'login'
            self.password = 'password'
            self.delay = int(30)
   
def login():
    cl = config_loader()
    http = urllib3.PoolManager(ca_certs=certifi.where())
    url = 'https://ipoe.tsutmb.ru/'
    req = http.request('POST', url, fields={'tsu_ipoe_login': cl.login ,'tsu_ipoe_password': cl.password})
    print('trying to connect ipoe.tsutmb.ru')
    wrong_str = 'Неправильный логин или пароль'
    if (wrong_str in req.data.decode('utf-8')):
        print("wrong login or password")
    else:
        print("you are logged in")
    
def amionline():
    try:
        http = urllib3.PoolManager(ca_certs=certifi.where())
        url = 'https://ya.ru/'
        resp = http.request('GET', url)
        print("you've been already connected")
        return 1
    except:
        print("you aren't connected")
        return 0
    
def stayonline():
    if (amionline() == 0):
        login()
        
cl = config_loader()
delay = cl.delay
while(1>0):
       stayonline()
       time.sleep(delay)


        
