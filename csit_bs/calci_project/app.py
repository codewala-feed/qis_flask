from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

host = "ocdb.app"
port = 5050
database = "db_42vjh6bg4" # your database
username = "user_42vjh6bg4" # your username
password = "p42vjh6bg4" # your password

connection_str = f"mongodb://{username}:{password}@{host}:{port}/{database}"

my_client = MongoClient(connection_str)
my_db = my_client[database]
results = my_db["results"]

valid_users = {
	"tony@gmail.com":"Tony#123",
	"steeve@gmail.com":"Steeve#123",
    "rahul@gmail.com":"Rahul#123"
	}

isLoggedIn = False

@app.route("/", methods=["GET"])
def homepage():
    return render_template("login.html")

@app.route("/login-details", methods=["POST"])
def get_login():
    global isLoggedIn
    email = request.form["email"]
    password = request.form["password"]
    if (email in valid_users) and (valid_users[email] == password):
        isLoggedIn = True
        return redirect("/project")
    else:
        return redirect("/")


@app.route("/project", methods=["GET", "POST"])
def calculator():
    if isLoggedIn == True:
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
    else:
        return redirect("/")