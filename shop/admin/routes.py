from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
import os

@app.route('/')
def home():
    return render_template('admin/index.html', title='GlobalFarm Market Platform')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # hash the password
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit() 
        flash(f'Welcome {form.name.data} Thanks for registering', 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Farmers Registration page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        # check the password that is store on our database
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # save the user in our session
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} you are logedin', 'success')
            # redirect user to the admin page
            return redirect(request.args.get('next') or url_for('home'))
    else:
        flash('Wrong password please try again', 'danger')
    return render_template('admin/login.html', form=form, title="Login Page")