from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "<h1>Hey Coder, Welcome to homepage</h1>"

@app.route("/wish", methods=["GET"])
def wishpage():
    return "<h1>We wish you happy coding</h1>"

@app.route("/add/<num1>/<num2>", methods=["GET"])
def addition(num1, num2):
    return f"<h1>{num1} + {num2} = {int(num1) + int(num2)}</h1>"

@app.route("/sub/<num1>/<num2>", methods=["GET"])
def subtraction(num1, num2):
    return f"<h1>{num1} - {num2} = {int(num1) - int(num2)}</h1>"

@app.route("/mul/<num1>/<num2>", methods=["GET"])
def multiplication(num1, num2):
    return f"<h1>{num1} x {num2} = {int(num1) * int(num2)}</h1>"

@app.route("/div/<num1>/<num2>", methods=["GET"])
def division(num1, num2):
    return f"<h1>{num1} / {num2} = {int(num1) / int(num2)}</h1>"