from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/home/<username>")
def userHome(username):
    return f"<h1>Hello {username}, welcome back.</h1>"
