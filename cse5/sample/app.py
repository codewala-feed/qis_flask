from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def homepage():
    return "<h1>Hey Coder, Welcome to the homepage</h1>"

@app.route("/sample", methods = ["GET", "POST"])
def sample():
    return "Hey Coder, Welcome to the sample page"