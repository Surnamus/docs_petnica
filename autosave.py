from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import json
import os

app = Flask(__name__)

data_store = {
    'user_data': '192.168.0.137'
}

save_path = 'autosave.json'

def save_data():
    with open(save_path, 'w') as f:
        json.dump(data_store, f)
    print("Data autosaved")

def load_data():
    if os.path.exists(save_path):
        with open(save_path, 'r') as f:
            return json.load(f)
    return data_store

data_store = load_data()

@app.route('/update', methods=['POST'])
def update_data():
    data = request.json
    data_store['user_data'] = data.get('user_data', data_store['user_data'])
    return jsonify({"message": "Data updated"}), 200

@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(data_store), 200

scheduler = BackgroundScheduler()
scheduler.add_job(func=save_data, trigger="interval", seconds=30)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)