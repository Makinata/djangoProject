import sqlite3

def magic(req):
    conn = sqlite3.connect(r'C:\Users\rogev\Documents\!Учеба\!Дз\Архитектура развертывания\курсач\djangoProject\db.sqlite3')
    cur = conn.cursor()
    cur.execute(f"{req}")
    resp = cur.fetchall()

    return resp