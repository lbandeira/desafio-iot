import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from cryptography.fernet import Fernet

app = Flask(__name__)
CORS(app)

key = Fernet.generate_key()
cipher = Fernet(key)

def read_devices_from_json():
    with open('devices.json', 'r') as file:
        return json.load(file)

def update_database(data):
    # Aplicar camada de seguranca em dados sensiveis
    for device in data:
        if 'password' in device:
            encrypted_password = cipher.encrypt(device['password'].encode())
            device['password'] = encrypted_password.decode()
        if 'key' in device:
            encrypted_password = cipher.encrypt(device['key'].encode())
            device['key'] = encrypted_password.decode()

    connect = sqlite3.connect('device_info.db')
    cursor = connect.cursor()
    # Cria tabela de dispositivos
    cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS devices (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        username TEXT,
                        password TEXT,
                        key TEXT,
                        camera_count INTEGER
                    )
                ''')
    
    # Cria tabela de cameras
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS cameras (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    rtsp TEXT,
                    snapshot TEXT,
                    username TEXT,
                    password TEXT,
                    device_id TEXT,
                    FOREIGN KEY(device_id) REFERENCES devices(id)
                  )''')
    
    # Apaga os dados existentes
    cursor.execute("DELETE FROM devices")

    # Adiciona linha na tabela
    for devices in data:
        cameras = devices['cameras']
        query = f'''INSERT INTO devices (
                            id, 
                            name, 
                            username, 
                            password, 
                            key,
                            camera_count) 
                    VALUES (
                        "{devices['id']}", 
                        "{devices['name']}", 
                        "{devices['username']}", 
                        "{devices['password']}", 
                        "{devices['key']}", 
                        "{len(devices['cameras'])}")'''
        cursor.execute(query)
        for index, camera in enumerate(cameras):
            query = f'''INSERT INTO cameras (
                                id, 
                                name, 
                                rtsp,
                                snapshot,
                                username, 
                                password,
                                device_id) 
                        VALUES (
                            "{camera['id']}", 
                            "{camera['name']}", 
                            "{camera['rtsp']}", 
                            "{camera['snapshot']}", 
                            "{camera['username']}", 
                            "{camera['password']}", 
                            "{devices['id']}")'''
            cursor.execute(query)
    #print(cameras[0]['id'])
    connect.commit()
    connect.close()

# def decrypted():
#     # Retrieve encrypted data from SQLite database and decrypt
#     conn = sqlite3.connect('device_info.db')
#     cursor = conn.cursor()

#     cursor.execute('SELECT * FROM devices;')
#     for row in cursor.fetchall():
#         decrypted_password = cipher.decrypt(row[3].encode()).decode()
#         print(f"Name: {row[1]}, Username: {row[2]}, Decrypted Password: {decrypted_password}")

#     conn.close()    

@app.route('/update_devices', methods=['POST'])
def update_devices():
    #Recebe JSON pela requisicao
    data = request.get_json()

    #Faz leitura do JSON de forma local
    #data = read_devices_from_json()
    if data:
        update_database(data)
        return jsonify({"message": "Database updated successfuly"}), 200
    else:
        return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/devices', methods = ['GET'])
def get_devices():
    connection = sqlite3.connect('device_info.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    connection.close()
    return jsonify(devices)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)