from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello AI world!"

# FLASK_APP=21_flask.py  flask run

##########################

from flask import Flask, render_template, redirect, url_for, request
from student import student

students=[]
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def students_page():
    if request.method == 'POST':
        new_student_id = request.form.get("student-id")
        ...
