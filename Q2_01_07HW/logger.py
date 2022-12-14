import os
from datetime import datetime as dt

def log_request(i, data):
    event_dt = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    if (os.path.isfile('Log.txt')): id = sum(1 for line in open('Log.txt','r'))
    else: id = 0 
    with open('Log.txt', 'a') as file :
        file.write('{};{};Тип запроса:{};Абонент:{}\n'.format(id, event_dt, i, data))
    return "Запрос записан в файл."

def add_list_entry(data):
    event_dt = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    if (os.path.isfile('PhoneList.txt')): id = sum(1 for line in open('PhoneList.txt','r'))
    else: id = 0 
    with open('PhoneList.txt', 'a') as file :
        file.write('{};{}\n'.format(data[0],data[1]))
    return "Абонент записан в справочник."
