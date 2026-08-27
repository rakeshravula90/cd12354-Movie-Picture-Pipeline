from flask import Flask, redirect
from movies import movies_api

app = Flask(__name__)

app.register_blueprint(movies_api)


@app.route("/")
def home():
    return redirect("/movies")