import sqlite3

connect = sqlite3.connect('device_info.db')
cursor = connect.cursor()

cursor.execute(''' 
               CREATE TABLE devices (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    location TEXT
                  )
               ''')

cursor.execute('''
                CREATE TABLE cameras (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    device_id INTEGER,
                    FOREIGN KEY(device_id) REFERENCES devices(id)
                  )
                ''')

connect.commit()
connect.close()