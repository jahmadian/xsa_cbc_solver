from flask import Flask
from cfenv import AppEnv
import os
import time
from datetime import datetime
from solver import pulp_solver

app = Flask(__name__)
env = AppEnv()

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

port = int(os.environ.get('PORT', 5000))


@app.route("/")
def hello():
    now = datetime.now().time()
    later = datetime.now().time()
    return "<h1 style='color:blue'>Hello There!\nthe func called at {now}\nthe func respond at {later} </h1>".format(now=str(now), later=str(later))


@app.route('/pulp_test')
def solver1():
    msg = pulp_solver()

    return msg


if __name__ == "__main__":
    app.run(port=port)
