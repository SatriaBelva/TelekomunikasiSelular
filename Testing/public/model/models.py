# models/models.py
from . import db  # Mengimpor db dari models/__init__.py

class Item(db.Model):  
    __tablename__ = 'Daftar_Anggota'  # Nama tabel dalam database
    id = db.Column(db.Integer(), primary_key=True)
    NIM = db.Column(db.String(100), nullable=False)  
    nama = db.Column(db.String(100), nullable=False)    
    divisi = db.Column(db.String(100), nullable=False)  
