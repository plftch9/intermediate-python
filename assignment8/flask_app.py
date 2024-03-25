"""
Paul Fitch
SDEV 300-7615
Wk8 Assignment
4 March 2023

This program renders specific html files, allows users to perform a login,
and allows users to change passwords
"""

import pathlib
import os
import hashlib
import socket
import datetime
from datetime import datetime
from functools import wraps
import pandas as pd
from flask import Flask, render_template, redirect, url_for, flash,  request, session
from wtforms import Form, StringField, PasswordField, validators


app = Flask(__name__)
IMAGES_FOLDER = os.path.join("static", "images")
app.config["UPLOAD_FOLDER"] = IMAGES_FOLDER
FILEPATH = pathlib.Path(os.path.abspath(__file__))
FILEPATH = FILEPATH.with_name("users.csv")


def validate_password(password):
    """
    This function checks strings for required characters
    and prevents users from selecting commonly used passwords
    """
    val = True
    syms = ["!", "@", r"#", "$", "%", "^",
            "&", "*", "(", ")", "_", "-", "+", "="]

    if not any(char.isdigit() for char in str(password)):
        val = False

    if not any(char.isupper() for char in str(password)):
        val = False

    if not any(char.islower() for char in str(password)):
        val = False

    if not any(char in syms for char in str(password)):
        val = False

    for line in open("CommonPassword.txt", "r", encoding="utf-8").readlines():
        if line in password.lower():
            val = False
            break

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
                password = hashlib.sha256(
                    form.password.data.encode()).hexdigest()
                new_user = (username, password)
                data_frame = pd.DataFrame({"username": [new_user[0]],
                                           "password": [new_user[1]]})
                data_frame.to_csv(FILEPATH, mode="a",
                                  index=False, header=False)
                flash("Registration Successful")
                return redirect(url_for("login"))
            flash("Password must have at least 1 upper character, \
                    1 lower character, 1 number, and 1 symbol")
        img_path = os.path.join(app.config["UPLOAD_FOLDER"], "register.jpg")
        return render_template("register.html", form=form, register_image=img_path)

    except Exception as ex:
        return str(ex)


@ app.route("/account", methods=["GET", "POST"])
@ login_required
def account():
    """
    This function validates password changes
    """
    try:
        form = UpdateForm(request.form)
        if request.method == "POST":
            pass_attempt = hashlib.sha256(
                form.old_secret.data.encode()).hexdigest()
            data_frame = pd.read_csv(FILEPATH)
            account_frame = pd.DataFrame({"username": [session["username"]],
                                          "password": [pass_attempt]})
            if pd.merge(data_frame, account_frame, on=["username", "password"],
                        how="inner").empty is False:
                if validate_password(form.new_secret.data):
                    new_word = hashlib.sha256(
                        form.new_secret.data.encode()).hexdigest()
                    data_frame.at[data_frame[data_frame["username"] ==
                                             session["username"]].index.item(),
                                  "password"] = new_word
                    data_frame.to_csv(FILEPATH, mode="w",
                                      index=False, columns=["username", "password"])
                    flash("Password update successful")
                    return redirect(url_for("mainpage"))

            flash("Incorrect old password or commonly used password")
        return render_template("account.html", form=form)
    except Exception as ex:
        return str(ex)


@ app.route('/login', methods=["GET", "POST"])
def login():
    """
    this function validates login requests
    """
    try:
        if request.method == "POST":
            hostname = socket.gethostname()
            ip_addr = socket.gethostbyname(hostname)
            user_attempt = request.form["username"]
            pass_attempt = hashlib.sha256(
                request.form["password"].encode()).hexdigest()
            login_attempt = (user_attempt, pass_attempt)
            login_frame = pd.DataFrame({"username": [login_attempt[0]],
                                        "password": [login_attempt[1]]})
            data_frame = pd.read_csv(FILEPATH)
            if pd.merge(data_frame, login_frame, on=["username", "password"],
                        how="inner").empty is False:
                session["logged_in"] = True
                session["username"] = login_attempt[0]
                flash("Login Successful")
                return redirect(url_for("mainpage"))
            with open("login_fails.txt", "a+", encoding="utf-8") as file:
                file.write(ip_addr)
                file.write(" ")
                file.write(today_date())
                file.write(" ")
                file.write(now_time())
                file.write("\n")
                file.close()
            flash("Wrong username or password")

        img_path = os.path.join(app.config["UPLOAD_FOLDER"], "login.jpg")
        return render_template("login.html", login_image=img_path)
    except Exception as ex:
        return str(ex)


@ app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    if "logged_in" in session:
        session["logger_in"] = False
        session.pop("username", None)
        flash("Logout Successful")
    else:
        flash("You are already logged out")


class UpdateForm(Form):
    """
    This class provieds the forms on the account page
    """
    old_secret = PasswordField("Old Password", validators=[validators.length(
        min=12, max=20), validators.input_required()])
    new_secret = PasswordField("New Password", validators=[validators.length(
        min=12, max=20), validators.input_required()])


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
