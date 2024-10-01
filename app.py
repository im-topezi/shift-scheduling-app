from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from os import getenv


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key=getenv("SECRET_KEY")
db = SQLAlchemy(app)

def admin_check(username):
    admin_search=db.session.execute(text("SELECT username FROM users WHERE role=(SELECT id FROM roles WHERE description='admin')"))
    admins=[item[0] for item in admin_search.fetchall()]
    return username in admins




@app.route("/")
def index():
    times=range(8,21)
    days=["maanantai","tiistai","keskiviikko","torstai","perjantai"]
    return render_template("index.html",times=times,days=days)

@app.route("/tools",methods=["POST"])
def tools():
    users_search=db.session.execute(text("SELECT username,description FROM users LEFT JOIN roles ON roles.id=users.role;"))
    users_and_roles=users_search.fetchall()
    roles=db.session.execute(text("SELECT description FROM roles")).fetchall()
    return render_template("tools.html",users_and_roles=users_and_roles,roles=roles)

@app.route("/tools/set_user_role",methods=["POST"])
def set_user_and_role():
    username=request.form["user"]
    new_role=request.form["new_role"]
    sql="UPDATE users SET role=(SELECT id FROM roles WHERE description=(:new_role)) WHERE username=(:user)"
    db.session.execute(text(sql),{"new_role":new_role,"user":username})
    db.session.commit()
    return tools()

@app.route("/tools/add_new_role",methods=["POST"])
def add_new_role():
    role_name=request.form["added_role"]
    sql="INSERT INTO roles (description) VALUES (:added_role)"
    db.session.execute(text(sql),{"added_role":role_name})
    db.session.commit()
    return tools()

    

@app.route("/login",methods=["POST"])
def login():

    result=db.session.execute(text("SELECT username FROM users"))
    usernames=[item[0] for item in result.fetchall()]
    username=request.form["username"]
    session["username"]=username
    if username not in usernames:
        sql="INSERT INTO users (username) VALUES (:username)"
        db.session.execute(text(sql),{"username":username})
        db.session.commit()
    role_search=db.session.execute(text("SELECT description FROM roles WHERE description='admin'"))
    admin_role=role_search.fetchone()
    if not admin_role:
        db.session.execute(text("INSERT INTO roles (description) VALUES ('admin')"))
        db.session.commit()
        sql="UPDATE users SET role=(SELECT id FROM roles WHERE description='admin') WHERE username=(:username)"
        db.session.execute(text(sql),{"username":username})
        db.session.commit()
    session["admin"]=False
    if admin_check(username):
        session["admin"]=True
    return redirect("/")





"""@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])"""
