from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required
from model.models import Anggota,Divisi,db,User
from controller import AuthController
# from werkzeug.security import generate_password_hash

routes = Blueprint('routes', __name__)

@routes.route("/")
@routes.route('/home')
@routes.route('/homepage')
@login_required
def homepage():
    tes   = 'Ini data 1'
    tesss = 'Ini data 2'
    return render_template('homepage.html', anjay=tes, anjay2=tesss)

@routes.route("/tes")
def tes():
    return render_template('tes.html')

@routes.route("/daftar_divisi")
@login_required
def daftar_divisi():
    divisi=Divisi.query.all()
    return render_template('daftar_divisi.html', divisi=divisi)

@routes.route("/daftar_tim")
@login_required
def daftar_tim():
    items = Anggota.query.all()
    return render_template('daftar_tim.html', items=items)

@routes.route("/register", methods=['GET', 'POST'])
def register():
    return AuthController.register()

@routes.route("/login", methods=['GET', 'POST'])
def login():
    return AuthController.login()

@routes.route("/logout", methods=['GET', 'POST'])
def logout():
    return AuthController.logout()



