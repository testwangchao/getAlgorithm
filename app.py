from flask import Flask
from utils import open_door

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/open/')
def open():
    if open_door():
        return "success"
    return "联系王超"


if __name__ == '__main__':
    app.run()