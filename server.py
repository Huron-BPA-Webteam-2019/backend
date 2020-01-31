from flask import Flask
from flask import request
import requests
import json
app = Flask(__name__)

@app.route('/ping')
@app.route('/')
def ping():
    return 'pong!'
@app.route('/calculate'):
    response = requests.get('https://api.myjson.com/bins/14s9u2').json()
    rooms = request.args.get("rooms")
    sqft = request.args.get("sqft")
    greenft = request.args.get("greenft")
    return f'''
    {response['a']}, {response['b']}, {response['c']}
    rooms {rooms}
    sqft {sqft}
    greenft {greenft}
    '''
if __name__ == '__main__':
    app.run(port=5000)
