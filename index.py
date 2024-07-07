# run with: flask --app index --debug run

"""
Lab — Flask, Part 2
CST 205
Vera Boukhonine
07/06/2024
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

my_info = {"flavors": ["sweet", "sour"], "colors": ["blue", "green", "brown"]}


# Task 2
@app.route("/")
def home():
    return render_template("page1.html")


# Task 3
@app.route("/page2")
def p2():
    return render_template("page2.html", my_info=my_info)


# Task 4

@app.route("/page3")
def p3():
    return render_template("page3.html")


"""
Lab Completion Report: 
I finished all the tasks in the lab to the best of my abilities. I spent some
time looking a bootstrap templates and designed another page to use them.
"""