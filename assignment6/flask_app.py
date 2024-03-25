"""
Paul Fitch
SDEV 300-7615
Wk6 Assignment
21 February 2023

This program renders specific html files
"""

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


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
    return render_template("mainPage.html", today=[date], current_time=[time])


@app.route("/gear")
def gear():
    """
    This function renders gear.html
    """
    return render_template("gear.html")


@app.route("/adventures")
def adventures():
    """
    this function renders adventures.html
    """
    return render_template("adventures.html")


app.run()
