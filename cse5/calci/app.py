from flask import Flask, request, redirect, render_template, flash, get_flashed_messages
from flask_mail import Mail, Message
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "reghwtrerrethrethdthr"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "" #your email
app.config["MAIL_PASSWORD"] = "" #your password
mail = Mail(app)


# my_client = MongoClient("localhost", 27017)
# my_db = my_client["cse5_calci"]
# results =  my_db["results"]



# Get the details from bytexl mongodb connection info
host = "ocdb.app"
port = 5050
database = "db_42vjh6bg4"
username = "user_42vjh6bg4"
password = "p42vjh6bg4"
connection_string = f"mongodb://{username}:{password}@{host}:{port}/{database}"
my_client = MongoClient(connection_string)
my_db = my_client[database]
results =  my_db["results"]

isLoggedIn = False
valid_users = {
		 "steeve@gmail.com":"Steeve#123",
		 "tony@gmail.com":"Tony#123",
         "hulk@gmail.com":"Hulk#123"
		}

@app.route("/", methods=["GET"])
def homepage():
    return render_template("login.html")

@app.route("/login-details", methods=["POST"])
def verify_login():
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
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            opr = request.form["opr"]

            if opr == "add":
                output = f"output: {num1} + {num2} = {num1+num2}"
                results.insert_one(
                    {"number1":num1, "number2":num2, "operator":opr, "result":num1+num2}
                )
                return render_template("index.html", data=output)
            elif opr == "sub":
                output = f"output: {num1} - {num2} = {num1-num2}"
                results.insert_one(
                    {"number1":num1, "number2":num2, "operator":opr, "result":num1-num2}
                )
                return render_template("index.html", data=output)
            
            elif opr == "div":
                try:
                    output = f"output: {num1} / {num2} = {num1/num2}"
                    results.insert_one(
                        {"number1":num1, "number2":num2, "operator":opr, "result":num1/num2}
                    )
                    return render_template("index.html", data=output)
                except Exception as e:
                    error = f"Please Change num2 as non-zero"
                    msg = Message(
                        subject="calci error", sender="coolcleavers.co.in@gmail.com",
                        recipients=["codewala.info@gmail.com"]
                    )
                    msg.body = error
                    mail.send(msg)
                    flash("Mail Sent Successfully")
                    flash(error)
                    return render_template("index.html", data=get_flashed_messages())

            elif opr == "mul":
                output = f"output: {num1} x {num2} = {num1*num2}"
                results.insert_one(
                    {"number1":num1, "number2":num2, "operator":opr, "result":num1*num2}
                )
                return render_template("index.html", data=output)
        else:
            return render_template("index.html")
    else:
        return redirect("/")