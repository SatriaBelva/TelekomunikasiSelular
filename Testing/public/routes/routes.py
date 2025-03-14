from flask import render_template, Blueprint
from model.models import Anggota

routes = Blueprint('routes', __name__)

@routes.route("/")
@routes.route('/home')
@routes.route('/homepage')
def homepage():
    tes   = 'Ini data 1'
    tesss = 'Ini data 2'
    return render_template('index.html', anjay=tes, anjay2=tesss)

@routes.route("/testing")
def testing():
    return render_template('tables.html')

@routes.route("/market")
def market():
    items = Anggota.query.all()
    return render_template('market.html', items=items)

@routes.route("/hello")
def hello_world():
    return "<p>Hello, World anjay!</p>\n<h1>Hallo Saya Satria Belva</h1>"

@routes.route('/profile/<profil>')
def profil(profil):
    return f'<h1><i>Account Profile</i></h1><h4>Nama Saya Adalah {profil}</h4>'



