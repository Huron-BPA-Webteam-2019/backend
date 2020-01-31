from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/ping')
@app.route('/')
def ping():
    return 'pong!'
if __name__ == '__main__':
    app.run(port=5000)