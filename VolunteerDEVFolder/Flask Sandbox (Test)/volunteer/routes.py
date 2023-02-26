from flask import Flask, render_template, url_for, session, request, flash, redirect
from volunteer import app, db
from flask_login import login_user, logout_user, current_user
from volunteer.models import User
from volunteer.forms import RegistrationForm, LoginForm

@app.route('/', methods=['GET','POST'])
def landing():
    return redirect(url_for("home"))

@app.route("/home", methods=['GET','POST'])
def home():
    #posts = Post.query.all()
    # return render_template('home.html', posts=posts)
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html',title='About Me')