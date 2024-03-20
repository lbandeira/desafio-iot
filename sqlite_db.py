import sqlite3
from flask import Flask, request, jsonify

# 1. Ajustar para atualizar o database
# 2. Utilizar o postman para envio do .json

app = Flask(__name__)

def update_database(data):
    connect = sqlite3.connect('device_info.db')
    cursor = connect.cursor()
    # Criar tabela caso nao tenha
    cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS devices (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        location TEXT
                    )
                ''')
    # Adiciona linha
    for device in data['devices']:
        cursor.execute("INSERT INTO devices (id, name, camera_count, location) VALUES (?, ?, ?, ?)",
                  (device['id'], device['name'], len(device['cameras']), device['location']))

    connect.commit()
    connect.close()

@app.route('/update_devices', methods=['POST'])

def update_devices():
    data = request.get_json()
    if data:
        update_database(data)
        return jsonify({"message": "Database updated successfuly"}), 200
    else:
        return jsonify({"error": "Invalid JSON data"}), 400

if __name__ == "__main__":
    app.run(debug=True)