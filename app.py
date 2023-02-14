from flask import Flask, render_template, jsonify
from utils import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    congratulations = load_congratulations()
    return render_template('hp_gosha.html', congratulations=congratulations)


if __name__ == '__main__':
    app.run()
