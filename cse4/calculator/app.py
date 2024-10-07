from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calci():
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        opr = request.form["opr"]

        if opr == "add":
            output = f"output: {num1} + {num2} = {num1+num2}"
            return render_template("index.html", data = output)
        elif opr == "sub":
            output = f"output: {num1} - {num2} = {num1-num2}"
            return render_template("index.html", data = output)
        elif opr == "mul":
            output = f"output: {num1} x {num2} = {num1*num2}"
            return render_template("index.html", data = output)
        elif opr == "div":
            try:
                output = f"output: {num1} / {num2} = {num1/num2}"
                return render_template("index.html", data = output)
            except Exception:
                error = "Please change num2 as non-zero"
                return render_template("index.html", data=error)
    else:
        return render_template("index.html")