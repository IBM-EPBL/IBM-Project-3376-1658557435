from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template("about.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signin", methods = ['POST', 'GET'])
def signin():  
  return render_template("signin.html")

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
  return render_template("signup.html")

@app.route("/tq")
def tq():
  return render_template("tq.html", e="test")