# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

# Membuat instance SQLAlchemy yang dapat digunakan di semua file dalam `model/`
db = SQLAlchemy()
