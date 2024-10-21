from flask import Flask, request, render_template
from flask_mail import Mail, Message
from pymongo import MongoClient
app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "" #your email
app.config["MAIL_PASSWORD"] = "" #your password
mail = Mail(app)
host = "ocdb.app"
port = 5050
database = "" # your databse
username = "" # your username
password = "" # your password
connection_str = f"mongodb://{username}:{password}@{host}:{port}/{database}"
my_client =  MongoClient(connection_str)
my_db = my_client[database]
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
                msg = Message(subject="Calci Error", 
                        recipients=["codewala.info@gmail.com"],
                        sender="coolcleavers.co.in@gmail.com"
                        )
                msg.body = error
                mail.send(msg)
                return render_template("index.html", data = error)
    else:
        return render_template("index.html")