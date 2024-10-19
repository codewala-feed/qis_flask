from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

host = "ocdb.app"
port = 5050
database = "" # your database
username = "" # your username
password = "" # your password

connection_str = f"mongodb://{username}:{password}@{host}:{port}/{database}"

my_client = MongoClient(connection_str)
my_db = my_client[database]
results = my_db["results"]


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
            results.insert_one(
                {"num1":num1, "num2":num2, "opr":opr, "result":num1+num2}
            )
            return render_template("index.html", data=output)
        elif opr == "sub":
            output = f"{num1} - {num2} = {num1-num2}"
            results.insert_one(
                {"num1":num1, "num2":num2, "opr":opr, "result":num1-num2}
            )
            return render_template("index.html", data=output) 
        elif opr == "mul":
            output = f"{num1} x {num2} = {num1*num2}"
            results.insert_one(
                {"num1":num1, "num2":num2, "opr":opr, "result":num1*num2}
            )
            return render_template("index.html", data=output) 
        elif opr == "div":
            try:
                output = f"{num1} / {num2} = {num1/num2}"
                results.insert_one(
                {"num1":num1, "num2":num2, "opr":opr, "result":num1/num2}
            )
                return render_template("index.html", data=output)
            except Exception:
                error = "Please change num2 as non-zero"
                return  render_template("index.html", data=error)
        else:
            return "Invalid Operation"
    else:
        return render_template("index.html")