from flask import Blueprint

# Inisialisasi blueprint untuk route utama
routes = Blueprint('routes', __name__)

# Import semua routes agar bisa digunakan
from routes import routes