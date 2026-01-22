from flask import Flask
app = Flask(__name__)
@app.route('/api/v1/auth')
def auth():
    return {"authorized": True, "role": "admin"}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)