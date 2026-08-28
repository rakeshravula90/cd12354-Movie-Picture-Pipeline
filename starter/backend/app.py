from flask import Flask, redirect
from flask_cors import CORS
from movies import movies_api

app = Flask(__name__)

CORS(app)

app.register_blueprint(movies_api)

@app.route("/")
def home():
    return redirect("/movies")