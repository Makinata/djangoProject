import sqlite3
from sqlite3 import Error

def magic(req):
    try:
        conn = sqlite3.connect(r'C:\Users\rogev\Documents\!Учеба\!Дз\Архитектура развертывания\курсач\app\db.sqlite3')
        cur = conn.cursor()
        cur.execute(f"{req}")
        try:
            resp = str(cur.fetchall())
        except:
            resp = 'Запрос выполнен'
    except (Exception, Error) as error:
        resp = str(error)
    return resp