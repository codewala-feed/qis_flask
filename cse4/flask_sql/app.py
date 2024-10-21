from flask import Flask
import pymysql as sql
from flask_mail import Mail, Message

app = Flask(__name__)
my_connection = sql.connect(
    host="ocdb.app",
    port=5051,
    database="", # your databse
    user="", # your user
    passwd="" # your password
)
my_cursor = my_connection.cursor()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)



table_query = """ 
        create table if not exists users (name varchar(45), phn int, 
            email varchar(50)
        );
    """
my_cursor.execute(table_query)

@app.route("/", methods=["GET"])
def homepage():
    return "You are in homepage :)"

@app.route("/insert/<name>/<phn>/<email>", methods=["GET", "POST"])
def create(name, phn, email):
    query = """ 
        insert into users (name, phn, email) values(%s, %s, %s);
    """
    values = [name, phn, email]
    my_cursor.execute(query, values)
    my_connection.commit()

    message = Message('check',sender='',recipients=[""])
    message.body = f"{name} Data Inserted, check in ByteXL :)"
    mail.send(message)

    print(mail)
    return f"{name} Data Inserted, check in ByteXL :)"