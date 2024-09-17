from flask import Flask
from flask import render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page/<int:id>")
def page(id):
    return "Tämä on sivu " + str(id)




@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])
