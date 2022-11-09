import sqlite3

conn = sqlite3.connect(r'C:\Users\rogev\Documents\!Учеба\!Дз\Архитектура развертывания\курсач\djangoProject\db.sqlite3')
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS guest;""")
cur.execute("""DROP TABLE IF EXISTS participant;""")
cur.execute("""DROP TABLE IF EXISTS organizer;""")
cur.execute("""DROP TABLE IF EXISTS event;""")
cur.execute("""DROP TABLE IF EXISTS place;""")
cur.execute("""DROP TABLE IF EXISTS event_type;""")

cur.execute("""CREATE TABLE IF NOT EXISTS place
    (eplace TEXT PRIMARY KEY, 
    capacity integer NOT NULL, 
    equipment TEXT);""")

cur.execute("""CREATE TABLE IF NOT EXISTS event_type
    (etype TEXT PRIMARY KEY);""")

cur.execute("""CREATE TABLE IF NOT EXISTS event 
    (event_title TEXT PRIMARY KEY, 
    etype TEXT NOT NULL,   
    eplace TEXT NOT NULL,   
    edate TEXT, 
    duration TEXT, 
    registration TEXT DEFAULT 'False',
    FOREIGN KEY (etype) REFERENCES event_type(etype)
    FOREIGN KEY (eplace) REFERENCES place(eplace));""")

cur.execute("""CREATE TABLE IF NOT EXISTS organizer
    (id_organizer INTEGER PRIMARY KEY AUTOINCREMENT,
    event_title TEXT NOT NULL, 
    fullname TEXT NOT NULL,
    contact_phone INTEGER NOT NULL,
    FOREIGN KEY (event_title) REFERENCES event(event_title));""")

cur.execute("""CREATE TABLE IF NOT EXISTS participant
    (id_participant INTEGER PRIMARY KEY AUTOINCREMENT,
    event_title TEXT NOT NULL, 
    fullname TEXT NOT NULL,
    contact_phone INTEGER NOT NULL,
    pgroup TEXT,
    FOREIGN KEY (event_title) REFERENCES event(event_title));""")

cur.execute("""CREATE TABLE IF NOT EXISTS guest
    (id_organizer INTEGER PRIMARY KEY AUTOINCREMENT,
    event_title TEXT NOT NULL,  
    fullname TEXT NOT NULL,
    contact_phone INTEGER NOT NULL,
    FOREIGN KEY (event_title) REFERENCES event(event_title));""")




