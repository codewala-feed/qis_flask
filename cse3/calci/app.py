from flask import Flask, request, render_template, redirect
from flask_mail import Mail, Message
from pymongo import MongoClient

app = Flask(__name__)

# # mail configurations
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "" #your email
# app.config["MAIL_PASSWORD"] = "" #your password
# mail = Mail(app)

# Database configurations
host = "ocdb.app"
port = 5050
database = "db_42vjh6bg4" # your databse
username = "user_42vjh6bg4" # your username
password = "p42vjh6bg4" # your password
connection_str = f"mongodb://{username}:{password}@{host}:{port}/{database}"
my_client =  MongoClient(connection_str)

my_db = my_client[database]
result = my_db["result"]

isLoggedIn = False
valid_users = {"steeve@gmail.com":"Steeve#123","mahesh@gmail.com": "Mahesh#123"}

@app.route("/", methods=["GET"])
def homepage():
    return render_template("login.html")

@app.route("/login-details", methods=["POST"])
def verify_login():
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
                    # msg = Message(subject="Calci Error", 
                    #         recipients=["codewala.info@gmail.com"],
                    #         sender="coolcleavers.co.in@gmail.com"
                    #         )
                    # msg.body = error
                    # mail.send(msg)
                    return render_template("index.html", data = error)
        else:
            return render_template("index.html")
    else:
        return redirect("/")

app.run(debug=True) 