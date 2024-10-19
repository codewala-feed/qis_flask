from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
host = "ocdb.app"
port = 5050
database = "db_42vfgee3d" # your database
username = "user_42vfgee3d" # your username
password = "p42vfgee3d" # your password
 
connection_string = f"mongodb://{username}:{password}@{host}:{port}/{database}"
my_connection = MongoClient(connection_string)
my_db = my_connection[database]
results = my_db["results"]

@app.route("/", methods=["GET", "POST"])
def calci():
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        opr = request.form["opr"]

        if opr == "add":
            output = f"output: {num1} + {num2} = {num1+num2}"
            results.insert_one(
                {"number1": num1, "number2": num2, "operator":opr, "result":num1+num2}
            )
            return render_template("index.html", data = output)
        elif opr == "sub":
            output = f"output: {num1} - {num2} = {num1-num2}"
            results.insert_one(
                {"number1": num1, "number2": num2, "operator":opr, "result":num1-num2}
            )
            return render_template("index.html", data = output)
        elif opr == "mul":
            output = f"output: {num1} x {num2} = {num1*num2}"
            results.insert_one(
                {"number1": num1, "number2": num2, "operator":opr, "result":num1*num2}
            )
            return render_template("index.html", data = output)
        elif opr == "div":
            try:
                output = f"output: {num1} / {num2} = {num1/num2}"
                results.insert_one(
                {"number1": num1, "number2": num2, "operator":opr, "result":num1/num2}
            )
                return render_template("index.html", data = output)
            except Exception:
                error = "Please change num2 as non-zero"
                return render_template("index.html", data=error)
    else:
        return render_template("index.html")