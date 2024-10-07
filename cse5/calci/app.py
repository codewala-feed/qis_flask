from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
my_client = MongoClient("localhost", 27017)
my_db = my_client["cse5_calci"]
results =  my_db["results"]

@app.route("/", methods=["GET", "POST"])
def calculator():
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
                return render_template("index.html", data=error)

        elif opr == "mul":
            output = f"output: {num1} x {num2} = {num1*num2}"
            results.insert_one(
                {"number1":num1, "number2":num2, "operator":opr, "result":num1*num2}
            )
            return render_template("index.html", data=output)
    else:
        return render_template("index.html")