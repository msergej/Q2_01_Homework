          # Модуль для записи резуьтатов вычислений.
import os
from datetime import datetime as dt

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    event_dt = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    if (os.path.isfile('Log.txt')): id = sum(1 for line in open('Log.txt','r'))
    else: id = 0 
    with open('Log.txt', 'a') as file :
        file.write('{};{};Задание:{};Результат:{}\n'.format(id, event_dt, expr, result))
    return "Задание и результат успошно добавлены в жунал."

def get_history() -> str:
    """Возвращает содержимое файла с результатами вычислений"""
    with open('Log.txt') as f: return f.read()
