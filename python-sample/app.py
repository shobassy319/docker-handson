from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '{"message": "Hello"}'

@app.route('/ping')
def ping():
    return '{"message": "pong"}'