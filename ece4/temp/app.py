from flask import Flask
from flask_mail import Mail, Message
import pymysql as sql

app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "" #your email
app.config["MAIL_PASSWORD"] = "" #your app password
mail = Mail(app)


my_connection = sql.connect(
    host="ocdb.app",
    port=5051,
    database="", #your database
    user="", #your username
    password="" #your password
)

my_cursor = my_connection.cursor()

table_query = """
    create table if not exists users (
        name varchar(45), 
        phn int, 
        email varchar(50)
    );
"""
my_cursor.execute(table_query)


@app.route("/", methods=["GET"])
def homepage():
    return "Hey Coder, Welcome to Fullstack :)"

@app.route("/insert/<name>/<phn>/<email>", methods=["GET"])
def create(name, phn, email):
    insert_query = """
        insert into users(name, phn, email)
        values (%s, %s, %s);
    """
    values = [name, phn, email]
    my_cursor.execute(insert_query, values)
    my_connection.commit()
    msg = Message(
        subject="SQL Data",
        sender="", #your sender
        recipients=[""] #your receipient
    )
    msg.body = f"{name} {email} {phn} Data Stored, check in ByteXL :)"
    mail.send(msg)
    return f"{name} Data Stored, check in ByteXL :)"