from flask_API import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

PATH = 'device_info.db'

@app.route('\devices', methods = ['GET'])

def get_devices():


def get_cameras():
