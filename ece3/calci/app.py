from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
# get the connection info from bytexl mongodb nimbus
host = "ocdb.app"
port = 5050
database = "" # your database
username = "" # your username
password = "" # your password

connection_str = f"mongodb://{username}:{password}@{host}:{port}/{database}"

my_client = MongoClient(connection_str)
my_db = my_client[database] # database
results = my_db["results"] # collection

@app.route("/", methods=["GET"])
def homepage():
    return "<h1>Hey coder, welcome to homepage</h1>"

@app.route("/project", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        n1 = int(request.form["num1"])
        n2 = int(request.form["num2"])
        o = request.form["opr"]
        
        if o == "add":
            output = f"[CALCI]: {n1} + {n2} = {n1 + n2}"
            results.insert_one(
                {"num1":n1, "num2": n2, "operation":o, "result": n1+n2}
            )
            return render_template("index.html", data=output)
        elif o == "sub":
            output = f"[CALCI]: {n1} - {n2} = {n1 - n2}"
            results.insert_one(
                {"num1":n1, "num2": n2, "operation":o, "result": n1-n2}
            )
            return render_template("index.html", data=output)
        elif o == "mul":
            output = f"[CALCI]: {n1} x {n2} = {n1 * n2}"
            results.insert_one(
                {"num1":n1, "num2": n2, "operation":o, "result": n1*n2}
            )
            return render_template("index.html", data=output) 
        elif o == "div":
            try:
                output = f"[CALCI]: {n1} / {n2} = {n1 / n2}"
                results.insert_one(
                {"num1":n1, "num2": n2, "operation":o, "result": n1/n2}
            )
                return render_template("index.html", data=output)
            except Exception:
                error = "Please change num2 as non-zero"
                return render_template("index.html", data=error)
    else:
        return render_template("index.html")