# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my Flask app!"

@app.route('/api/data')
def data():
    return jsonify({"message": "This is sample data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
