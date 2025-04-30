from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Example sensor data
sensor_data = {
    "pH": 8.5,
    "temperature": 27.0,
    "humidity": 50.0,
    "light_level": 1500,  # New data
    "water_level": 50.0,  # New data
}

@app.route('/api/sensor-data', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data)

@app.route('/api/toggle-lights', methods=['POST'])
def toggle_lights():
    data = request.json
    lights_on = data.get('lightsOn', False)
    # Add logic to control lights (e.g., send a signal to an IoT device)
    return jsonify({"status": "success", "lightsOn": lights_on})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')
    # Add logic to verify username and password
    if username == 'admin' and password == 'password':
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == '__main__':
    app.run(debug=True)