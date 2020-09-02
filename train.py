from flask import send_from_directory
from glob import glob
from flask import Flask
import os
from random import choice

app = Flask(__name__)

def imagesWith(prefix):
    types = "png jpg jpeg".split()
    images = []
    path = "static/img"
    for type in types:
        images.extend(glob(os.path.join(path, prefix+"*."+type)))
    return images

@app.route('/')
def index():
    return send_from_directory("static", "train.html")

@app.route("/img/<path>")
def img_path(path):
    return send_from_directory("static/img/", path)

@app.route('/ground')
def img_ground():
    path = choice(imagesWith("ground_"))
    print(path)
    return send_from_directory(*os.path.split(path))

@app.route('/air')
def img_air():
    path = choice(imagesWith("air_"))
    return send_from_directory(*os.path.split(path))



if __name__ == "__main__":
    app.run(port=5555)
