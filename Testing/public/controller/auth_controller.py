from flask import render_template, redirect, url_for, flash, get_flashed_messages
from flask_login import login_user, logout_user
from forms import RegisterForm, LoginForm
from model.models import User, db

class AuthController:
    @staticmethod
    def register():
        form = RegisterForm()
        register = 'Register Account'

        if form.validate_on_submit():
            user_to_create = User(
                username    = form.username.data,
                email       = form.email.data,
                password    = form.password1.data
            )

            db.session.add(user_to_create)
            db.session.commit() 
            login_user(user_to_create)  # Pindahkan setelah commit

            # Tambahkan pesan sukses
            flash(f'Account Created Successfully! You are now logged in as {user_to_create.username}', category='success')

            return redirect(url_for('routes.homepage'))  # Sesuaikan dengan blueprint routes
        
        if form.errors:
            for field, err_msg in form.errors.items():
                flash(f"{field}: {', '.join(err_msg)}", category='danger')
        
        return render_template('register.html', form=form, register=register)
    
    @staticmethod
    def login():
        form = LoginForm()

        # Hapus pesan flash lama sebelum login
        # get_flashed_messages()

        if form.validate_on_submit():
            attempted_user = User.query.filter_by(username=form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
                login_user(attempted_user)
                flash(f'Success! You are logged in as : {attempted_user.username}', category='success')
                return redirect(url_for('routes.homepage'))
            else:
                flash(f'Wrong Password are not match', category='danger')
                return render_template('login.html', form=form)  # <-- Ubah redirect ke render_template
        return render_template('login.html', form=form)
    
    @staticmethod
    def logout():
        logout_user()
        flash('You have been logout', category='info')
        return redirect(url_for('routes.login'))