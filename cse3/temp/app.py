from flask import Flask
import pymysql as sql

app = Flask(__name__)
my_connection = sql.connect(
    host="ocdb.app",
    port=5051,
    database="db_42veu6nve", #your database
    user="user_42veu6nve", #your username
    password="p42veu6nve" #your password
)
my_cursor = my_connection.cursor()
query = """ 
    create table if not exists users (name varchar(45), 
                phn int, email varchar(50));
"""
my_cursor.execute(query)
@app.route("/", methods=["GET"])
def homepage():
    return "You are in homepage"

@app.route("/create/<name>/<int:phn>/<email>", methods=["GET"])
def insert(name, phn, email):
    query = """ 
        insert into users (name, phn, email) values(%s, %s, %s)
    """
    values = [name, phn, email]
    my_cursor.execute(query, values)
    my_connection.commit()
    return f"{name} Data Inserted Successfully, check in byteXL"