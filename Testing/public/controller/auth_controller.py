from flask import render_template, redirect, url_for
from model.models import User, db
from forms import RegisterForm

class AuthController:
    @staticmethod
    def register():
        form = RegisterForm()
        register = 'Register Account'

        if form.validate_on_submit():
            user_to_create = User(
                username=form.username.data,
                email=form.email.data,
                password_hashed = form.password1.data
            )
            db.session.add(user_to_create)
            db.session.commit()
            return redirect(url_for('routes.homepage'))  # Sesuaikan dengan blueprint routes
        
        if form.errors != {} : #Kalo gaada error dari validasinya
            for err_msg in form.errors.values():
                print(f"ERROR: {err_msg}")
        
        return render_template('register.html', form=form, register=register)
