from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
# get the below details from byteXL nimbus
host = "ocdb.app"
port = 5050
database = "" # your database
username = "" # your username
password = "" # your password

connection_string = f"mongodb://{username}:{password}@{host}:{port}/{database}"

my_client = MongoClient(connection_string)
my_db = my_client[database] #database
results = my_db["results"] # collection

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
            results.insert_one(
                {"n1":num1, "n2":num2, "operation":opr, "result":num1+num2}
            )
            return render_template("index.html", data=output)
        elif opr == "sub":
            output = f"{num1} - {num2} = {num1-num2}"
            results.insert_one(
                {"n1":num1, "n2":num2, "operation":opr, "result":num1-num2}
            )
            return render_template("index.html", data=output) 
        elif opr == "mul":
            output = f"{num1} x {num2} = {num1*num2}"
            results.insert_one(
                {"n1":num1, "n2":num2, "operation":opr, "result":num1*num2}
            )
            return render_template("index.html", data=output) 
        elif opr == "div":
            if num2 != 0:
                output = f"{num1} / {num2} = {num1/num2}"
                results.insert_one(
                {"n1":num1, "n2":num2, "operation":opr, "result":num1/num2}
            )
                return render_template("index.html", data=output) 
            else:
                error = "Please change num2 as non-zero"
                return render_template("index.html", data=error)
        else:
            return "Invalid operation"
    else:
        return render_template("index.html")