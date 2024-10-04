from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "<h1>Hey Coder, You are in homepage</h1>"

@app.route("/wish", methods=["GET"])
def wishpage():
    return "<h1>We wish you happy coding :)</h1>"


@app.route("/add/<num1>/<num2>", methods=["GET"])
def addition(num1, num2):
    return f"<h1>{num1} + {num2} = {int(num1) + int(num2)}</h1>"

@app.route("/sub/<num1>/<num2>", methods=["GET"])
def subtraction(num1, num2):
    return f"<h1>{num1} - {num2} = {abs(int(num1) - int(num2))}</h1>"

@app.route("/mul/<num1>/<num2>", methods=["GET"])
def multiplication(num1, num2):
    return f"<h1>{num1} X {num2} = {int(num1) * int(num2)}</h1>"

@app.route("/div/<num1>/<num2>", methods=["GET"])
def division(num1, num2):
    if num2 != '0':
        return f"<h1>{num1} / {num2} = {int(num1) / int(num2)}</h1>"
    else:
        return "<h1>Please change num2 as non-zero</h1>"
    

@app.route("/calci/<opr>/<num1>/<num2>", methods=["GET"])
def calculator(opr, num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    if opr == "add":
        return f"<h1>{num1} + {num2} = {(num1) + (num2)}</h1>"
    elif opr == "sub":
        return f"<h1>{num1} - {num2} = {abs((num1) - (num2))}</h1>"
    elif opr == "mul":
        return f"<h1>{num1} X {num2} = {(num1) * (num2)}</h1>"
    elif opr == "div":
        if num2 != '0':
            return f"<h1>{num1} / {num2} = {(num1) / (num2)}</h1>"
        else:
            return "<h1>Please change num2 as non-zero</h1>"
    else:
        return "<h1>Invalid Operator</h1>"