from flask import render_template, Blueprint
from model.models import Anggota,Divisi,db,User
from forms import RegisterForm

routes = Blueprint('routes', __name__)

@routes.route("/")
@routes.route('/home')
@routes.route('/homepage')
def homepage():
    tes   = 'Ini data 1'
    tesss = 'Ini data 2'
    return render_template('homepage.html', anjay=tes, anjay2=tesss)

@routes.route("/testing")
def testing():
    divisi=Divisi.query.all()
    return render_template('testing.html', divisi=divisi)

@routes.route("/daftar_tim")
def daftar_tim():
    items = Anggota.query.all()
    return render_template('daftar_tim.html', items=items)

@routes.route("/register")
def register():
    form = RegisterForm()
    register = 'Register Account'
    return render_template('register.html', form = form, register=register)

@routes.route("/hello")
def hello_world():
    return "<p>Hello, World anjay!</p>\n<h1>Hallo Saya Satria Belva</h1>"

@routes.route('/profile/<profil>')
def profil(profil):
    return f'<h1><i>Account Profile</i></h1><h4>Nama Saya Adalah {profil}</h4>'



