from flask import Flask
from flask import request
from flask import Response
import requests
import json
app = Flask(__name__)

@app.route('/ping')
@app.route('/')
def ping():
    response.headers.add('Access-Control-Allow-Origin', '*')
    return 'pong!'
@app.route('/price')
def price():
    data = requests.get('https://api.myjson.com/bins/14s9u2').json()
    rooms = request.args.get("rooms")
    sqft = request.args.get("sqft")
    greenft = request.args.get("greenft")
    val = calculate(rooms, sqft, greenft, data)
    resp = Response(val)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def calculate(rooms, sqft, greenft, data):
    # Remove data parameter later, just for testinf
    return data['a'] * rooms + data['b'] * sqft + data['c'] * greenft
if __name__ == '__main__':
    app.run(port=5000)
