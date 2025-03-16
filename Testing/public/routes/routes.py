from flask import render_template, Blueprint, redirect, url_for
from model.models import Anggota,Divisi,db,User
from forms import RegisterForm
from controller import AuthController
# from werkzeug.security import generate_password_hash

routes = Blueprint('routes', __name__)

@routes.route("/")
@routes.route('/home')
@routes.route('/homepage')
def homepage():
    tes   = 'Ini data 1'
    tesss = 'Ini data 2'
    return render_template('homepage.html', anjay=tes, anjay2=tesss)

@routes.route("/daftar_divisi")
def daftar_divisi():
    divisi=Divisi.query.all()
    return render_template('daftar_divisi.html', divisi=divisi)

@routes.route("/daftar_tim")
def daftar_tim():
    items = Anggota.query.all()
    return render_template('daftar_tim.html', items=items)

@routes.route("/register", methods=['GET', 'POST'])
def register():
    return AuthController.register()

@routes.route("/hello")
def hello_world():
    return "<p>Hello, World anjay!</p>\n<h1>Hallo Saya Satria Belva</h1>"

@routes.route('/profile/<profil>')
def profil(profil):
    return f'<h1><i>Account Profile</i></h1><h4>Nama Saya Adalah {profil}</h4>'



