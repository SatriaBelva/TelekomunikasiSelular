from flask import Blueprint
from routes import routes

# Inisialisasi blueprint untuk route utama
routes = Blueprint('routes', __name__)
