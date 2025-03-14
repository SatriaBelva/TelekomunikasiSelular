from . import db  # Mengimpor db dari models/__init__.py

class Divisi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    anggota = db.relationship('Anggota', backref='divisi_rel', lazy=True)  # Pastikan backref ada

class Anggota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NIM = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    divisi_id = db.Column(db.Integer, db.ForeignKey('divisi.id'), nullable=False)  # Pastikan ada foreign key

class User(db.Model) :
    __tablename__ = 'User'  # Nama tabel dalam database
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    password_hashed = db.Column(db.String(60), nullable=False)


# class Divisi(db.Model):
#     __tablename__ = 'Divisi'
#     id = db.Column(db.Integer(), primary_key=True)
#     nama = db.Column(db.String(100), nullable=False)

#     # One-to-Many: Satu divisi memiliki banyak anggota
#     anggota = db.relationship('Anggota', back_populates='divisi')  # Harus cocok

#     def __repr__(self):  
#         return f"{self.nama}" # ✅ Mengubah tampilan default object menjadi nama divisinya

# class Anggota(db.Model):  
#     __tablename__ = 'Daftar_Anggota'  # Nama tabel dalam database
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer(), primary_key=True)
#     NIM = db.Column(db.String(100), nullable=False)  
#     nama = db.Column(db.String(100), nullable=False)
#     divisi_id = db.Column(db.Integer(), db.ForeignKey('Divisi.id'))  
#     divisi_rel = db.relationship('Divisi', back_populates='divisi')  # ✅ Sesuaikan dengan Divisi