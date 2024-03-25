"""
Paul Fitch
SDEV 300-7615
Wk6 Assignment
21 February 2023

This program renders specific html files
"""

import os
import hashlib
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, redirect, url_for, flash,  request, session
from wtforms import Form, StringField, PasswordField, validators


app = Flask(__name__)
IMAGES_FOLDER = os.path.join("static", "images")
app.config["UPLOAD_FOLDER"] = IMAGES_FOLDER


def validate_password(password):
    """
    This function checks strings for required characters
    """
    val = True
    syms = ["!", "@", "\#", "$", "%", "^",
            "&", "*", "(", ")", "_", "-", "+", "="]

    if not any(char.isdigit() for char in str(password)):
        val = False

    if not any(char.isupper() for char in str(password)):
        val = False

    if not any(char.islower() for char in str(password)):
        val = False

    if not any(char in syms for char in str(password)):
        val = False

    return val


def login_required(fnc):
    """
    This wrapper function prevents access to pages without being logged in
    """
    @wraps(fnc)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return fnc(*args, **kwargs)
        flash("You must log in first")
        return redirect(url_for("login"))
    return wrap


def today_date():
    """
    This function retrieves, formats, and returns today's date
    """
    today = datetime.today()
    date_format = today.strftime("%B %d, %Y")

    return date_format


def now_time():
    """
    This function retrieves, formats, and returns the current time
    """
    exact_time = datetime.now().time()
    time_format = exact_time.strftime("%H:%M")

    return time_format


@app.route("/")
def mainpage():
    """
    This function renders mainPage.html and populates the date / time
    portion of the page
    """
    date = today_date()
    time = now_time()
    img_path = os.path.join(app.config["UPLOAD_FOLDER"], "scuba1.jpg")
    return render_template("mainPage.html", today=[date], current_time=[time], main_image=img_path)


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    this function validates login requests
    """
    try:
        if request.method == "POST":
            user_attempt = request.form["username"]
            pass_attempt = request.form["password"].encode()
            for line in open("users.txt", "r", encoding="utf-8").readlines():
                login_info = line.split()
                if user_attempt == login_info[0] and \
                        hashlib.sha256(pass_attempt).hexdigest() == login_info[1]:
                    session["logged_in"] = True
                    flash("Login Successful")
                    return redirect(url_for("mainpage"))
            flash("Wrong username or password")

        img_path = os.path.join(app.config["UPLOAD_FOLDER"], "login.jpg")
        return render_template("login.html", login_image=img_path)
    except Exception as ex:
        return str(ex)


class RegisterForm(Form):
    """
    this class provides the forms on the register page
    """

    username = StringField("Username", validators=[validators.length(
        min=5, max=15), validators.input_required()])
    password = PasswordField("Password", validators=[validators.length(
        min=12, max=20), validators.input_required()])
    # validators.regexp(
    #     r"^[.*a-z]", message="Must contain at least 1 lower case character"),
    # validators.regexp(
    # r"^[.*A-Z]", message="Must contain at least 1 upper case character"),
    # validators.regexp(
    #     r"^[.*0-9]", message="Must contain at least 1 number"),
    # validators.regexp(r"^[.*^A-Za-z0-9]", message="Must contain at least 1 symbol")])


@ app.route("/register", methods=["GET", "POST"])
def register():
    """
    this function validates register requests, encrypts / hashes passwords, and
    writes usernames / passwords to a file
    """
    try:
        form = RegisterForm(request.form)
        if request.method == "POST" and form.validate():
            username = form.username.data
            if validate_password(form.password.data):
                password = form.password.data.encode()
                with open("users.txt", "a+", encoding="utf-8") as file:
                    file.write(username)
                    file.write(" ")
                    file.write(hashlib.sha256(password).hexdigest())
                    file.write("\n")
                    file.close()
                    flash("Registration Successful")
                    return redirect(url_for("login"))
            else:
                flash("Password must have at least 1 upper character, \
                                  1 lower character, 1 number, and 1 symbol")
        img_path = os.path.join(app.config["UPLOAD_FOLDER"], "register.jpg")
        return render_template("register.html", form=form, register_image=img_path)

    except Exception as ex:
        return str(ex)


@ app.route("/gear")
@ login_required
def gear():
    """
    This function renders gear.html
    """
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template("gear.html")


@ app.route("/adventures")
@ login_required
def adventures():
    """
    this function renders adventures.html
    """
    if not session.get('logged_in'):
        return render_template('login.html')
    img_path = os.path.join(app.config["UPLOAD_FOLDER"], "scuba2.jpg")
    return render_template("adventures.html", adventure_image=img_path)


app.secret_key = os.urandom(12)
app.run()
