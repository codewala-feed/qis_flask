from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "<h1>You are in homepage</h1>"

@app.route("/project", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        opr = request.form["opr"]

        if opr == "add":
            output = f"{num1} + {num2} = {num1+num2}"
            return render_template("index.html", data=output)
        elif opr == "sub":
            output = f"{num1} - {num2} = {num1-num2}"
            return render_template("index.html", data=output) 
        elif opr == "mul":
            output = f"{num1} x {num2} = {num1*num2}"
            return render_template("index.html", data=output) 
        elif opr == "div":
            output = f"{num1} / {num2} = {num1/num2}"
            return render_template("index.html", data=output) 
        else:
            return "Invalid Operation"
    else:
        return render_template("index.html")