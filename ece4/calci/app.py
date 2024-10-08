from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "Hey coder, you are in homepage"

@app.route("/wish", methods=["GET"])
def wishpage():
    return "We wish you happy coding :)"

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
            if num2 != 0:
                output = f"{num1} / {num2} = {num1/num2}"
                return render_template("index.html", data=output) 
            else:
                error = "Please change num2 as non-zero"
                return render_template("index.html", data=error)
        else:
            return "Invalid operation"
    else:
        return render_template("index.html")