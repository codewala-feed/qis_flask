from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

my_client =  MongoClient("localhost", 27017)
my_db = my_client["calci"]
result = my_db["result"]

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        opr = request.form["opr"]
        if opr == "add":
            output = f"output: {num1} + {num2} = {num1+num2}"
            result.insert_one({
                "num1": num1, "num2":num2, "opr": opr, "output": num1+num2
            })
            return render_template("index.html", data = output)
        elif opr == "sub":
            output = f"output: {num1} - {num2} = {num1-num2}"
            result.insert_one({
                "num1": num1, "num2":num2, "opr": opr, "output": num1-num2
            })
            return render_template("index.html", data = output)
        elif opr == "mul":
            output = f"output: {num1} x {num2} = {num1*num2}"
            result.insert_one({
                "num1": num1, "num2":num2, "opr": opr, "output": num1*num2
            })
            return render_template("index.html", data = output)
        elif opr == "div":
            try:
                output = f"output: {num1} / {num2} = {num1/num2}"
                result.insert_one({
                "num1": num1, "num2":num2, "opr": opr, "output": num1/num2
            })
                return render_template("index.html", data = output)
            except Exception:
                error = f"Please change num2 as non-zero"
                return render_template("index.html", data = error)
    else:
        return render_template("index.html")