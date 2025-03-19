# models/__init__.py
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Membuat instance SQLAlchemy yang dapat digunakan di semua file dalam `model/`
db = SQLAlchemy()
bcrypt = Bcrypt()  # Inisialisasi bcrypt di sini
login_manager = LoginManager()  # Inisialisasi bcrypt di sini
