from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import Book, User, Category
from . import db

auth=Blueprint('auth',__name__)

@auth.route('/',methods=['GET','POST'])
def login():
    if request.form == 'POST':
        U_name=request.form.get('U_name')
        U_pass=request.form.get('U_pass')
    
    if U_name == "librarian123" and U_pass == "librarian@123":
        return redirect(url_for("views.home"))
    else:
         flash("Invalid credentials", category = "error")
    return render_template("home.html")
@auth.route("/student-login", methods = ['GET', 'POST'])
def student_login():
    if request.method == "POST":
        u_name = request.form.get("uname")
        passwd =  request.form.get("pass")
        user = User.query.filter_by(username = u_name).first()
        if user:
            if user.password == passwd:
                return redirect(url_for("views.student_home"))
            else:
                flash("Invalid Password", category= "error")
        else:
            flash("User does not exist !! Try signing up", category= 'error')
    return render_template("student_login.html")