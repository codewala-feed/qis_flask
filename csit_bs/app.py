from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "Hey Coder, Welcome to homepage"

@app.route("/sample", methods=["GET"])
def samplePage():
    return "<h1>You are in Sample Page</h1>"

@app.route("/add/<num1>/<num2>", methods=["GET"])
def addition(num1, num2):
    return f"<h1>Sum of {num1} + {num2} = {int(num1) + int(num2)}</h1>"

@app.route("/sub/<num1>/<num2>", methods=["GET"])
def subtraction(num1, num2):
        return f"<h1>Diff of {num1} - {num2} = {abs(int(num1)-int(num2))}</h1>"

@app.route("/mul/<num1>/<num2>", methods=["GET"])
def multiplication(num1, num2):
        return f"<h1>Product of {num1} and {num2} = {int(num1)*int(num2)}</h1>"

@app.route("/div/<num1>/<num2>", methods=["GET"])
def division(num1, num2):
        return f"<h1>Division of {num1} and {num2} = {int(num1)/int(num2)}</h1>"
