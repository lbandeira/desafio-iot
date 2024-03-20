import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# 1. Ajustar para atualizar o database
# 2. Utilizar o postman para envio do .json

app = Flask(__name__)
CORS(app)

def read_devices_from_json():
    with open('devices.json', 'r') as file:
        return json.load(file)

def update_database(data):
    connect = sqlite3.connect('device_info.db')
    cursor = connect.cursor()
    # Criar tabela caso nao tenha
    cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS devices (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        camera_count INTEGER
                    )
                ''')
    
    # Apaga os dados existentes
    cursor.execute("DELETE FROM devices")

    # Adiciona linha
    for devices in data:
        query = f'''INSERT INTO devices (id, name, camera_count) VALUES ("{devices['id']}", "{devices['name']}", "{len(devices['cameras'])}")'''
        print(query)
        cursor.execute(query)

    connect.commit()
    connect.close()

@app.route('/update_devices', methods=['POST'])

def update_devices():
    #data = request.get_json()
    data = read_devices_from_json()
    if data:
        update_database(data)
        return jsonify({"message": "Database updated successfuly"}), 200
    else:
        return jsonify({"error": "Invalid JSON data"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)