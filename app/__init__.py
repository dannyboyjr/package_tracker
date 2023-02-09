from flask import Flask, render_template
from .config import Config


app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
def index():
    return '<h1>Hello World </h1>'