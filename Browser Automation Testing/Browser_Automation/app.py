
from flask import Flask, request, render_template

app = Flask(__name__)
users = {}

@app.route("/")
def home():

    return render_template("registration.html",message="")

@app.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    users[username] = {"email": email,"password": password}

    return render_template("registration.html", message="Registration Successful")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username]["password"] == password:message = "Login Successful"

    else:

        message = "Invalid Username or Password"

    return render_template( "registration.html",message=message)

if __name__ == "__main__":
    app.run(debug=True)
