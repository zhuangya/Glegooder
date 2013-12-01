from contextlib import closing

import pymongo
from flask import Flask, flash, render_template


DEBUG = True
SECRET_KEY = "123"
USERNAME = "admin"
PASSWORD = "admin"


app = Flask(__name__)
app.config.from_object(__name__)


def get_db():
    if not hasattr(g, "connection"):
        g.connection = pymongo.MongoClient()
    return g.connection

@teardown_request
def teardown_request(error):
    if hasattr(g, "connection"):
        g.connection.disconnect()


@app.route("/add", method=['POST'])
def create_todo_event():
    pass

@app.route("/register", method=['GET', 'POST'])
def register():
    if request.method == "POST":
        error_list = []
        if not request.form["username"]:
            error_list.append("You have to enter a username")
        if not request.form["email"] or "@" not in request.form["email"]:
            error_list.append("You have to enter a valid email address")
        if not request.form["password"]:
            error_list.append("You have to enter a password")
        if request.form["repassword"] != request.form["password"]:
            error_list.append("two passwords are not match")

        if not error_list:
            user_db = get_db()["user"]
            user_db.insert(
                {
                    "name": request.form["username"],
                    "email": request.form["email"],
                    "password": request.form["password"],
                }
            )
            flash("You were successfully registered and can login now!")
    return render_template("register.html", error_list)

if __name__ == "__main__":
    app.run()
