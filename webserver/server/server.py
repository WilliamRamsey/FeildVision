from flask import Flask, request, Response
import json
from datastructure import *


test_device = Device(1)

app = Flask(__name__)

@app.route('/')
def index():
    return open('C:/Users/willi/OneDrive/Desktop/Field-Vision/webserver/client/index.html', 'r').read()

# @app.route('/<name>')
# def print_name(name):
#     return f'Hello {name}'

@app.route('/api/devices', methods=['GET', 'POST'])
def return_device():
    if request.method == 'GET':
        return json.dumps(test_device()), 200, {"Content-Type": "application/json"}

@app.route('/resources/getdevices.js')
def return_javascript():
    if request.method == 'GET':
        return open('C:/Users/willi/OneDrive/Desktop/Field-Vision/webserver/client/resources/getdevices.js').read(), 200, {"Content-Type": "text/javascript"}

app.run()
