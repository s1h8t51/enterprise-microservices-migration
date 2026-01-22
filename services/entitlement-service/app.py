from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/entitlements', methods=['GET'])
def get_entitlements():
    # This represents the logic moved out of the Broadcom monolith
    return jsonify({
        "status": "success",
        "data": [
            {"id": 1, "name": "Enterprise License", "active": True},
            {"id": 2, "name": "Telemetry Dashboard", "active": False}
        ],
        "message": "Data served from Microservice"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)