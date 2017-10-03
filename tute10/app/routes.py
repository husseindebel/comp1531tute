from setup import app, db
from flask import render_template, request
from models import User
import json

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("something")
    return render_template("something.html", user=User.query.all())

@app.route('/add', methods=['POST'])
def addUser():
    username = request.form['username']
    # add into database
    print(username, "yes yes")
    email = request.form['email']
    print(email)
    
    new = User(username=username, email=email)
    db.session.add(new)
    db.session.commit()


    return "something"

