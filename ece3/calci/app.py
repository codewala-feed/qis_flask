from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
# get the connection info from bytexl mongodb nimbus
host = "ocdb.app"
port = 5050
database = "db_42vjh6bg4" # your database
username = "user_42vjh6bg4" # your username
password = "p42vjh6bg4" # your password

connection_str = f"mongodb://{username}:{password}@{host}:{port}/{database}"

my_client = MongoClient(connection_str)
my_db = my_client[database] # database
results = my_db["results"] # collection


valid_users = {
    "steeve@gmail.com":"Steeve#123",
    "tony@gmail.com":"Tony#123",
    "ravi@gmail.com":"Ravi#123"
    }
isLoggedIn = False

@app.route("/", methods=["GET"])
def homepage():
    return render_template("login.html")

@app.route("/login-details", methods=["POST"])
def get_details():
    global isLoggedIn
    email = request.form["email"]
    password = request.form["password"]
    if email in valid_users and password == valid_users[email]:
        isLoggedIn = True
        return redirect("/project")
    else:
        return redirect("/")

@app.route("/project", methods=["GET", "POST"])
def calculator():
    if isLoggedIn == True:
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
    else:
        return redirect("/")