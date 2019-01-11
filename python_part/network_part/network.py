from flask import Flask


# env FLASK_APP=./python_part/network_part/network.py flask run


app = Flask(__name__)

@app.route('/hi')
def hi():
    return 'Hi world!'

@app.route('/hello')
def hello():
    return 'Hello world!'

@app.route('/')
def test():
    return 'test'