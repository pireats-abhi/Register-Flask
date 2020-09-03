from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_PORT'] = db['mysql_port']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM registrants")
    userDetails = cur.fetchall()
    return render_template("index.html", userDetails=userDetails)

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("appology.html", message="You must provide a name.")
        email = request.form.get("email")
        if not email:
            return render_template("appology.html", message="You must provide a email address.")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO registrants (name, email) VALUES (%s, %s)", [name, email])
        mysql.connection.commit()
        cur.close()
        return redirect("/")