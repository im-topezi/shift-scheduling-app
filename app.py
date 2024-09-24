from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from os import getenv


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    #db.session.execute(text("INSERT INTO testi (data) VALUES ('testi testi')")) Just some testing of the database
    #db.session.commit()
    return render_template("index.html")



@app.route("/homepage",methods=["POST"])
def homepage():
    times=range(8,21)
    result=db.session.execute(text("SELECT username FROM users"))
    usernames=result.fetchall()
    username=request.form["username"]
    if username not in usernames:
        sql="INSERT INTO users (username) VALUES (:username)"
        db.session.execute(text(sql),{"username":username})
        db.session.commit()
    return render_template("homepage.html",username=username,times=times)




@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])
