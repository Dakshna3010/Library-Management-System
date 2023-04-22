from flask import Blueprint,render_template

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/student_login')
def student_home():
    return render_template("student.html")