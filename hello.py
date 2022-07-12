#To run the appliation
    # export FLASK_APP=hello
    # flask run
# To make the server ublicily available
#   flask run --host=0.0.0.0
# To run Falsk with all development features
    # export FLASK_ENV=development
    # flask run

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"